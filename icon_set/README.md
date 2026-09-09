# `icon_set` — Pictographic icon system

Three families, three canvases, three folders, one rule: **an icon's family
decides where it lives, what canvas it is drawn on, and where it ships.** The
families never share a canvas and never share a folder.

| Family | Profile | Canvas | Authored in | Ships to | Icons |
|---|---|---|---|---|---|
| `sub` | `SUB32` | 32×32 | `model/icons/sub/` | `dist/sub32/` | 52 |
| `solo` | `SOLO48` | 48×48 | `model/icons/solo/` | `dist/solo48/` | 13 |
| `container` | `CONTAINER64` | 64×64 | `model/icons/container/` | `dist/container64/` | 5 |

The geometry model and vector validator use the standard library. Build-time
hole/pinch QA requires CairoSVG, NumPy, OpenCV, and Pillow; install them with
`python3 -m pip install -r icon_set/requirements-qa.txt`. Imports are lazy.

```bash
python3 -m unittest discover -s icon_set/tests -t .     # test suite
python3 icon_set/scripts/build.py                        # validate + export every family to dist/
python3 icon_set/scripts/build.py --family solo          # one family only
python3 icon_set/scripts/generate_skills.py              # regenerate /icon-sub, /icon-solo, /icon-container
python3 icon_set/scripts/profile_lab.py show             # the profile numbers in force
python3 icon_set/scripts/profile_lab.py try SOLO48.interior_guide_inset=8   # what a change would cost
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo.png
python3 icon_set/scripts/lucide_reference.py inspect heart --profile SUB32
python3 icon_set/scripts/compose.py --host container-circle --sub heart --png
```

**Designing a new icon?** Use the family's slash skill — `/icon-sub`,
`/icon-solo` or `/icon-container` — generated from the contracts into
`.claude/skills/`. The shared technique library they point at is
[`skills/icon-design/SKILL.md`](skills/icon-design/SKILL.md). A map of every
folder and script by mission is in [`STRUCTURE.md`](STRUCTURE.md).

## The families

**`sub` — 32.** A glyph read small and hosted by others: verbs, states,
modifiers, operators, arrows, chevrons, and simple noun shapes such as `heart`
or `circle` that work as content. Its canvas is exactly the container's content region.

**`solo` — 48.** A standalone subject drawn to be read on its own: a device, an
object, a badge, a traced drawing whose proportions matter. It hosts nothing and
is hosted by nothing. `smartwatch`, `film-frame` and `award-ribbon` live here.

**`container` — 64.** An enclosure or a framed device: a window, a screen, a
board, a card, a badge. Drawn as its subject requires, interior furniture and
all — nothing inside the canvas is reserved. It stands alone as a noun and is
the outer half of a `CONTAINER_COMBINE`; whether it clears a given sub icon is
measured by `compose.py` rather than promised in advance. A composition is
emitted on `CONTAINER64` and belongs to this family.

The protected slot that used to keep `(16,16)-(48,48)` empty was **withdrawn**
on 2026-09-07. It guaranteed hosting at the price of the containers: a 64
canvas leaves 12 centerline units above a centred 32×32 slot, a title bar with
an indicator row needs 20, so windows, tab bars, lids and dial faces could not
be drawn at all. `(16,16)-(48,48)` is now the *content region* — advisory, the
place a hosted child lands.

The binding is written once, in `model/contracts/icon-profile.v1.json` under
`families`, and enforced three times over:

1. **The family base has no profile to override.** `Sub32`, `Solo48` and
   `Container64` resolve their profile from the family name through the
   contract. A subclass can say which family it is; it cannot say which canvas.
2. **The registry discovers by folder** and refuses a module whose class
   belongs to another family. A `Solo48` saved into `sub/` fails discovery with
   both family names in the message.
3. **The validator's first check** rejects any icon whose profile is not its
   family's, and the record schema requires `family` and binds it to `profile`.

Each family builds into its own `dist/<family><canvas>/` folder with its own
`manifest.json`, so a consumer of the 32 set never sees a 48 or 64 record.

Profile names are the family plus the canvas. Earlier releases named the 48 and
64 profiles for a role rather than a family, which is how a solo subject ended
up on the container canvas; the numbers are unchanged, only the binding is new.

## Authoring an icon

