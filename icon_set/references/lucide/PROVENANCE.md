# Lucide construction references

This is a local, offline reference snapshot copied on 2026-09-03 from the
user-provided sibling `analyze_lucide` dataset. It contains 1,798 original SVGs and their per-segment decompositions.
The upstream commit/version of that dataset was not recorded; do not claim this
is a version-pinned release or the latest Lucide collection. Per-file SHA-256 hashes in `index.json` identify
the exact imported snapshot.

- `original/`: unchanged original icon geometry and source element grouping.
- `atomic-debug/`: the same 1,798 icons decomposed into one `<path>` per
  segment, for reading construction.
- `index.json`: searchable names/keywords, paths, counts, and content hashes.
- `LICENSE`: Lucide's ISC notice and the Feather-derived icons' MIT notice,
  retrieved from https://raw.githubusercontent.com/lucide-icons/lucide/main/LICENSE
  on 2026-09-03. Retain these notices when distributing the reference corpus.

## What this copy carries

Carried into `icon_set/`: `original/`, `atomic-debug/`, `index.json`, `LICENSE`,
this file. Nothing is omitted. Every entry in `index.json` names both views and
carries a SHA-256 for each.

### `atomic-debug/` — the geometry reference

Each file is the matching original split into **atoms**: one `<path>` per
segment, stroked on a hue ramp so the decomposition is visible, and carrying
three data attributes.

| attribute | meaning |
|---|---|
| `data-atom` | `<element>.<segment>` — the leading number groups segments that came out of the same source element, so a ring stays identifiable as one contour |
| `data-src` | the SVG element the segment came from: `path`, `rect`, `circle`, `line`, `ellipse`, `polyline`, `polygon` |
| `data-kind` | the segment class: `line/horizontal`, `line/vertical`, `line/diagonal`, `arc/quarter-circle`, `arc/circular`, `arc/elliptical`, `cubic`, `quad` |

This is the half of a construction reference an outline cannot show. Lucide's
heart is a single `d` string; its atoms say it is three circular arcs, two
cubics and two diagonals closed into a ring — which is the shape of the
`add_arc` / `add_line` / `add_contour` calls that would rebuild it on a profile
here. Reading it answers *how is this corner turned, where does that curve stop
being a curve*, which is the question a reference is for.

**Read it as an inventory, never as a part count to reproduce.** It is analyzer
output, not the designer's own structure: it splits a native circle into four
quarter-arcs and numbers its colours sequentially within each icon rather than
by meaning. Splitting one contour into many paths does not improve a drawing,
and this system's own contour rules — one path per contour, round joins inside
it — are decided by how the icon should paint, not by where the analyser
found it convenient to cut. `segmentCount` and `segmentKinds` in `index.json` are counted
from these files; `tests/test_references.py` asserts the two still agree, so a
drifted or truncated copy is caught.

Read a few relevant icons, not the whole corpus:

```bash
python3 icon_set/scripts/lucide_reference.py search 'subject or construction' --limit 6
python3 icon_set/scripts/lucide_reference.py search 'square' --kind arc/quarter-circle
python3 icon_set/scripts/lucide_reference.py inspect house --profile SUB32
python3 icon_set/scripts/lucide_reference.py atoms house
```

**Lucide is 2/24; this system is 4/32.** A reference is proportionally about
twice as heavy relative to its canvas, so detail that survives there may not
survive here. Recompose on the selected profile; never copy a 24-unit drawing in.

The source subject/brief remains authoritative. Lucide is a style/construction
reference, not permission to add an unrelated feature or substitute an icon.
See the maintained project workflow in `docs/shared/icon-pipeline.md` and the
official guide at https://lucide.dev/contribute/icon-design-guide.
