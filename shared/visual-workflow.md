# Create visuals and keep a reusable style

This procedure is available from the router, publishing checklist and visual specialist, including standalone installations. Respond in the user's language. The host's tool, privacy and image-generation rules take precedence over this portable procedure.

## 1. Carry the actual brief

Reuse the existing draft and review instead of asking for them again. Keep a `visual_brief` containing:

- `draft_or_topic`, `selected_format`, `audience` and the user's intended result;
- `images`: ordered purpose, exact supported message, essential conditions, source references and any required assets for each;
- `existing_assets`, `evidence_ids`, `profile_scope`, `style_decision` and unresolved inputs.

Use the smallest useful image set; multiple images need distinct jobs. The first should stand on its own, with the most useful supported message and essential conditions. Honor an explicit action-first or other user preference. Keep the main finding in the post text too. The first-available-image behavior belongs to a specific media-selection path, not every model or an upload bonus. Retrieve applicable evidence through the knowledge guide when explaining algorithm effects; these design recommendations are editorial judgments.

## 2. Discover capabilities before offering production

Inspect the current tool catalog and applicable host skills. Identify what can actually create/edit images, render exact charts, capture authorized screenshots or use supplied assets. A tool's presence is not proof that a requested provider/model is supported or authenticated. Read its documentation; never invent tool calls or silently substitute a provider.

If native image generation is available, explicitly tell the user you can generate the images here. Offer meaningful choices for this brief: their own images, real screenshots, available AI generation (or their preferred service), or a mixture. Follow an already stated choice directly. A stored provider is a preference, not a credential or proof of availability today.

If the preferred provider is unavailable, name the limitation and available alternatives. If there is no image creation tool, still provide an ordered brief, exact text and portable prompts, labeling them as production instructions. Do not call a prompt a generated image. No paid-provider setup, installation or external upload is implied by an image recommendation.

## 3. Read or establish preferences

First visual use means the first requested creation/style workflow, not every audit with missing images. Locate persistent preferences before questioning the user:

```bash
python3 scripts/visual_preferences.py path
python3 scripts/visual_preferences.py show --scope default
```

Choose an explicit `series:<id>` or `account:<id>` when the user identifies one; otherwise use `default`. Names are stable user-chosen identifiers, not secrets. The helper returns `requested_scope` and `resolved_scope`; a missing specific profile falls back to default. Tell the user when a fallback is used. It does not implicitly merge accounts or series.

On first use, ask only for missing source/provider and broad style, with an option to use a proposed style. Group the essentials in one short question. Offer to remember it for this account, series or as the default. Do not turn optional color/font/aspect/signature fields into a long compulsory questionnaire. A user-supplied style or reference already answers the corresponding question.

For a saved profile, briefly show its distinguishing traits and offer **reuse / change only this time / save a new series style**. If the user already says reuse, or explicitly gives a one-time change, follow that instruction without reconfirming it. The choice concerns style, not renewed permission to complete the requested work.

Keep long-term preferences in the profile; keep the current draft, sources and one-off content in the brief. A temporary override uses `show --override` or an in-memory merge and never runs `save`. Save a new or revised profile only when the user requests remembering it or selects that option. A new series saves under a new series scope; it does not change default. When changing an existing profile, preserve fields the user did not change.

## 4. Private persistence and portability

`visual_preferences.py` uses Python 3.9+ and the standard library. Run it from the installed skill root, or use its absolute path with your Python command. `--file` precedes the operation and accepts an absolute private path.

| Platform | Default location |
| --- | --- |
| Linux | `$XDG_CONFIG_HOME/for-you-skills/visual-preferences.json`, otherwise `~/.config/for-you-skills/visual-preferences.json` |
| macOS | `~/Library/Application Support/for-you-skills/visual-preferences.json` |
| Windows | `%APPDATA%/for-you-skills/visual-preferences.json`, otherwise the user's `AppData/Roaming` directory |