One new file in the family's folder, subclassing the family's base:

```python
# icon_set/model/icons/sub/heart.py
from ...keyshapes import Keyshape
from ._base import Sub32

class Heart(Sub32):
    icon_id = "heart"
    keyshape = Keyshape.HRECT_XL         # visible (0,2)-(32,30) on SUB32
    semantic_role = "MAIN"
    semantic_kind = "noun"

    def build(self) -> None:
        self.add_arc("lobe-left", (16, 11), (2, 11), radius_x=7, sweep=False)
        self.add_line("side-left", (2, 11), (16, 28))
        self.add_line("side-right", (16, 28), (30, 11))
        self.add_arc("lobe-right", (30, 11), (16, 11), radius_x=7, sweep=False)
        self.add_contour("outline", "lobe-left", "side-left", "side-right", "lobe-right", closed=True)
```

```python
heart = Heart()
heart.profile                    # Profile.SUB32 -- decided by the family, not the class
heart.validate_icon()            # ValidationReport(status="valid", ...)
heart.export_icon_to("heart.svg")
```

Nothing to register: the folder is the registry. Geometry is authored
**backwards from the keyshape's four extreme coordinates** in the family's own
canvas. Pick the keyshape first, write those numbers down, then place geometry
to hit them exactly.

## Where the numbers live

`model/contracts/*.json` is the single machine-readable source. `profiles.py`
and `keyshapes.py` read it and cross-check themselves against it at import
time, so the runtime table and the contract cannot drift apart.

| File | Holds |
|---|---|
| `icon-profile.v1.json` | the three families and their profile/folder/dist binding; per profile: canvas, interior guide, MIC, centerline minima, rational scale; style; tolerances |
| `keyshapes.v1.json` | 10 base sizes and all 30 resolved profile definitions |
| `exceptions.v1.json` | approved `FREE` records keyed by `(icon_id, profile)`: bounds, rationale, approval id |
| `composition-templates.v1.json` | the four classes; `SOLO` and `CONTAINER_COMBINE` are frozen |
| `categories.json` | the category tree (`primitives/*`, `objects/*`, … — a *subject* taxonomy, orthogonal to family) |

## Two decisions this implementation froze

The plan left both open, and every icon's geometry depends on them.

**1. The painted envelope is exact.** Every cap and join is round, so the
painted region is exactly the Minkowski sum of the centerline with a disc of
radius `stroke/2`. Visible bounds are therefore the centerline bounds grown by
exactly 2, and the rectangle-family fit test runs at **tolerance 0**.
`validation/envelope.py` still derives this per primitive — segment endpoints,
plus an arc's true axis extrema from its centre parameterization — so curves
are measured rather than assumed.

**2. Rectangle fit and circle fit are different tests.**

- `SQUARE` / `HRECT_*` / `VRECT_*`: the visible bounding box must **equal** the
  keyshape bounds, exactly.
- `CIRCLE`: a **radial** test. All ink within radius `R` (exact), and maximum
  radial extent `>= R - 0.5` so the artwork touches its envelope. A bbox test
  would reject every genuinely radial subject, because a regular pentagon or
  five-point star has no exact integer vertices at any useful radius.

A consequence worth knowing: **there is no full-canvas square keyshape.**
`CIRCLE` is the only full-canvas token and it is radial-only, so full-bleed
rectilinear art uses `SQUARE` (28 of 32, 42 of 48, 56 of 64).

## Validation

Every build also runs the rendered hole/pinch gate ported from `claude_skills`.
Its rules live in `model/contracts/negative-space.v1.json`: minimum authored hole
radius 1u (diameter 2u), configured solid fill depth 1u, and 32 raster samples per
unit. The source measurement algorithm and its adjusted fill-depth calculation
are retained; see `validation/PROVENANCE.md`. Spacing uses this project's profile
MIC values, never the old source project's spacing settings.

```bash
python3 icon_set/scripts/build.py --debug                  # HTML + debug images
python3 icon_set/scripts/build.py --no-debug --report      # HTML, no debug images (default)
python3 icon_set/scripts/build.py --debug --no-report      # images + JSON, no HTML
python3 icon_set/scripts/build.py --no-debug --no-report   # validation, no QA artifacts
python3 icon_set/scripts/validate_library.py --debug       # inspect without releasing
```

