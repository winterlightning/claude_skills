---
name: generate
description: Entry skill for a symbol-library generation pack (manifest kind "generate"). Read one batch, read each symbol's icon_type.txt, decide normal versus container for every normal symbol, and route each symbol to the sub-icons, icons, or container-icons skill.
---

# Generate a symbol batch

This is the common entry point for a downloaded generation pack such as
`Business-Products-generation-2026-09-03/batch-NN/`. It does not draw anything
itself. It reads the batch, fixes the icon type of every symbol, and hands each
symbol to the type skill that owns its profile:

| `icon_type.txt` | Skill | Built-in profile |
| --- | --- | --- |
| `sub` | [sub-icons/SKILL.md](sub-icons/SKILL.md) | 32×32px, 4px stroke |
| `normal` → agent verdict `normal` | [icons/SKILL.md](icons/SKILL.md) | 48×48px, 4px stroke |
| `normal` → agent verdict `container`, or `container` | [container-icons/SKILL.md](container-icons/SKILL.md) | 64×64px, 4px stroke, 32×32 protected slot |

Exact canvas, stroke, keyshape, and slot values come from
`core/icon_profiles.json`; the sizes above are the built-in defaults.

## Scope and inputs

Work on one explicitly selected `batch-NN` folder (or several named folders).
Read, in this order:

1. The pack root `README.md` and the batch `README.md`, for what the pack is.
2. `GENERATION-PROMPTS.md`: the renamed symbol name and `minimal_description`
   for every symbol, plus the prototype and output paths.
3. `manifest.json`: `kind`, `api.label`, and per symbol `sid`, `name`,
   `minimal_description`, `n_icons`, `instances`, `files.prototype`, `upload`.
4. Per symbol folder `sym_XXXXXX/`: `description.txt`,
   `<sid>_prototype.svg`, and `icon_type.txt`.