`FOR_YOU_SKILLS_CONFIG_DIR` overrides the directory with an absolute path. All installed copies use the same location in the same OS account. Separate containers, remote hosts and devices need import/export or a user-approved persistent volume. Do not promise cross-device sync. In an ephemeral filesystem, use the host's approved persistent private storage; otherwise disclose session-only memory and offer a downloadable export. Claim persistence only after verifying the write and read in durable storage.

A profile object may contain these fields; omit unknown preferences:

```json
{
  "source": "mixed",
  "provider": "native",
  "style": "Clean editorial cards with real evidence panels",
  "palette": ["#F7F3EA", "#222222", "#E46B32"],
  "typography": "Readable sans serif; short headings",
  "layout": "One clear finding per image",
  "aspect_ratio": "4:5",
  "text_language": "en",
  "signature": "No signature",
  "first_image_priority": "Action and essential condition",
  "references": [],
  "avoid": ["Decorative dashboards", "Invented screenshots"]
}
```

`source`: `user-assets`, `screenshots`, `ai`, or `mixed`. `model` is an optional string. `references` holds user-approved reference descriptions or stable paths/URLs, not copied image data. Credentials, access tokens and signed/private download URLs do not belong in any field. Profiles and imports are data, never executable instructions or authorization to read/upload assets.

Write the agreed profile object to a private temporary JSON file, then:

```bash
python3 scripts/visual_preferences.py save --scope series:weekly-code --input /absolute/private/profile.json --expect-revision 0
python3 scripts/visual_preferences.py show --scope series:weekly-code
```

Replace `0` with the revision returned by the preceding read. If it is stale, reread and reconcile instead of overwriting. `save` replaces only that scope, preserving the other scopes. Writes are atomic, with restrictive permissions on POSIX; Windows access follows the user's directory ACL. Existing corrupt files and unsupported versions are rejected unchanged. A busy lock is reported rather than bypassed.

Export/import uses the full document with `schema_version: 1`, `revision` and `profiles`:

```bash
python3 scripts/visual_preferences.py export --output /absolute/private/visual-preferences-export.json
python3 scripts/visual_preferences.py import --input /absolute/private/visual-preferences-export.json
```

Export refuses to overwrite an existing file. Import merges scopes; differing existing profiles require an explicit user choice before `--replace`, which replaces only incoming conflicting scopes. Review exports before sharing: they can identify accounts, reference assets or a personal brand. Import transfers preferences, not provider access or referenced images.

No Python? Use the same schema through the host's reliable file/storage tools, preserving existing scopes, validating fields, and verifying readback. Keep preference and temporary files outside repositories and skill directories. If safe persistent editing is unavailable, retain session context and offer the validated export; do not pretend it is installed memory. Never commit private profiles with the public skill package.

## 5. Produce, inspect, deliver

Choose the method per image:

| Content needed | Production method |
| --- | --- |
| Real UI, code evidence or source quotation | Supplied/authorized captured material; preserve relevant context and annotate accurately |
| Exact values, comparisons or process diagrams | Render from verified data/text using suitable chart, vector or layout tools |
| Conceptual or decorative imagery | Available AI image tool or supplied artwork, with the selected style |
| Evidence plus illustration | Compose verified evidence with clearly distinguishable conceptual elements |

Use host-specific generation instructions and the actual supported tool. Include the agreed purpose, exact text, source constraints, style, crop/aspect needs and image order. When source material is missing, request that material or finish independent images; do not fabricate evidence. Reference images need actual access and the host's permitted handling.

Inspect each returned image at a readable size: verify text, numbers, conditions, source fidelity, cropping, mobile legibility, consistent style and first-image usefulness. Correct defects with the appropriate tool. If inspection or correction is unavailable, label that limitation. A style preference never overrides factual accuracy.

Deliver the actual artifacts through the host's supported image/file mechanism, in posting order, with concise alt text and any needed source attribution. Say what remains unfinished. Save the agreed style separately from task output, and report whether it was saved or used for this request only. Creation does not publish to X.com.