The Python entry point accepts the same independent switches:

```python
from icon_set.scripts.build import build
build(debug=True, report=True)
```

The default report is `dist/qa/index.html`, with library-wide `results.json` and
one `<family>/<icon>/metrics.json` per icon. `debug=True` adds `spacing.svg`,
`spacing.png`, and `holes.png`. The report supports search and family/status
filters, shows clean previews, distances, authored and measuring diameters,
findings, and SVG/rule hashes. Even a `--family` build reports the entire current
library; unselected families are marked as context and do not block that build.

**Small-circle hole exception:** complete circular contours with a centerline
size of exactly 4×4 or 6×6 units (radius 2 or 3) may pass the hole gate even
below its usual minimum. This applies to circles inside any icon, including
circles authored from arcs. The rule is recorded in `negative-space.v1.json`.
The report retains the measured failure and labels the accepted result as a
circle exception. Other sizes, non-circular regions, and circles split by extra
strokes receive no exemption; spacing, pinch, and other rules still apply.

These switches control evidence only: spacing and hole checks always run for
built icons, even with `--no-png`. Failed icons and checker errors block release,
while a fresh diagnostic snapshot is saved for inspection. A new enabled QA run
replaces stale debug/report files; disabling both leaves the last saved snapshot
untouched. Reports describe current source validation, not published release
status. A zero-hole result on a processing error is never a pass. Raster values
near a threshold should be inspected visually; do not lower the rule to hide a
failure.


Structural validation checks metadata, filenames, geometry types, and references
before measuring a drawing. Duplicate contour IDs and conflicting output path
IDs are errors, and every primitive must appear in exactly one emitted path.
Composition spacing exemptions use explicit child ownership rather than names.

Release builds stage all selected families, including PNG previews, before
replacing output directories. Validation or rendering failures leave the previous
release intact; publication I/O errors trigger rollback. Directory replacement
is atomic per directory, but the complete set of SVG and PNG directories is not
a single transaction against process termination or power loss. Avoid concurrent
builds to the same destinations.


`icon.validate_icon()` runs `validation/validator.py`'s eight checks in the
locked order from plan section 5, and reports the element id and coordinates
for every failure:

```
schema/profile → style/grid → canvas/keyshape bounds → mic → keyshape
              → composition → svg round-trip → reproducibility
```

The first check now includes the family binding: `sub` on anything but `SUB32`,
`solo` on anything but `SOLO48`, or `container` on anything but `CONTAINER64`
is an error before any geometry is measured.

The MIC engine (`validation/stroke_distance.py`) is **vendored** from the
previous system with one import changed. It uses exact rational predicates for
straight segments and adaptive curve subdivision with Hausdorff bounds, and it
returns three verdicts — `pass`, `fail`, and `review`. **`review` is not a
pass**: it means the engine could not certify the result within its numerical
bounds, and the corpus test asserts no shipped icon produces one.

Intentional contacts are declared per pair with `icon.relate("connect", a, b)`.
A declaration excuses **that pair only**; it is never a global bypass, and
`test_a_declaration_is_scoped_to_its_own_pair` proves it.

## The `sub` set (52, SUB32)

| Keyshape | Symbols |
|---|---|
| `SQUARE` 28×28 | plus, close, asterisk, hash, square, diamond, hexagon, octagon, triangle up/down/left/right, arrow-up-left/-up-right/-down-left/-down-right, chevrons-up/-down/-left/-right, skip-forward, skip-back |
| `CIRCLE` 32×32 | circle, pentagon, star, sparkle, target |
| `HRECT_XL` 32×28 | heart |
| `HRECT_L` 32×24 | check, menu, divide, arrow-left, arrow-right |
| `HRECT_M` 32×20 | chevron-up, chevron-down, tilde, arrows-horizontal |
| `HRECT_S` 32×16 | equals |
| `VRECT_XL` 28×32 | slash, backslash |
| `VRECT_L` 24×32 | arrow-up, arrow-down |
| `VRECT_M` 20×32 | chevron-left, chevron-right, arrows-vertical |
| `VRECT_S` 16×32 | pause |
| `FREE` | minus, bar, dot, exclamation, ellipsis, dots-vertical |

## The `solo` set (13, SOLO48)