The brief is `name` + `minimal_description`. `icons[]` lists downstream
icons that use the symbol; it is context for the container decision, never a
feature list. The prototype is a 26u foreign-grid drawing (24u art box, 1u
margin, 1.5 stroke): use it for subject, part count, and arrangement, never
for canvas, stroke, or exact proportion. Apply the shared
[extracted-prototype rule](shared/icon-rules.md#extracted-prototypes-restore-missing-geometry).

Keep every pack input unchanged: prototypes, descriptions, manifest, pack
README, `GENERATION-PROMPTS.md`, and `upload.py`. The manifest `upload` path
(`sym_XXXXXX/sym_XXXXXX_generated.svg`) is the local delivery destination.
It is never authorization to run `upload.py`; uploading needs a separate,
explicit instruction.

## Step 1 — make sure every symbol has `icon_type.txt`

`icon_type.txt` is the skill picker. It holds one word: `sub`, `normal`, or
`container`. The size classifier writes `sub` or `normal` from the painted
bounding box of the prototype (longest side ≤ 12u, half the 24u art box, is
`sub`). If any symbol folder lacks the file, run from the repository root:

```bash
python3 core/classify_icon_type.py <pack-or-batch-folder>
python3 core/classify_icon_type.py <batch-folder> --dry-run --json   # preview only
```

The classifier never writes `container` and preserves an existing
`container` verdict. Do not pass `--overwrite` unless the user asks to discard
earlier review decisions. To see the raw measurement behind a verdict:

```bash
python3 core/bbox_zones.py <batch>/sym_XXXXXX/sym_XXXXXX_prototype.svg
```

## Step 2 — route each symbol

Read `icon_type.txt` for every symbol and build the batch routing table before
composing anything.

### `sub`

Route directly to the [sub-icons skill](sub-icons/SKILL.md). The symbol is a
small part of larger icons (dots, dashes, small marks, tiny rings) and is
recomposed to fill the sub canvas as an independently recognizable symbol.

### `normal` — decide normal or container

The classifier cannot tell an outer frame from a full-size figure. For every
`normal` symbol, look at the rendered prototype, the brief, and the manifest
usage counts, and give one verdict:

**Container** when all of these hold:

- The prototype is an outer or enclosing form (outline, frame, bubble,
  window, badge, ring, shield, document edge, screen) whose interior is empty
  or carries only edge detail.
- It stays recognizable when a centered square half its size is kept
  completely clear, because the container profile protects a 32×32 slot
  inside its 64×64 canvas.
- The brief describes the enclosure itself and nothing inside it
  ("Single circle outline", "Rectangular speech bubble", "Browser window").
- Usage supports it: a high `n_icons` / `instances` count means many icons
  place other symbols inside this one (Circle Outline is used by 724 icons).

**Normal** otherwise: figures, arrows, objects whose identity-bearing detail
crosses the center (envelope flap, magnifying-glass handle across the lens,
delivery van, standing person), or any enclosure that would lose recognition
with its center cleared.

Record every verdict with a one-line reason in `batch-notes.md`. When the
verdict is `container`, write `container` into that symbol's `icon_type.txt`
so the picker is stable on re-runs (the classifier preserves it). Leave
`normal` files unchanged. If a `container` verdict later proves impossible
(the slot cannot be kept clear without losing the subject), downgrade it to
`normal`, rewrite `icon_type.txt`, and record why.

### `container`

A symbol already marked `container` by an earlier review routes directly to
the [container-icons skill](container-icons/SKILL.md).

## Step 3 — execute each symbol with its skill

Load the selected skill, its `rules.md`, and its generated `profile.md`; then
follow the [shared pipeline](shared/icon-pipeline.md). Declare `iconType` in
every editable source to match the routing table. Never mix profiles in one
QA invocation or one contact sheet.

**Sub and normal symbols** use the
[local manifest pack lane](icons/rework.md#local-manifest-pack-lane). The pack
builder accepts this pack's `<sid>_generated.svg` delivery name:

```bash
python3 core/rework_pack.py inspect <batch-folder>
python3 core/rework_pack.py prepare <batch-folder>
# author <batch-folder>/editable/<kebab-case-name>.json per symbol,
# with sourceAnalysis.symbolId = sid and iconType from the routing table
python3 core/rework_pack.py build <batch-folder>
```

`build` emits the native SVG and its same-size design alias, runs the mandatory
native canvas/keyshape gate on both alongside the other profile-aware QA gates,
checks the hash-locked visual review, and copies each passing SVG to its manifest
`upload` path. It processes the whole manifest, so containers in the same
batch must have their editable sources present too; the builder does not
deliver a container without separate filled-preview evidence.

**Container symbols** use the manual profile-aware pipeline from the
container skill: emit with `core/emit_icon.py`, run the structural, grid,
overlap, keyshape, and hole/pinch gates with `--icon-type container`, author
the accepted sub icon and compose the filled preview with
`core/compose_container_preview.py`, review at native size, then copy the
passing empty container SVG to that symbol's manifest `upload` path.

## Step 4 — verify every generated output and repair failures

Follow the [mandatory canvas/keyshape gate](shared/icon-pipeline.md#9-validate-the-declared-painted-keyshape)
for every symbol; a plausible-looking preview or a correct viewBox alone is not
acceptance. The gate checks the configured native output dimensions and stroke
against the editable source's declared keyshape, including stroke overflow and
container-slot protection. It does not replace the other pipeline gates.

After copying to a manifest delivery name, verify that actual file with the
explicit editable mapping because `<sid>_generated.svg` differs from the editable
name:

```bash
python3 core/validate_icon_keyshapes.py \
  <batch-folder>/sym_XXXXXX/sym_XXXXXX_generated.svg \
  --editable <batch-folder>/editable/<kebab-case-name>.json \
  --output-dir <batch-folder>/qa/<sid>/delivery-keyshape
```

Require a successful exit and a fresh passing report for every expected delivery.
If any result fails, repair the editable geometry, regenerate both canonical and
design SVGs, rerun all affected structural/grid/spacing/keyshape/hole/visual gates,
and replace the delivery only after it passes. Do not change the profile, token,
optical-fit mode, or validator thresholds merely to make the result pass. Missing,
stale, or failed outputs block completion; report genuinely blocked symbols and
continue safe work on the others. Numeric success is not native-size visual
approval and never authorizes uploading.

## Delivery

Per batch, deliver `batch-notes.md` with:

- batch ID and the exact symbol list;
- per symbol: `icon_type.txt` value, the normal/container verdict and reason,
  the editable source name, and gate results including the fresh native
  canvas/keyshape report for the actual delivery;
- blocked or omitted symbols with the stopping step and reason;
- one native-size contact sheet per profile present in the batch.

Deliver each symbol's editable JSON, native SVG, QA evidence, and the
`<sid>_generated.svg` file at the manifest path. Do not run `upload.py`.
End after the selected batch; do not open the next batch automatically.

## Stop conditions

Stop the affected symbol and report it when:

- `icon_type.txt` is missing and the classifier cannot measure the prototype;
- the prototype, `description.txt`, and manifest entry disagree on the symbol;
- two symbols resolve to the same editable name;
- a `container` verdict cannot keep the protected slot clear and the
  downgrade to `normal` would change the subject;
- the brief is too vague to enumerate required features;
- the user's decision would change the subject or the icon type.

Continue safe work on the other symbols and list every real omission.
