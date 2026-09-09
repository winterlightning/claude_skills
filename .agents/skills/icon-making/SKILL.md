---
name: icon-making
description: Inspect a Pictographic icon request or reference, decide solo/sub/container routing, and run the appropriate icon skill. Use as the entry point for making icons, applying review feedback, or processing Pending briefs. Detect container and side combinations and split them into standalone component briefs rather than authoring a combined primitive. Generated from .claude/skills/icon-making/SKILL.md by icon_set/scripts/generate_skills.py; edit the source, not this copy.
---

# $icon-making — reference triage and family routing

Use the user's request as the brief, including any supplied icon ID, reference paths, and output directory.

Resolve repository paths and run commands from the `claude_skills` directory containing `icon_set/` (three levels above this skill folder). In Codex, invoke these skills with `$icon-brief`, `$icon-sub`, `$icon-solo`, or `$icon-container`; in ChatGPT, select the skill with `@`. Treat slash-style handoffs in generated briefs as references to the corresponding skill.

Run from the repository containing `icon_set/`. This skill selects and invokes
one of `$icon-solo`, `$icon-sub`, `$icon-container`, or `$icon-brief`; it does not
replace their geometry and validation instructions. Inspect the corresponding
skill file before authoring. Their sources are in `.claude/skills/`; Codex copies
are in `.agents/skills/` and portable copies in `skills/`.

## Inspect and classify before authoring

Render and visually inspect a supplied SVG, or view a supplied PNG. Names and
SVG markup alone are not evidence of the subject. The existing
`icon_set/scripts/prepare_references.py` produces reference renders. For a text
request with no image, classify the described subject without inventing an image.

Preserve a family explicitly supplied by the user or an existing Python icon.
Otherwise this router is authorized to decide it:

| Intended subject | Route |
|---|---|
| One independently recognizable noun/object, tool, person, animal, or scene reduced to a single subject | `$icon-solo` (48×48) |
| Small operator, arrow, state, modifier, or simple glyph intended to accompany another icon | `$icon-sub` (32×32) |
| A standalone enclosure, frame, screen, card, window, or speech bubble | `$icon-container` (64×64) |

Use function and meaning, not the source image's dimensions. Explain the chosen
family in one sentence. A simple noun glyph can be `sub`; a screen with its own
structural controls can be a standalone `container`. If the user's specified
family conflicts with a combined reference, split it through the workflow below
instead of silently reclassifying the whole reference.

## Reject combined references as single primitives

Follow `icon_set/skills/icon-design/reference-triage.md` before invoking an
individual authoring skill. Two disallowed primitive candidates are:

- **Container combination:** an independently meaningful icon hosted inside a
  distinct enclosure. Example: a folder/badge containing a separate check mark.
  Queue the enclosure as `container` and the inner glyph as `sub`.
- **Side combination:** an independently meaningful noun/enclosure plus a
  separate action/state icon beside it. Example: a document with an adjacent
  plus. Queue the main subject as `solo` (or `container` when it is an enclosure)
  and the modifier as `sub`. Do not implement a SIDE_COMBINE renderer here;
  its composition slots are not frozen in the current contract.

A handle, lid, screen button, clothing detail, or natural body part is not a
second icon just because it is a separate shape. Reject only when both parts
have independent icon meanings. An empty container is a valid primitive.

Name and describe exactly two standalone components. Preserve the full
reference path/UUID and explain which component each brief isolates. Do not
create the combined icon or an edited variant of the combination. Keep existing
Python files and exports for historical comparison.

If reviewing a built icon, use **Reject — combined primitive** in its inspector;
enter the combination type and the two named component briefs. This removes the
combined icon from approved results and adds two entries to **Pending briefs**.

For a source reference before generation, save a JSON object under
`work/pending-brief/` and queue it using:

```bash
python3 icon_set/scripts/queue_brief.py --file work/pending-brief/split.json
```

Example JSON shape (replace values with visually established components):

```json
{
  "reference_path": "pictographic-primitives/category/source_UUID.svg",
  "combination_type": "container",
  "reason": "Separate enclosure and hosted status glyph.",
  "components": [
    {"name": "Document frame", "family": "container", "description": "The document enclosure alone, excluding the check mark."},
    {"name": "Check mark", "family": "sub", "description": "The check mark alone, excluding the surrounding document."}
  ]
}
```

The queue helper also copies the full source and saves `brief.md`/`brief.json`
under `work/pending-brief/<component-family>/<reference-and-revision>/` for each
component. `icon-brief` uses the same helper after its own visual detection.
Use `--files-only` to prepare handoffs without a database write.

Use `combination_type: "side"` for side combinations. Supply optional `icon`
with the exact `family$icon-id` when rejecting a built icon already linked to
this reference; the CLI verifies that relationship. Use `--database` when the
review server uses a different persistent database. A repeated identical source
revision does not duplicate its briefs. Keep the JSON handoff if the server's
remote database cannot be reached; do not claim it was queued remotely.

Stop after queuing a rejected combined reference unless the user also requested
generating its components. When processing **one Pending brief**, inspect the
full original but isolate only the named component; do not enqueue the same
whole-reference split again. Use the brief's explicit family and search for a
reusable standalone icon before creating another. After a successful build,
link the generated `family$icon-id` with **Mark generated** in Pending briefs.
This completes the brief without approving the component automatically.

## Route and finish

For standalone references, hand the name, chosen family, source path/UUID, and
focused description to the matching family skill. For a batch needing briefs,
invoke `$icon-brief` with an explicit family per standalone item/group; split
combined references out first. The brief writer receives your family decision
and does not need to guess it again.

For feedback on an existing standalone icon, preserve the old version. Use
`icon_set/scripts/create_variant.py` to allocate a new variant file/ID, then
invoke the same family skill to edit only that new file. Preserve parent links,
source identity, and family rules. Do not patch the parent in place.

Validate and build the chosen family with `icon_set/scripts/build.py --family`
and its family argument. Inspect the generated output at native size and report
file path, ID, family, validation, and any remaining limitation. Leave human
approval to the reviewer. Queueing a split alone does not require a build and
must not be reported as generated output.