The set contains `award-ribbon`, `bathrobe-with-tied-belt`,
`beer-mug-with-foam`, `dress`, `film-frame`,
`open-end-maintenance-wrench`, `organizational-hierarchy-cube`,
`paper-airplane-message-send`, `passenger-bus`, `sailboat`, `smartwatch`,
`tropical-island-with-palm-tree`, and `vintage-studio-microphone`.
Each reference-backed subject was re-authored on the 48 canvas; none is a
scaled copy of source geometry, and the model rejects scale transforms.

## The `container` set (5, CONTAINER64)

`container-circle`, `container-square`, `container-rounded-square`,
`container-hexagon`, `clipboard`. Each keeps the slot empty by construction and
`test_every_registered_container_leaves_the_slot_empty` proves it.

### Notes that cost a cycle to learn

- **Curved parts need real MIC margin, not a threshold-exact fit.** `target`
  was first drawn with radii 14 and 7, exactly the 7-unit SUB32 minimum. The
  spacing engine measured 6.99987 through its curve-flattening bound and
  returned `review` rather than certifying a pass. Radius 6 (8 units of
  spacing) is correct. Straight-line pairs are exact and may sit on the minimum
  — but only if *both* paths are straight. `film-frame`'s perforations sat
  exactly 8 from the frame's straight rails and still came back `review`,
  because the rails share a contour with curved corners. They sit at 9 now.
- **A 48 canvas holds one feature fewer than you think.** `film-frame` on
  `SQUARE-48` has 15-unit bands between its curved edge and each divider; a
  4-unit mark with the 8-unit minimum on both sides needs 16. `VRECT_XL-48`
  gives 18 and the design survives with all its parts.
- **Regular polygons have no integer vertices.** Pentagon and the five-point
  star place vertices on the nearest grid point to the true radius, which the
  circle touch rule accepts. The octagon is authored as a chamfered square
  instead, so every vertex is exact.
- **Six glyphs cannot fill any keyshape.** minus, bar, dot, exclamation,
  ellipsis and dots-vertical have a stroke-defined 4-unit axis, and the
  smallest standard minor dimension is 16. Each has an approved `FREE` record;
  the family base refuses to construct a FREE icon that has none. Records carry
  a `status`: release requires `approved`, a draft run accepts `proposed`, so an
  agent can submit one for review without being blocked.
- **A tangent-continuous junction is worth designing for.** The heart's lobe and
  shoulder are both circles centred on `y = 12`, so they meet vertically with no
  corner. Running a straight side off the widest point instead puts a
  41-degree kink where the eye reads the shoulder — same bounds, same keyshape,
  same validator verdict, visibly worse.
- **Pick the arc radius whose apex is the endpoint.** The `smartwatch` strap
  rises from (10,11) to (22,5) with r 15 because that is the one integer radius
  whose circle tops out exactly at (22,5), so the arc leaves tangent-horizontal
  and cannot bulge past the keyshape. The fitted radius from the trace bulged.
- **A container's interior is measured, not reserved.** The hexagon's top
  corners sit at `x = 14` rather than `x = 22` because at 22 its diagonals cut
  across where a hosted child sits. That is now a hosting trade-off reported by
  `compose.py`, not a rule — draw the subject, then measure what it holds.
- **A composite is measured from `draw()`, not `.primitives`.** A `CombinedIcon`
  holds its geometry in its placed children; reading the raw attribute reports a
  composite as empty.

## Lucide references

`references/lucide/` carries 1,798 original Lucide SVGs in two views, the index,
and the licences.

- **`original/`** — the drawing as Lucide ships it.
- **`atomic-debug/`** — the same icon split into one `<path>` per segment, each
  tagged `data-atom` (`element.segment`), `data-src` (the element it came from)
  and `data-kind` (`line/horizontal`, `arc/quarter-circle`, `cubic`, …). This is
  the **geometry reference**: an outline tells you the silhouette, the atoms
  tell you how it is built. Lucide's heart is one `d` string; its atoms are
  three circular arcs, two cubics and two diagonals closed into a ring — the
  shape of the `add_arc` / `add_line` / `add_contour` calls that would rebuild
  it here. Read it as an inventory of the construction, never as a part count
  to match: it is analyser output, and it cuts a native circle into four
  quarter-arcs. `PROVENANCE.md` has the full attribute table and the caveats.

