# Intake

Two modes. Both end in the same place: an `Icon` subclass authored on the
selected profile. Neither one licenses copying a drawing in.

## Brief only

The user gives a concept name and a minimal description.

Use them directly to identify the subject, its essential parts, and their
arrangement. Then go to [authoring.md](authoring.md).

**Do not fabricate evidence.** No synthetic source SVG, no detector run, no
invented reference name. A rough sketch may help you think; it is a draft, not
evidence, and it does not go in the record.

Record on the icon: `category`, `aliases`, `keywords`. If the brief was thin and
you made a judgment call about what the subject includes, say so in your reply
to the user rather than silently deciding.

## Brief plus references

The user places images or files in scope.

Inspect **only** what was placed in scope. For each reference, record what you
took from it and why.

- **Raster (PNG/JPG):** read the silhouette, the part count, the openings and
  cutouts, and the arrangement. Describe semantic regions in your own words. Do
  not invent element ids for shapes that exist only as pixels.
- **SVG:** **render it and look at it.** Do not read its coordinates and fit
  primitives to them. That reproduces an exporter's fragmentation, its stroke
  ratio and its accidents, none of which survive a 64-unit canvas with a fixed
  4-unit stroke -- and it answers the wrong question. Geometry tells you what
  coordinates a drawing has; the picture tells you what it *is*, which is what
  you are about to rebuild. Use
  `python3 icon_set/scripts/prepare_references.py <folder> --out <work dir>`
  to rasterize a whole folder, or `cairosvg` for one.
- **Anything else:** open it with an appropriate reader. If you cannot inspect
  something essential, say so. Never quietly substitute a different reference or
  claim you reviewed one you could not open.

### What a reference is, and is not

A reference is evidence about the **subject**: what it is, which parts carry its
identity, how they sit together.

It is **not**:

- a grid — recompose on the selected profile's canvas;
- a stroke weight — this system is always 4;
- a licence to add features the brief did not ask for;
- a licence to draw a different subject;
- authority over the brief. If they conflict, resolve it with the user before
  authoring.

A reference's extraction defects — clipped edges, missing geometry, stray
fragments — are defects. Do not reproduce them.

## Reconstructing a folder of references

For a batch, prepare it once and then work through it one icon at a time:

```bash
python3 icon_set/scripts/prepare_references.py container_icons/svg --out container_icons/work
```

That writes, per icon, a large render and a native-size render, plus a brief
carrying whatever concept, description and tags the source manifest had. Pass
`--native 48` when the batch is solo subjects and `--native 32` for sub glyphs;
the default of 64 suits a container batch. It also
writes contact sheets and an `index.html`, so a set can be triaged in a couple of
screens before any of it is authored.

Then measure each source from its render, which turns a picture into an
authoring brief without copying a single coordinate:

```bash
python3 icon_set/scripts/reconstruct.py trace container_icons/svg
```

Per icon that writes painted bounds and aspect in the target canvas's units,
the keyshape those proportions point at, every full-width and full-height rule
with its position and thickness, every detached mark with its centre, and the
corner rounding. For a browser window it says: square, corner rounding about 8,
rules at y 1.6, 15.3 and 62.1, two marks at y 8.5. That is what the subject
*is*, stated in numbers you can design against.

Recompose those proportions on the profile; do not transcribe them. The trace's
numbers are fractional and this system is integer, and the gaps a source uses
are often tighter than the profile's minimum clearance — the browser window's
own header packs its rules 6.5 units apart where CONTAINER64 needs 8, so the
band has to open up. That is a decision the trace informs, not one it makes.

**Then check you drew the same picture.**

```bash
python3 icon_set/scripts/reconstruct.py compare --family container
```

This is the step that keeps a batch honest. Validation says the rules were
followed; it cannot tell you a feature went missing. `compare` renders the
source and the authored icon at native size and reports `fidelity` — how much
of each is accounted for by the other, allowing 2 units of stroke movement —
alongside the raw `iou`, and writes a source/authored/overlay panel you can
look at. The ledger sorts worst first, so the batch has a work queue rather
than a pile. A reconstruction that validates at fidelity 0.55 is a different
icon; go back to the render before you go back to the validator.

The order matters. **Look, then measure, then decide, then draw, then compare.** Read the brief, look at the
render, say in one sentence what the subject is, and only then choose the
family — which fixes the profile — and the keyshape. An icon reconstructed from its picture is a new
drawing of the same subject on this system's terms -- which is the goal.
Reproducing the reference's coordinates is not.

Check the native-size render too. It shows what actually survives, and it is
usually the thing that decides which details to drop.

## Lucide references

Use these as the default construction reference in **both** modes, while
preserving the subject established by the user brief and any supplied references. The local bundle
at `icon_set/references/lucide/` is a **construction** reference: how contours
flow, how a corner is turned, how parts are spaced. It carries each icon twice —
`original/` for the drawing, `atomic-debug/` for its geometry.

```bash
python3 icon_set/scripts/lucide_reference.py search 'cloud' --limit 6
python3 icon_set/scripts/lucide_reference.py inspect cloud --profile SOLO48
python3 icon_set/scripts/lucide_reference.py atoms cloud
python3 icon_set/scripts/lucide_reference.py search 'square' --kind arc/quarter-circle
```

`inspect` reports an original in this system's terms — painted bounds, aspect
ratio, and which keyshape those proportions actually point at. Pass the
profile of the family you have chosen: `SUB32`, `SOLO48` or `CONTAINER64`.

`atoms` is the geometry half. It lists the reference's segments in document
order with each one's kind — `line/horizontal`, `arc/quarter-circle`, `cubic`
and so on — and its own `d`, read from `atomic-debug/`. Use it when the question
is *how is this made*: whether a corner is an arc or a mitre, where a curve
stops being a curve, how many arcs a lobe actually takes. `search --kind` runs
the same vocabulary backwards, finding references built out of a construction
you are trying to learn.

**It is an inventory, not a part count.** The decomposition is analyser output:
it splits a native circle into four quarter-arcs and numbers its colours
sequentially. Your contours are decided by how the icon should paint — one path
per contour, round joins inside it — never by how many atoms the reference
reports.

Two things it will remind you of, because both matter:

- **Lucide is 2/24; this system is 4/32.** Ours is 1.5x heavier relative to the
  canvas. Detail that separates cleanly there can close up here.
- **Lucide coordinates are fractional; ours are integers.** A reference
  proportion is a target to re-derive from your keyshape's extremes, never a
  number to multiply through.

Search the subject, and separately search a construction family when that is the
real question — an enclosure, a handle, an attachment. Inspect only what answers
a question you actually have. There is no required reference count, and no
reason to read the corpus.

Record the references you used and the principle you took from each. If nothing
useful matched, say that honestly instead of naming something you did not use.
