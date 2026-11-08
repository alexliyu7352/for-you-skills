#!/usr/bin/env python3
"""Read-only comparison of the reviewed algorithm snapshot with public upstream.

Requires Python 3.9+ and Git. Exit 0 means a comparison succeeded (including
review_required); exit 2 means no trustworthy comparison could be produced.
Neither mode updates the checkpoint, knowledge, skills, or a supplied local repo.
"""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'xai-org/x-algorithm'
UPSTREAM_URL = 'https://github.com/' + REPOSITORY + '.git'


class CheckError(Exception):
    """An incomplete or invalid comparison; never a clean result."""


def git(repo, *args, check=True):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_OPTIONAL_LOCKS='0',
               GIT_NO_REPLACE_OBJECTS='1', GIT_NO_LAZY_FETCH='1',
               GIT_ASKPASS='', SSH_ASKPASS='')
    command = ['git', '-c', 'credential.helper=', '-C', str(repo), *args]
    try:
        result = subprocess.run(command, capture_output=True, encoding='utf-8',
                                errors='replace', env=env, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CheckError('Git operation failed: ' + str(exc)) from exc
    if check and result.returncode:
        detail = result.stderr.strip() or 'exit code ' + str(result.returncode)
        raise CheckError('Git ' + args[0] + ' failed: ' + detail)
    return result


def read_checkpoint(path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise CheckError('Cannot read checkpoint: ' + str(exc)) from exc
    if not isinstance(data, dict):
        raise CheckError('Invalid checkpoint: expected a JSON object')
    if type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise CheckError('Invalid checkpoint: schema_version must be 1')
    if data.get('repository') != REPOSITORY:
        raise CheckError('Invalid checkpoint: repository must be ' + REPOSITORY)
    snapshot = data.get('snapshot')
    if not isinstance(snapshot, str) or not re.fullmatch(r'[0-9a-f]{40}', snapshot):
        raise CheckError('Invalid checkpoint: snapshot must be a full lowercase commit SHA')
    reviewed_at = data.get('reviewed_at')
    try:
        if not isinstance(reviewed_at, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', reviewed_at):
            raise ValueError('expected YYYY-MM-DD')
        date.fromisoformat(reviewed_at)
    except ValueError as exc:
        raise CheckError('Invalid checkpoint: reviewed_at must be a valid YYYY-MM-DD date') from exc
    return data


def resolve(repo, ref, label):
    result = git(repo, 'rev-parse', '--verify', ref + '^{commit}', check=False)
    if result.returncode:
        raise CheckError(label + ' is missing or is not a commit: ' + ref)
    return result.stdout.strip()


def has_commit(repo, sha):
    return git(repo, 'cat-file', '-e', sha + '^{commit}', check=False).returncode == 0


def is_ancestor(repo, base, head):
    result = git(repo, 'merge-base', '--is-ancestor', base, head, check=False)
    if result.returncode not in (0, 1):
        raise CheckError('Cannot establish snapshot ancestry: ' + result.stderr.strip())
    return result.returncode == 0


def is_shallow(repo):
    return git(repo, 'rev-parse', '--is-shallow-repository').stdout.strip() == 'true'


def reject_partial_local(repo):
    # A lazy object fetch could write into a supplied repo. Require a complete
    # local clone even on Git versions that predate GIT_NO_LAZY_FETCH.
    legacy = git(repo, 'config', '--get', 'extensions.partialClone', check=False)
    promisors = git(repo, 'config', '--type=bool', '--get-regexp',
                    r'remote\..*\.promisor', check=False)
    if legacy.returncode not in (0, 1) or promisors.returncode not in (0, 1):
        raise CheckError('Cannot inspect local upstream partial-clone configuration')
    if legacy.returncode == 0 or any(line.endswith(' true') for line in promisors.stdout.splitlines()):
        raise CheckError('Local upstream repository is partial; provide a complete clone')


def range_is_complete(repo, base, head):
    if base == head or not is_shallow(repo):
        return True
    # Every truncated history boundary must be excluded by base..head. Merely
    # finding base on one parent chain is insufficient for a merged branch.
    shallow_path = Path(git(repo, 'rev-parse', '--git-path', 'shallow').stdout.strip())
    if not shallow_path.is_absolute():
        shallow_path = repo / shallow_path
    try:
        boundaries = shallow_path.read_text(encoding='ascii').splitlines()
    except (OSError, UnicodeError) as exc:
        raise CheckError('Cannot inspect shallow history: ' + str(exc)) from exc
    return bool(boundaries) and all(is_ancestor(repo, sha, base) for sha in boundaries)


def fetch_upstream(repo, branch, base):
    git(repo, 'init', '--bare', '--quiet')
    git(repo, 'remote', 'add', 'origin', UPSTREAM_URL)
    target = 'refs/heads/checked-upstream'
    git(repo, 'fetch', '--quiet', '--no-tags', '--filter=blob:none', '--depth=128',
        'origin', branch + ':' + target)
    head = resolve(repo, target, 'Upstream ref')
    deepen = 128
    while True:
        base_available = has_commit(repo, base)
        if base_available and is_ancestor(repo, base, head) and range_is_complete(repo, base, head):
            return head
        if not is_shallow(repo):
            if not base_available:
                # Distinguish an unavailable checkpoint from a rewritten branch.
                fetched = git(repo, 'fetch', '--quiet', '--no-tags', '--filter=blob:none',
                              '--depth=1', 'origin', base, check=False)
                if fetched.returncode or not has_commit(repo, base):
                    raise CheckError('Reviewed snapshot is unavailable from upstream: ' + base)
            raise CheckError('Reviewed snapshot is not an ancestor of upstream head; '
                             'history has diverged or the selected branch is behind')
        # Pin the initial head so an upstream push during the check cannot change
        # the comparison. No blobs or working tree are needed for names/logs.
        git(repo, 'fetch', '--quiet', '--no-tags', '--filter=blob:none',
            '--deepen=' + str(deepen), 'origin', head)
        deepen = min(deepen * 2, 8192)


def make_report(repo, checkpoint, head):
    base = resolve(repo, checkpoint['snapshot'], 'Reviewed snapshot')
    if not is_ancestor(repo, base, head):
        raise CheckError('Reviewed snapshot is not an ancestor of upstream head; '
                         'history has diverged or the selected branch is behind')
    commit_fields = git(repo, 'log', '--reverse', '--topo-order', '--encoding=UTF-8',
                        '--format=%H%x00%s', '-z', base + '..' + head).stdout.split('\0')
    if commit_fields[-1] == '':
        commit_fields.pop()
    if len(commit_fields) % 2:
        raise CheckError('Cannot parse complete upstream commit list')
    commits = [{'sha': commit_fields[index], 'subject': commit_fields[index + 1]}
               for index in range(0, len(commit_fields), 2)]
    # Disabling rename detection avoids downloading blobs. Renames appear as
    # the deleted old path and added new path; this is a net tree comparison.
    names = git(repo, 'diff', '--no-ext-diff', '--no-textconv', '--no-renames',
                '--name-only', '-z', base, head, '--').stdout.split('\0')
    changed_files = names[:-1] if names[-1] == '' else names
    return {
        'schema_version': 1,
        'repository': checkpoint['repository'],
        'reviewed_at': checkpoint['reviewed_at'],
        'base': base,
        'head': head,
        'status': 'up_to_date' if base == head else 'review_required',
        'commit_count': len(commits),
        'commits': commits,
        'changed_file_count': len(changed_files),
        'changed_files': changed_files,
        'compare_url': 'https://github.com/' + REPOSITORY + '/compare/' + base + '...' + head,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
        epilog='Changed files are net paths between base and head, with renames counted as '
               'old and new paths. A review_required result never means skills were updated.')
    parser.add_argument('--checkpoint', type=Path, default=ROOT / 'knowledge/algorithm-updates.json',
                        help='reviewed checkpoint JSON (default: knowledge/algorithm-updates.json)')
    parser.add_argument('--upstream', type=Path,
                        help='existing complete local Git repository; do not fetch or modify it '
                             '(default: temporary public GitHub fetch, no credentials needed)')
    parser.add_argument('--ref', default='main', metavar='BRANCH',
                        help='branch name, resolved as refs/heads/BRANCH locally and remotely '
                             '(default: main; not origin/main or an arbitrary revision)')
    args = parser.parse_args(argv)
    try:
        checkpoint = read_checkpoint(args.checkpoint)
        branch = 'refs/heads/' + args.ref
        if git(ROOT, 'check-ref-format', branch, check=False).returncode:
            raise CheckError('Invalid branch ref: ' + args.ref)
        if args.upstream is not None:
            repo = args.upstream.resolve()
            if not repo.is_dir():
                raise CheckError('Local upstream repository does not exist: ' + str(repo))
            if is_shallow(repo):
                raise CheckError('Local upstream repository is shallow; provide complete history')
            reject_partial_local(repo)
            head = resolve(repo, branch, 'Upstream ref')
            report = make_report(repo, checkpoint, head)
        else:
            with tempfile.TemporaryDirectory(prefix='for-you-upstream-') as directory:
                repo = Path(directory)
                head = fetch_upstream(repo, branch, checkpoint['snapshot'])
                report = make_report(repo, checkpoint, head)
        print(json.dumps(report, ensure_ascii=True, indent=2))
        return 0
    except CheckError as exc:
        print('Upstream check failed: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