`scripts/lucide_reference.py` reads both and reports them in this system's terms
— painted bounds, aspect ratio, which keyshape those proportions point at on the
profile you name, and the atom tally. Asked about `heart` on `SUB32`, it
independently answers `HRECT_XL`, which is the keyshape that icon uses.
`atoms <name>` lists the segments on their own, and `search --kind
arc/quarter-circle` narrows a search to references built out of the
construction you are trying to learn.

Lucide is 2/24 and this system is 4/32, so a reference is 1.5x lighter relative
to its canvas, and its coordinates are fractional where all of ours are
integers. It is a construction reference, never a source to copy.

## Not in this release

The rest of M6 (`SIDE_COMBINE`, `DIAGRAM_COMBINE`, the constraint solver), M7
taxonomy, M8 agents, M9 dedupe, M10 packaging and catalog.

**Variants are deliberately deferred.** Identity is `(icon_id, profile)`, and
the profile is the family's: one drawing per concept per family. The
`-variant-N` suffix is reserved and documented, not implemented. Each family's
manifest is a list of records rather than a map keyed by concept, so a variant
field can be added later without a format break.

## Within-contour spacing review

Every build also inspects sustained opposing edges within each contour. It can
flag touching dress straps and narrow wrench jaws even when they belong to one
connected component. This is an **advisory**: it sets `needs_review` and
`internal_spacing.status = "review"`, but leaves release status unchanged.
Existing spacing uncertainties still block release as before.

The diagnostic samples lines/arcs at up to 0.25-unit intervals, looks for
approximately parallel opposing stretches at least 2 units long, and compares
clear ink gaps to the icon profile's MIC. Adjacent segments, shared endpoints,
0.5-unit endpoint neighbourhoods, and complete circular contours are excluded.
Circles retain their existing hole validation. Findings are approximate and
need visual review; this is not a proof that all internal gaps are valid.

`--debug` saves `internal-spacing.svg` and `internal-spacing.png`, with amber
edges and numbered red gap markers. The report lists both element IDs, the
measured gap (negative for overlap), and the sustained length. Use its
**Needs review (advisory)** filter to inspect candidates. Passing release checks
and an advisory can coexist; JSON and manifests keep these separate.

## Interactive icon gallery

Every successful build also creates `dist/gallery/index.html` and `icons.json`.
The gallery shows all currently exported families, including unchanged families
when building with `--family`. It is generated even with `--no-report`. A failed
build preserves the previous gallery and exported icons.

Search by name or keyword, filter by family/category, and click an icon to see
its enlarged preview, canvas, stroke, keyshape, SVG source, full metadata, and
validation details. Download its SVG or describe a requested change in the
feedback textarea. Submitted feedback is stored on the server with the icon
family/ID, SVG revision hash, and timestamp. The inspector shows the latest
100 submissions for that icon. Unsaved drafts stay in the current browser when
local storage is available. Feedback records requests; it does not edit icons.

From the repository root:

```bash
python3 icon_set/scripts/build.py
python3 icon_set/scripts/deploy.py --open
# On a server, listen on all interfaces:
python3 icon_set/scripts/deploy.py --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/` locally or `http://SERVER_IP:8000/` remotely.
`deploy.py` serves the build; it does not upload files or run a build for you.
It needs only Python 3.10+ and the standard library; build requirements remain
in `requirements-qa.txt`. Paths default relative to the script, so it works
from any working directory. For deployment, copy `icon_set/dist/` and
`icon_set/scripts/deploy.py` and `icon_set/scripts/brief_queue.py`, preserving that layout.

Feedback defaults to `icon_set/data/feedback.sqlite3`, outside the public build
folder, and survives rebuilds/restarts. Back up this database. Override with
`--database /persistent/path/feedback.sqlite3`; use `--dist /path/to/dist` for
a custom build. The gallery is shared: all visitors can read and submit feedback.
For an internet-facing server, run it behind a reverse proxy providing HTTPS,
access control if needed, and request limits; preserve the original `Host`
header. Use a service manager to keep the process running.

### Review grid and approval

Each icon card shows its category and review status, with an **Approve** button.
Use the **All icons / Ready / Pending / Approved** tabs with the category,
family, and search filters. Tab counts reflect the current category/search.
Click a card to inspect it and change its status using the review dropdown.

