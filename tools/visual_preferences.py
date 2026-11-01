"""Private, portable visual preferences. No network access or provider credentials."""
import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import sys
import tempfile

TEXT_FIELDS = {'provider', 'model', 'style', 'typography', 'layout', 'aspect_ratio',
               'text_language', 'signature', 'first_image_priority'}
LIST_FIELDS = {'palette', 'references', 'avoid'}
SOURCES = {'user-assets', 'screenshots', 'ai', 'mixed'}


def absolute(value):
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise ValueError('Preference paths must be absolute.')
    return path.resolve()


def default_path(environ=None, platform=None, home=None):
    env = os.environ if environ is None else environ
    platform = sys.platform if platform is None else platform
    home = Path.home() if home is None else Path(home)
    if env.get('FOR_YOU_SKILLS_CONFIG_DIR'):
        base = absolute(env['FOR_YOU_SKILLS_CONFIG_DIR'])
    elif platform == 'win32':
        base = absolute(env['APPDATA']) if env.get('APPDATA') else home/'AppData/Roaming'
        base /= 'for-you-skills'
    elif platform == 'darwin':
        base = home/'Library/Application Support/for-you-skills'
    else:
        base = absolute(env['XDG_CONFIG_HOME']) if env.get('XDG_CONFIG_HOME') else home/'.config'
        base /= 'for-you-skills'
    return base/'visual-preferences.json'


def private_path(value):
    path = absolute(value)
    for parent in path.parents:
        if (parent/'.git').exists() or (parent/'SKILL.md').exists():
            raise ValueError('Keep preferences outside repositories and installed skill directories.')
        if parent.name.lower() in {'skills', 'remote-skills'}:
            raise ValueError('Keep preferences outside installed skill directories.')
    return path


def validate_scope(scope):
    if scope != 'default' and not re.fullmatch(r'(account|series):[^\s\x00-\x1f]{1,160}', scope):
        raise ValueError('Use default, account:<id> or series:<id> as the scope.')


def validate_profile(profile):
    if not isinstance(profile, dict) or not profile:
        raise ValueError('A profile must be a nonempty object.')
    allowed = TEXT_FIELDS | LIST_FIELDS | {'source'}
    if set(profile) - allowed:
        raise ValueError('Unsupported profile field. Credentials and tool configuration are not preferences.')
    for key, value in profile.items():
        if key == 'source':
            if not isinstance(value, str) or value not in SOURCES:
                raise ValueError('source must be user-assets, screenshots, ai or mixed.')
        elif key in TEXT_FIELDS:
            if not isinstance(value, str) or not value.strip() or len(value) > 4000:
                raise ValueError(key+' must be a nonempty string of at most 4000 characters.')
        elif (not isinstance(value, list) or len(value) > 30 or
              any(not isinstance(x, str) or not x.strip() or len(x) > 4000 for x in value)):
            raise ValueError(key+' must be a list of at most 30 nonempty strings.')
    return profile


def validate_store(store):
    if not isinstance(store, dict) or set(store) != {'schema_version', 'revision', 'profiles'}:
        raise ValueError('Invalid preference document fields.')
    if type(store['schema_version']) is not int or store['schema_version'] != 1:
        raise ValueError('Unsupported preference schema version; existing file was left unchanged.')
    if type(store['revision']) is not int or store['revision'] < 0:
        raise ValueError('Invalid revision.')
    if not isinstance(store['profiles'], dict):
        raise ValueError('profiles must be an object.')
    for scope, profile in store['profiles'].items():
        validate_scope(scope)
        validate_profile(profile)
    return store


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def read_store(path):
    if not path.exists():
        return {'schema_version': 1, 'revision': 0, 'profiles': {}}
    return validate_store(read_json(path))


@contextmanager
def locked(path):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    lock = path.with_name(path.name+'.lock')
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError('Preferences are busy. Retry after the other writer finishes; do not overwrite its lock.')
    try:
        os.close(fd)
        yield
    finally:
        lock.unlink()


def atomic_write(path, store):
    validate_store(store)
    fd, temporary = tempfile.mkstemp(prefix='.visual-prefs-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as output:
            json.dump(store, output, ensure_ascii=False, indent=2)
            output.write('\n')
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def selection(path, store, scope, overrides=None):
    validate_scope(scope)
    resolved = scope if scope in store['profiles'] else 'default'
    profile = store['profiles'].get(resolved)
    if overrides is not None:
        validate_profile(overrides)
        profile = dict(profile or {}, **overrides)
    return {'path': str(path), 'revision': store['revision'], 'requested_scope': scope,
            'resolved_scope': resolved if resolved in store['profiles'] else None,
            'profile': profile, 'temporary_override': overrides is not None}


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument('--file', help='Absolute private JSON path; defaults to the user configuration directory.')
    commands = result.add_subparsers(dest='command', required=True)
    commands.add_parser('path', help='Show the persistence path without creating it.')
    show = commands.add_parser('show', help='Read a scoped profile, falling back to default; never writes.')
    show.add_argument('--scope', default='default')
    show.add_argument('--override', help='Temporary profile JSON file to merge for this read only.')
    save = commands.add_parser('save', help='Replace one explicitly chosen profile, preserving other scopes.')
    save.add_argument('--scope', default='default')
    save.add_argument('--input', required=True, help='Profile object JSON, not a full exported document.')
    save.add_argument('--expect-revision', type=int, help='Reject stale writes; use the revision returned by show.')
    export = commands.add_parser('export', help='Write a portable validated copy to a new private file.')
    export.add_argument('--output', required=True)
    imp = commands.add_parser('import', help='Merge a validated export; conflicting profiles require --replace.')
    imp.add_argument('--input', required=True)
    imp.add_argument('--replace', action='store_true', help='Replace conflicting scopes, preserving all other scopes.')
    return result


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    args = parser().parse_args()
    try:
        path = private_path(args.file or default_path())
        if args.command == 'path':
            result = {'path': str(path), 'exists': path.exists()}
        elif args.command == 'show':
            result = selection(path, read_store(path), args.scope,
                               read_json(args.override) if args.override else None)
        elif args.command == 'export':
            store = read_store(path)
            target = private_path(args.output)
            with locked(target):
                if target.exists():
                    raise ValueError('Export destination exists; choose a new private file.')
                atomic_write(target, store)
            result = {'exported': str(target), 'profiles': list(store['profiles'])}
        else:
            incoming = read_json(args.input)
            if args.command == 'save':
                validate_profile(incoming)
                validate_scope(args.scope)
            else:
                validate_store(incoming)
            with locked(path):
                store = read_store(path)
                if args.command == 'save':
                    if args.expect_revision is not None and args.expect_revision != store['revision']:
                        raise ValueError('Stale revision; read current preferences before saving again.')
                    store['profiles'][args.scope] = incoming
                else:
                    for scope, profile in incoming['profiles'].items():
                        if (scope in store['profiles'] and store['profiles'][scope] != profile
                                and not args.replace):
                            raise ValueError('Import conflicts with '+scope+'; review before using --replace.')
                    store['profiles'].update(incoming['profiles'])
                store['revision'] += 1
                atomic_write(path, store)
            result = {'saved': str(path), 'revision': store['revision'], 'profiles': list(store['profiles'])}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
