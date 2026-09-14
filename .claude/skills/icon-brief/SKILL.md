---
name: icon-brief
description: Turn reference SVGs into authoring briefs for the Pictographic icon set. Use when given a folder or file of source SVGs to prepare, triage or catalogue before drawing — renders each one, then writes its name, icon_id, family, description and tags into a brief that /icon-sub, /icon-solo, /icon-avatar or /icon-container can be run against. Detect side combinations and copy flagged or uncertain references into a human-review folder; distinguish modifiers from natural multi-object subjects. Save container component briefs for later authoring. The requested family applies to standalone icons; split components use their individual families. Hand-authored; edit this file directly.
argument-hint: <svg folder or file> <sub|solo|container|avatar> [--out <dir>]
---

# /icon-brief — reference SVGs in, authoring briefs out

Request: $ARGUMENTS

A brief says **what the reference is**. It does not say how to draw it. You
identify and name the subject; the family skill that authors it decides what
survives at native size, what the keyshape is, and where every coordinate goes.
Keep that line and the briefs stay useful for years.

**The family comes with the request, not from you.** The requester names the
icon type — `sub`, `solo`, `container` or `avatar` — and standalone briefs carry
it. Combined references use the separate component-family routing below. See [Family](#family) before writing anything.

Before writing a standalone brief, visually classify the reference using
`icon_set/skills/icon-design/reference-triage.md`. Do this within `icon-brief`;
do not defer detection until authoring. Hold side combinations and uncertain
cases for human review; save split handoffs for clear container combinations
as described below. This brief-only review hold takes precedence over the
shared triage guide's immediate splitting step.
When invoked by `/icon-making`, its chosen family is an explicit input.

## Detect combinations and save them for later

After opening each reference render, classify it as **standalone**,
**container combination**, **side combination**, or **uncertain**. Read the
side-combination decision criteria and examples in
`icon_set/skills/icon-design/reference-triage.md`. Never classify from the
filename, number of objects, SVG groups, or position alone.

- Container combination: a separate glyph inside an enclosure. Write two briefs:
  the empty/standalone enclosure in `container/`, and its isolated content in `sub/`.
- Side combination: a main subject with a separate adjacent or overlapping
  action/state modifier. Mark and copy the complete reference for human review
  using the procedure below. Do not split or queue components yet.
- Uncertain: the render does not clearly establish whether the second element
  is a modifier or part of the subject. Save it for human review with the
  competing interpretations; do not force a combination label.
- Standalone: continue the ordinary five-field brief in the requested family.
  A coherent subject may contain two or more objects.

### Hold side combinations for human review

Save every side combination and uncertain reference under
`work/combination-review/side/<source-stem>-<digest>/` or
`work/combination-review/uncertain/<source-stem>-<digest>/`, respectively.
If the user supplies an output directory, put `combination-review/` there.
Use a digest of the full source path and source bytes to distinguish references
with the same filename and different revisions. Retain the full filename and
UUID inside the folder. Copy the original SVG (or supplied PNG) byte for byte;
do not move, crop, redraw, or modify the source. Include the inspected preview
when available and a `review.json` like this:

```json
{
  "reference_path": "pictographic-primitives/category/source_UUID.svg",
  "classification": "side_combination",
  "review_status": "pending_human_review",
  "requested_family": "solo",
  "main_subject": "Cloud",
  "modifier": "Check mark",
  "modifier_position": "bottom-left, overlapping the cloud outline",
  "reason": "The cloud is independently recognizable; the detached check acts as a status badge rather than a physical part of the cloud.",
  "uncertainty": null
}
```

For an uncertain case use `classification: "uncertain"`, describe both plausible
readings in `uncertainty`, and use `null` for any component or position you cannot
identify. The reason must cite visible evidence, including why the smaller
object acts as a modifier rather than belonging to a natural scene. Record each
reference's classification and review-folder path (when flagged) in the run's
`triage.json` beside its preview index; keep these review fields out of the
standalone five-field brief.

Verify the copy's bytes match the source. Reuse an identical review bundle;
never overwrite human edits. Keep held references out of the standalone manifest
and authoring handoff, and do not queue them in Pending briefs. Continue briefing
the clear standalone references. Human review can later confirm a side split
(main subject in `solo/` or `container/`, modifier in `sub/`) or return a reference
to standalone briefing. Do not turn a solo subject into a container to fit a
folder name.

### Save clear container splits (or human-confirmed side splits)

For these combinations, do not produce one normal authoring brief for the whole
reference. Write a split JSON handoff with `reference_path`, `combination_type`
(`container` or `side`), a visual `reason`, and exactly two `components`. Each
component has `name`, `family`, and `description`; include `icon_id` and `tags`
when known. Descriptions say what to generate and which other component to
exclude. Preserve the complete supplied source path and UUID. If the reference
cannot be unambiguously separated into two components, hold it as uncertain
instead of inventing a two-part split.

```json
{
  "reference_path": "pictographic-primitives/category/source_UUID.svg",
  "combination_type": "container",
  "reason": "A separate check mark inside a document enclosure.",
  "components": [
    {"name": "Document frame", "family": "container", "description": "The document enclosure alone. Exclude the check mark."},
    {"name": "Check mark", "family": "sub", "description": "The check mark alone. Exclude the document."}
  ]
}
```

Save each split JSON under `work/pending-brief/requests/` with a unique source-based
filename, then run:

```bash
python3 icon_set/scripts/queue_brief.py --file work/pending-brief/requests/split.json
```

This copies the unchanged full SVG (or PNG when that is the supplied reference)
into **each component's folder**, with `brief.md` and `brief.json` beside it:

```text
work/pending-brief/
  container/<reference-and-revision>/
    <original-source-filename>.svg
    brief.md
    brief.json
  sub/<reference-and-revision>/
    <original-source-filename>.svg
    brief.md
    brief.json
```

Side combinations may also create `solo/<reference-and-revision>/`. The actual
source filename and bytes are retained; the copied file is the full reference,
not a generated or cropped component. The brief explains which part to isolate.
The helper includes a source/revision digest in the folder name to avoid
collisions, reuses an identical handoff, and refuses to overwrite modified work.

By default it also adds the two components to the review app's Pending briefs.
Use `--files-only` when only preparing files for later work; use `--out` to choose
another handoff root, and `--database` if the review app uses a different database.
If queueing fails after saving files, report the saved paths and the queue error
rather than claiming the items appeared in the app.

Check that each saved source copy matches the original and both briefs name
their family and excluded component. Report standalone, container-split, side-review, and uncertain-review counts
and the saved folders. Do not generate either component during a brief-only task.

Per standalone icon you produce exactly five fields:

| Field | What it is |
|---|---|
| `concept` | Title-case noun phrase, the brief's heading — `Sailing Boat with Single Sail` |
| `icon_id` | Proposed kebab-case id for the authored icon — `sailboat` |
| `family` | The family named in the request. Copied, never decided. Routes to `/icon-<family>` and sets the native render size |
| `description` | 1–2 short sentences: silhouette, how the parts attach, the one interior mark that carries the meaning |
| `tags` | 6–10 lowercase search terms |

## Design handoff

Keep the complete source filename/path and its supplied ID in every brief and
handoff, even when proposing a shorter descriptive `icon_id`. A trailing UUID
belongs to the reference identity and must not be discarded. The authoring
skill must carry it into the Python filename and `SOURCE_ICON_ID`, with the
source path in `SOURCE_PATH` and its own model in `AUTHOR`, as specified in
`icon_set/skills/icon-design/naming.md`. Preserve the source/render/native path
lines when editing generated briefs; those paths retain the original identity.

All icon-family agents prioritize Lucide-style geometric construction, smooth
curves, and optional symmetry and balance where they preserve the subject’s
meaning and natural shape. Skip either when it would weaken recognizability. Keep briefs faithful to the
reference: describe visible symmetry, curve character, and meaningful asymmetry
in the existing description field when they define the subject. Do not invent
symmetry, prescribe coordinates, or replace the reference's identity to match
Lucide. The authoring skill chooses the construction and reviews the result.

## Procedure

0. **Confirm the family.** It is in the request or you ask for it. Everything
   below renders and previews at that family's canvas, so getting it after the
   fact means doing the run twice.

1. **Render first.** Never brief an SVG you have not looked at; its markup tells
   you what coordinates it has, not what it is.

   ```
   python3 icon_set/scripts/prepare_references.py <folder-or-file> \
       --native <32|48|64> --out work/<name>
   ```

   This writes `png/<stem>.png` (320px), `png/<stem>@<native>.png`, a contact
   sheet per 36 icons, `index.html`, `index.md`, and a placeholder brief each.

   Pass `--native` for the requested family — 32 sub, 48 solo (including avatars), 64 container. It
   defaults to **64**, so omitting it on a solo run previews every icon at the
   wrong size and you describe detail the real canvas will not hold.

2. **Look at every render.** Read `sheets/sheet-NN.png` to triage the batch,
   then open each `png/<stem>.png` individually — the sheet is too small to
   describe from. Also open the `@<native>` copy: not to decide what to cut, but
   so your description does not lean on detail that is not actually there.

3. **Triage before writing briefs.** Save side/uncertain review bundles and
   split clear container combinations using the procedure above. Keep all of
   these references out of the standalone authoring handoff. Then **write the standalone manifest** at `<svg folder>/manifest.json` — a JSON array, one
   object per file, `file` matching the SVG filename exactly (including spaces
   and parentheses):

   ```json
   [
    {
     "file": "(pictoicon) - Sailing Boat with Single Sail.svg",
     "icon_id": "sailboat",
     "concept": "Sailing Boat with Single Sail",
     "family": "solo",
     "description": "A small sailboat: a U-shaped hull with a flared, flat-topped gunwale, a vertical mast rising from its centre, and one triangular sail with a curved, bellied leech filling the space to the right of the mast.",
     "tags": ["boat", "sailboat", "sail", "sailing", "ship", "nautical", "travel", "sea"]
    }
   ]
   ```

   `family` holds the requested value and is **identical in every entry** — the
   example says `solo` because that was the request, not because the sailboat
   looks like one. Check it before moving on:

   ```
   python3 -c "import json,sys; m=json.load(open(sys.argv[1])); print(len(m),{e['family'] for e in m})" <folder>/manifest.json
   ```

   One family in that set, or you have inferred something you were not asked to.

   An existing manifest with other keys (`categories`, `id`, …) keeps them; add
   the five fields alongside rather than rewriting the file.

4. **Regenerate only standalone references** against it. The renderer scans
   every SVG in a supplied folder; omitting entries from the manifest does not
   exclude those files. For a mixed batch, run this command once per standalone
   source file with the shared manifest and output directory. Keep the first-pass
   preview index as a triage aid, but move any placeholder briefs for held/split
   references out of the deliverable `briefs/` folder into their review/handoff
   bundles. Do not overwrite existing human edits.

   For a folder containing only standalone references:

   ```
   python3 icon_set/scripts/prepare_references.py <folder-or-file> \
       --manifest <folder>/manifest.json --out work/<name>
   ```

   Each icon now renders at the requested family's native size and its brief
   carries the five fields plus the `/icon-<family>` instruction. A manifest
   sitting next to the SVGs is found automatically; pass `--manifest` when it
   lives elsewhere.

   Regenerating does not remove native renders left from an earlier size. If
   the first pass ran at a different `--native`, delete the stale copies —
   `rm -f work/<name>/png/*@<old>.png` — so nothing points at a preview from
   the wrong canvas. Then check the briefs agree:

   ```
   grep -h "^- family:" work/<name>/briefs/*.md | sort | uniq -c
   grep -h "^- native"  work/<name>/briefs/*.md | sed 's/:.*//' | sort | uniq -c
   ```

   One family, one native size, and the count equal to the number of standalone references.

5. **Report** the standalone, container-split, side-review, and uncertain-review
   counts, the output paths, and any reference you think is wrong
   for the requested family — briefed as asked, flagged for the requester.
   Name the held references and their visual reasons, and link their review
   folders. Hand over the first standalone command to run (if any): `/icon-<family> <icon_id> — <one
   sentence>`.

## Naming

`concept` names the subject as a person would say it, in the reference's own
terms. `icon_id` names the **concept, not the drawing**: lower kebab-case
matching `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`, singular, no family suffix unless the
same concept already exists in another family. Follow an existing prefix family
(`arrow-*`, `chevron-*`, `container-*`) when the icon belongs to one. A supplied
`sym-<id>` stays at the front of the name, complete. Full rules:
`icon_set/skills/icon-design/naming.md`.

Check the id is free before proposing it:

```
python3 -c "import sys; sys.path.insert(0,'.'); from icon_set.model.icons.registry import icons_in; print(sorted(i.icon_id for f in ('sub','solo','container','avatar') for i in icons_in(f)))"
```

If it is taken by the same concept in another family, propose the suffixed form
(`bell-sub`); if it is taken by a different concept, pick another name.

## Family

**For standalone references, the requester names the family and it stays fixed
across that standalone run. Combination detection is the explicit exception:
hold side/uncertain references for review and save confirmed component briefs
in their correct families as described above.**

- `sub` (SUB32) — 32×32. A small glyph, mark, operator, arrow, chevron, state
  or modifier.
- `solo` (SOLO48) — 48×48. One independently readable subject: a device,
  object, tool, garment, vehicle, figure.
- `container` (CONTAINER64) — 64×64. An enclosure that holds something: frame,
  window, screen, card, board, bubble, badge outline.

Read the family off the request — `/icon-brief <folder> solo`, "brief these as
containers", "these are all sub icons". Write that one value into `family` for
every entry in the manifest.

**If the request does not name a family, stop and ask.** One short question
before you render anything. Do not infer it from the filenames, from how
detailed the drawings look, from what the set is short of, or from what the
subjects appear to be. A folder of zodiac glyphs is not automatically `sub`; a
folder of frames is not automatically `container`. Guessing produces a whole
run at the wrong canvas, and the native previews, the brief text and the
`/icon-<family>` handoff are all wrong with it.

Mixed runs happen only when the requester asks for them, and then they say
which files go where. Absent that, one request means one family.

If a reference looks genuinely wrong for the family you were given — a wide
detailed scene asked for at SUB32, an enclosure asked for as `solo` — **brief
it as asked** and say so in your report, naming the file and the reason. That
is the requester's call to reverse, not yours to pre-empt.

## Description

Keep it short — 1–2 sentences, roughly 25–45 words. Describe the drawing in
front of you in order of what carries the identity: overall silhouette, then
the parts and how they attach, then the one or two interior marks without which
the subject stops being itself. Present tense, plain nouns. Name orientation and
stance when they matter (`facing right`, `on a diagonal from lower-left`). Say
what each part *is* — `a horizontal belt across the waist`, not `a rounded rect`.

Short does not mean vague. A long inventory of every rivet and fold is worse
than useless here: the author is going to redraw the subject on a small canvas,
and a description that treats incidental ornament with the same weight as the
identity misleads them about what has to survive. Spend the words on the
identity; sum up the rest in a clause (`fine hatching across the body`).

Do not write: what the icon *means* or when to use it; marketing lines
("signifies a fresh start"); path counts, coordinates, viewBox numbers or
stroke widths from the source.

## Adapt the reference or generate a new icon

Include this guidance in every brief's authoring handoff, outside the subject
description and without adding a sixth brief field:

> You can try modifying a copy of the SVG reference to fit the icon design rules,
> or generate a new icon that matches the icon name. Either approach must follow
> the requested family's design rules and preserve the named subject's identity.

For a split component brief, this choice applies only to the named component;
continue to exclude the other component. Keep the original reference unchanged.
The authoring skill chooses the approach and produces the required deliverables.

Assume every incoming reference is **too thin and too complex for the canvas it
is headed to**. These SVGs are drawn at illustration scale: hairline strokes,
nested detail, ornament that resolves only when the thing is 320px wide. The
authored icon lands on the requested family's grid — 32, 48 or 64 — with the
profile's stroke weight. Detail that fine does not shrink; it turns into mud.

Whether adapting the SVG or drawing anew, bring the result into the profile:
fewer parts where needed, the required stroke weight, adequate gaps, and
geometry fitted to the grid. What must not change is what the
thing *is* — the silhouette a person recognizes it by, the parts that make it
that subject and not a neighbouring one, the stance and orientation that carry
its sense. Simplify the drawing; never simplify away the meaning.

Your job in the brief is to make either approach safe. Name the subject
precisely and describe it so the identity is unmistakable, and the author can
cut freely without cutting the wrong thing. Note in the description when the
reference itself is hard to read — dense hatching, stacked parts, an ambiguous
subject — because that tells the author the drawing has to be rebuilt rather
than followed. What you must not do is make the cuts yourself:

## Do not make reduction decisions

The brief is a description, not a design. Never add to it:

- keep/drop lists, or any "at 48 this disappears" judgement
- "simplify", "reduce to three", "use a single curve instead"
- a proposed keyshape, extreme coordinates, grid or stroke advice
- an opinion on what the authored icon should leave out

The authoring agent runs `/icon-<family>`, looks at the same render, and makes
every one of those calls itself with the profile's real numbers in front of it.
A brief that pre-empts that work biases the drawing toward the reference's
proportions — exactly what the reconstruction flow exists to avoid. Describe the
reference as it is, including detail that will obviously be cut; just say it
briefly, and let the author decide what goes.

## Scope

This skill produces briefs only. It does not author icons, edit
`icon_set/model/icons/`, or run the build. When the request is "draw this",
prepare the brief and then hand over to `/icon-sub`, `/icon-solo` or
`/icon-container`.