- **Ready**: a new icon version awaiting review.
- **Pending**: needs changes; saving feedback sets this automatically.
- **Approved**: a reviewer confirmed the icon is OK using **Approve**.

Decisions are shared across visitors and saved in the existing SQLite database.
They survive restarts and rebuilds of identical SVGs. A changed SVG starts Ready
and requires a fresh approval. Existing feedback migrates to Pending without
overwriting later decisions. Restart `deploy.py` after updating the server code,
then reload the gallery. API status values are `ready`, `pending`, and `approve`.

### Icons, generator feedback, and final icons

The gallery has three top-level tabs. **Icons** browses the library. **Feedback**
shows requests newest first, with category/status/search filters, the referenced
SVG version, Copy change brief, Inspect & respond, and Mark ready for review.
This page helps a generator review requests; it does not generate or edit files.
**Final icons** shows only the currently approved generated SVG versions.

This is an internal application. The Feedback tab opens directly without a login
or access key. `GET /api/feedback-feed` returns requests with the icon family/ID,
requested change, SVG hash, and timestamp. Restart `deploy.py` after updating
server code; refresh the browser after gallery updates.

### Preserve versions when applying feedback

**Copy change brief** now instructs an agent to create a separate variant.
From the repository root, scaffold a copy before changing its geometry:

```bash
python3 icon_set/scripts/create_variant.py --icon square --family sub --label "Softer corners"
# Edit the NEW file printed by the command, then validate/export:
python3 icon_set/scripts/build.py --family sub
```

The scaffold allocates a unique ID such as `square-v2`, then `square-v3`,
and creates a separate class/file in the same family. It copies the current
implementation and source-reference metadata. The parent file is never written.
The new file is an independent starting copy, not an automatic geometry change.

Variants declare `variant_of` (the immediate parent icon ID) and `variant_label`
on their class. The registry rejects missing parents, cross-family ancestry,
empty labels, and cycles. The fields are exported in manifests; the gallery
links the complete version family and shows the previous generated version in
the inspector alongside the usual output/original-reference comparison.

Variants have separate feedback and approvals because their IDs differ. A new
variant starts Ready. Creating or approving one does not change its parent's
review status. Final icons shows every individually approved version. Existing
icons need no metadata changes. Existing historical edits cannot be recovered
by this feature; version preservation starts with new variants.

For a manually created variant, use a unique ID, same family, parent ID, and
nonempty label, and keep the old module in place. For shared modules, the scaffold imports sibling icons instead of registering
duplicates. Per-ID FREE keyshape exceptions need a manual variant with valid
exception metadata.

### Icon-making router and combined-reference rejection

Use `$icon-making` (Claude: `/icon-making`) as the entry point for a reference or
creation request. It visually checks the subject, honors an explicit family,
otherwise chooses solo/sub/container and reads the matching authoring skill.
It preserves existing versions for review-driven changes.

The router rejects two kinds of combined reference as a single primitive:
container + hosted sub icon, and a main subject + adjacent sub modifier. It
queues exactly two component briefs and stops instead of authoring the combined
primitive, unless generating the components was also requested. Intrinsic parts
of one object are not split.

In the inspector, **Reject — combined primitive** opens a form for the
combination type and two component names/families/descriptions. Submit to reject
the current SVG revision and create two **Pending briefs**. Repeated submissions
do not duplicate or reset an active split. A rejected icon cannot be approved or
enter Final icons. Its files and feedback remain intact. **Restore for review**
returns it to Ready and removes its split from the active queue.

Pending briefs provide **Copy generation brief**, routed to `$icon-making`, and
**Mark generated** to link a built standalone icon in the correct family. This
does not approve the component. Existing standalone icons can fulfill a brief;
the rejected composite cannot.

Before a reference has a generated icon, the router can queue JSON with
`icon_set/scripts/queue_brief.py --file <split.json>`. The JSON shape and routing
rules are maintained in `.claude/skills/icon-making/SKILL.md`; generated Codex
and portable copies live in `.agents/skills/icon-making/` and `skills/icon-making/`.
The queue shares the server feedback database. Use the same `--database` path for
the CLI and server; on a remote deployment transfer the JSON handoff or use the
review app rather than writing to a different local queue.
