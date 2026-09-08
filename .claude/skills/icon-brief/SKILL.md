---
name: icon-brief
description: Turn reference SVGs into authoring briefs for the Pictographic icon set. Use when given a folder or file of source SVGs to prepare, triage or catalogue before drawing — renders each one, then writes its name, icon_id, family, description and tags into a brief that /icon-sub, /icon-solo or /icon-container can be run against. The requester names the icon family; this skill never infers it. Hand-authored; edit this file directly.
argument-hint: <svg folder or file> <sub|solo|container> [--out <dir>]
---

# /icon-brief — reference SVGs in, authoring briefs out

Request: $ARGUMENTS

A brief says **what the reference is**. It does not say how to draw it. You
identify and name the subject; the family skill that authors it decides what
survives at native size, what the keyshape is, and where every coordinate goes.
Keep that line and the briefs stay useful for years.

**The family comes with the request, not from you.** The requester names the
icon type — `sub`, `solo` or `container` — and every brief in the run carries
it. See [Family](#family) before writing anything.

Per icon you produce exactly five fields:

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

   Pass `--native` for the requested family — 32 sub, 48 solo, 64 container. It
   defaults to **64**, so omitting it on a solo run previews every icon at the
   wrong size and you describe detail the real canvas will not hold.

2. **Look at every render.** Read `sheets/sheet-NN.png` to triage the batch,
   then open each `png/<stem>.png` individually — the sheet is too small to
   describe from. Also open the `@<native>` copy: not to decide what to cut, but
   so your description does not lean on detail that is not actually there.

3. **Write the manifest** at `<svg folder>/manifest.json` — a JSON array, one
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

4. **Regenerate** against it:

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

   One family, one native size, and the count equal to the number of files.

5. **Report** the count, the output paths, and any reference you think is wrong
   for the requested family — briefed as asked, flagged for the requester.
   Hand over the first command to run: `/icon-<family> <icon_id> — <one
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
python3 -c "import sys; sys.path.insert(0,'.'); from icon_set.model.icons.registry import icons_in; print(sorted(i.icon_id for f in ('sub','solo','container') for i in icons_in(f)))"
```

If it is taken by the same concept in another family, propose the suffixed form
(`bell-sub`); if it is taken by a different concept, pick another name.

## Family

**The requester names the family. You do not choose it, and you do not vary it
across a run.**

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

## The reference is regenerated, not traced

Assume every incoming reference is **too thin and too complex for the canvas it
is headed to**. These SVGs are drawn at illustration scale: hairline strokes,
nested detail, ornament that resolves only when the thing is 320px wide. The
authored icon lands on the requested family's grid — 32, 48 or 64 — with the
profile's stroke weight. Detail that fine does not shrink; it turns into mud.

So the authored icon is a **simpler reconstruction of the subject, not a copy of
the reference**. It is redrawn from the meaning: fewer parts, heavier strokes,
larger gaps, rebuilt on the profile's geometry. What must not change is what the
thing *is* — the silhouette a person recognizes it by, the parts that make it
that subject and not a neighbouring one, the stance and orientation that carry
its sense. Simplify the drawing; never simplify away the meaning.

Your job in the brief is to make that regeneration safe. Name the subject
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
