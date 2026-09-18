# Pictographic icon app

This repository contains the Pictographic icon library, its Python drawing and
validation system, and a local web app for generating, editing, and reviewing
icons. Python geometry is exported as SVG, PNG previews, and gallery data.

The normal workflow is **run the app → generate a candidate → inspect it → add
it to the grid → approve the finished SVG**. Building an icon and approving it
are separate operations.

## Contents

- [Install and run](#install-and-run)
- [Generate an icon in the app](#generate-an-icon-in-the-app)
- [Execute generation from the terminal](#execute-generation-from-the-terminal)
- [Author an icon in Python](#author-an-icon-in-python)
- [Build and export commands](#build-and-export-commands)
- [How validation works](#how-validation-works)
- [Edit validation and manual artwork](#edit-validation-and-manual-artwork)
- [Files, storage, and deployment](#files-storage-and-deployment)
- [Troubleshooting](#troubleshooting)
- [Tests and further documentation](#tests-and-further-documentation)

## Install and run

Run the commands below from the repository root: the directory containing
`icon_set/`, `skills/`, and this README. Examples use a macOS/Linux shell.

Requirements:

- Python **3.10 or newer**.
- The packages in `icon_set/requirements-qa.txt`: CairoSVG, NumPy,
  OpenCV Headless, Pillow, and Matplotlib.
- For AI generation: an installed, authenticated **Codex CLI** available to the
  operating-system account running the server. Drawing and validating Python
  icons does not require Codex.

Create an environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r icon_set/requirements-qa.txt
```

Keep the environment active when building and starting the server. Keep `.venv/`
out of commits; the repository ignores that directory.

Build the gallery and exports:

```bash
python3 icon_set/scripts/build.py
```

Then start the app in the same environment:

```bash
python3 icon_set/scripts/deploy.py --open
```

Open [the local app](http://127.0.0.1:8000/). Leave the terminal running; use
**Ctrl+C** to stop it. To restart later, activate the environment and run
`deploy.py` again. A rebuild is needed when icon sources or generated gallery
assets change; starting the server does not run a build.

If the build exits with failed icons, inspect the printed findings and the
gallery's **Failed build** view. Passing icons can still be exported, so a build
exit code of 1 does not necessarily mean that the app cannot start.

The public navigation includes **Home**, **Design rules**, **Icon**, and
**Icon Grid**. The Icon page contains approved icons; Icon Grid is the review
workspace. Log in to generate, save edits, or make review decisions. The current
development accounts are `jakes`, `ray`, `phuong`, and `hina`, each with password
`1`, as defined in `icon_set/scripts/deploy.py`.

## Pipeline API reference

Open **API** in the app navigation or `/gallery/api.html` for the complete
review pipeline reference. It includes a configurable production/local base URL,
login instructions, an endpoint explorer with copyable curl requests, reads by
stage, Ready/Disapproved/Approved/Rejected transitions, feedback, artwork
revisions, and generation acceptance. The page builds commands without sending
write requests. All pipeline API calls work without login and are attributed to `system`.
An optional reviewer session attributes actions to the logged-in reviewer.

## Generate an icon in the app

1. Ensure Codex is installed and signed in under the account running the server.
   If its executable is not on that account's PATH, set `CODEX_BIN` to its full
   executable path before starting `deploy.py`.
2. Open **Icon Grid**, log in, and open its **Generate** view.
3. Enter an icon name and a concrete description of the subject, silhouette, and
   essential details. Choose **Auto**, **sub**, **solo**, or **container**.
4. Optionally select a model or attach references. Leaving the model blank uses
   the server's Codex configuration. Up to four references are supported:
   PNG files up to 2 MB each, or SVG files up to 1 MB each.
5. Start generation and inspect the candidate, validation outcome, and run log.
6. Choose **Add to grid** to accept the new source file, or **Discard**. An
   accepted candidate enters the grid as **Ready**.
7. Review the accepted SVG and approve it when satisfied. Only the approved
   current SVG version appears in the approved/final views.

Example description:

> A standalone watering can in side view, with one curved handle, a short angled
> spout, and a clearly recognizable body. Use the solo family.

Choose the family by the icon's job:

| Family | Canvas/profile | Intended use | Source folder |
| --- | --- | --- | --- |
| `sub` | 32×32 / `SUB32` | Small glyph, modifier, state, arrow, operator, or hosted content | `icon_set/model/icons/sub/` |
| `solo` | 48×48 / `SOLO48` | Standalone object, animal, person, or other subject | `icon_set/model/icons/solo/` |
| `container` | 64×64 / `CONTAINER64` | Enclosure, window, card, screen, frame, or bubble | `icon_set/model/icons/container/` |

An avatar is a specialization of `solo`. Its head and body remain one subject.
A distinct enclosure plus a hosted symbol, or a subject plus an adjacent modifier,
may require two standalone component briefs. The icon-making workflow handles
that split instead of treating the combination as one primitive.

### Upload a new icon

Open **Icon review → Upload icon** and choose an SVG up to 1 MB. No login is
required for the upload page or `POST /api/icons/upload`. The page shows the full
production endpoint and a copyable curl example:
`https://suffered-scored-nicole-default.trycloudflare.com/api/icons/upload`. Anonymous uploads are attributed to
`system`; an optional login attributes approval, disapproval, and other actions
to a named reviewer.
Enter its name and optional category (defaults to `manual_upload`). Every upload
receives the `uploaded` icon type, including those with a custom category.
The canvas selects the family automatically
(32 = sub, 48 = solo, 64 = container); the server checks that it matches.
Choose **Upload to Ready**, then **Review uploaded icon** to approve or disapprove it.
Uploads remain outside the approved library until approved.

The optional JSON boolean `bypass_validation` defaults to `true`. Set it to
`false` to run rendered SVG hole-and-pinch checks before saving. Failures return
422 with a validation report and save nothing; checker errors return 503.
SVG safety, canvas, and rendering checks always run. These SVG checks do not
replace authored-geometry validation (grid, keyshape, vector spacing, symmetry).

New uploads and their original SVGs are stored in the feedback database, so gallery
rebuilds and server restarts preserve them. Back up the database along with the
existing artwork folders. These are SVG-only icons: use Manual Edit for revisions;
Python generation and browser primitive editing require authored Python geometry.

### Fix an existing icon

Open its inspector and choose **Fix with AI** / **Generate fixed variant**.
Describe the requested change. The job receives the existing Python source and
family and creates a new variant. Review and accept it in the same way as a new
icon. The original remains available, with its own review history.

### What executes behind the Generate button

The server creates a job under
`icon_set/data/generation-jobs/<job-id>/` by default. It copies the drawing
runtime, contracts, scripts, and skills into an isolated `workspace/`, prepares
the prompt, and runs `icon_set/scripts/run_icon_agent.sh` there.

The agent reads the icon-making and family skills and must produce exactly one
new public Python icon module plus a root `candidate.json` identifying it.
Changes to existing candidate-workspace files are rejected by the acceptance
workflow. A successful candidate build is required before the preview is offered.

**Add to grid** copies the new module into the real library without overwriting
an existing module, then builds its family. An acceptance build failure rolls
back the newly added source file. **Discard** removes the candidate workspace
and preview while retaining a small job record and log.

Run one server process per repository. Its job lock allows one generation or
acceptance build at a time; avoid an external build during acceptance. A server
restart marks interrupted running/accepting jobs as failed.

## Execute generation from the terminal

### Submit to the running app with authentication

The generation API supports system actions without login. This example optionally
identifies a reviewer using `curl` and a
temporary cookie file. Start the app first; submitting the job starts a Codex
run under the server account.

```bash
ICON_APP_URL=http://127.0.0.1:8000
ICON_COOKIE_FILE=$(mktemp)

curl --fail-with-body --silent --show-error \
  --cookie-jar "$ICON_COOKIE_FILE" \
  -H 'Content-Type: application/json' \
  --data '{"username":"jakes","password":"1"}' \
  "$ICON_APP_URL/api/auth/login"

curl --fail-with-body --silent --show-error \
  --cookie "$ICON_COOKIE_FILE" \
  -H 'Content-Type: application/json' \
  --data '{"mode":"generate","name":"Watering can","family":"solo","prompt":"A watering can in side view with one curved handle and a short angled spout.","model":""}' \
  "$ICON_APP_URL/api/generation"

rm -f "$ICON_COOKIE_FILE"
```

The response includes the job `id`. Log in through the browser and open
`http://127.0.0.1:8000/gallery/generate.html#job-JOB_ID`, replacing `JOB_ID` with
that value, to inspect and accept/discard it. API submission does not approve or
automatically accept the candidate.

For a fix request, use `"mode":"fix"` and include the current `icon` key
(`family/icon-id`) and `svg_sha256`, alongside `name`, `family`, `prompt`, and
`model`. The current gallery entries are in `/gallery/icons.json`. A stale hash
is rejected; using the inspector's fix form handles these fields for you.

### Submission helper

The repository also has this shorter wrapper:

```bash
bash icon_set/scripts/run_icon_agent.sh generate \
  --name "Watering can" --family solo \
  --prompt "A watering can in side view"
```

Its `generate` and `fix` modes delegate to `submit_generation.py`. That script
sends no login cookie, so its requests are attributed to `system`.
Use the optional cookie-based example above to attribute requests to a reviewer.

### Low-level agent execution

For an already prepared candidate workspace and prompt file:

```bash
bash icon_set/scripts/run_icon_agent.sh /path/to/candidate-workspace /path/to/prompt.txt

# Optional model and attached PNG references; an empty model uses the default.
bash icon_set/scripts/run_icon_agent.sh /path/to/candidate-workspace /path/to/prompt.txt "" /path/to/reference.png
```

This runs `codex -a never exec --sandbox workspace-write --skip-git-repo-check`
with the supplied workspace and prompt. It does not create an app job or provide
the app's acceptance workflow. Use a separate candidate workspace and follow the
request/output format in `icon_set/scripts/templates/generate_icon_prompt.md`
or `fix_icon_prompt.md`.

## Author an icon in Python

Read the [symbol language reference](symbol-language.md) when planning an icon's
construction. It describes typed shapes, symbol grouping, repetition, symmetry,
and attachment nodes—the relationships to preserve when placing geometry on the
grid.

You can draw directly without an AI run. Put a new public `.py` file in the
correct family folder and subclass that family's base. Registry discovery is
automatic; there is no manual registration list. Icon IDs must be unique across
the library, and a filename beginning with `_` is not discovered.

For a minimal construction example, save this as
`icon_set/model/icons/solo/readme_demo_square.py`. It is a geometry tutorial;
choose the appropriate family for the actual subject you intend to ship.

```python
from ...keyshapes import Keyshape
from ._base import Solo48


class ReadmeDemoSquare(Solo48):
    icon_id = "readme-demo-square"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"

    def build(self) -> None:
        self.add_polyline(
            "outline",
            (6, 6), (42, 6), (42, 42), (6, 42),
            closed=True,
        )
```

The SOLO48 square keyshape has visible bounds `(4, 4)–(44, 44)`. A 4-unit stroke
extends 2 units on each side of a centerline, so the points above produce that
exact envelope.

Validate only, without exporting a release:

```bash
python3 - <<'PY'
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon

icon = create("readme-demo-square")
print(icon.validate_icon().describe())  # Vector checks only.
qa = inspect_icon(icon)                # Full vector and rendered QA.
print("Full QA:", qa["status"])
for message in qa["errors"] + qa["warnings"]:
    print(message)
raise SystemExit(0 if qa["status"] == "pass" else 1)
PY
```

Then build that source file:

```bash
python3 icon_set/scripts/build.py \
  --icon icon_set/model/icons/solo/readme_demo_square.py --debug
```

Direct calls such as `icon.export_icon_to(...)` and
`icon.export_json_graph(...)` are useful for drafts. They are not substitutes
for the build release gate; JSON graph export explicitly supports unfinished
drawings.

For skill-guided drawing, use `$icon-making` in Codex or `/icon-making` in Claude,
with a name, description, and any reference paths. The router selects
`icon-sub`, `icon-solo`, `icon-avatar`, or `icon-container`.

To scaffold a separate variant of an existing icon before editing:

```bash
python3 icon_set/scripts/create_variant.py \
  --icon square --family sub --label "Softer corners"
```

Edit the new file printed by the command and build it. The scaffold copies the
source; it does not make the requested visual change itself.

## Build and export commands

```bash
# Incremental build: new/changed icons; reuse unchanged previous results.
python3 icon_set/scripts/build.py

# Recheck everything after validator, contract, renderer, or rule changes.
python3 icon_set/scripts/build.py --all

# One family; add --all to force every icon in that family to be rechecked.
python3 icon_set/scripts/build.py --family solo

# One Python file; --icon takes a file path, not an icon ID.
python3 icon_set/scripts/build.py --icon icon_set/model/icons/sub/shapes.py

# Full check with debugging images and HTML evidence.
python3 icon_set/scripts/build.py --all --debug

# Validate the entire Python library and save evidence, without publishing.
python3 icon_set/scripts/validate_library.py --debug

# Skip preview PNG output and saved QA artifacts; checks still run.
python3 icon_set/scripts/build.py --no-png --no-debug --no-report
```

`--family` and `--icon` can be repeated. A source file can contain several icon
classes, so a file selection may check more than one icon. Other icons in a
targeted build retain their last results without being rechecked; its exit code
covers the selected icons. A family-filtered QA report can also include other
families as context, which do not determine that build's exit code.

| Output | Default location |
| --- | --- |
| SVGs and family manifests | `icon_set/.local/dist/sub32/`, `solo48/`, `container64/` |
| PNG previews | `icon_set/.local/previews-png/<family><canvas>/` |
| Web app assets and icon catalog | `icon_set/.local/dist/gallery/` |
| Failed SVGs and findings | `icon_set/.local/dist/failed/<family><canvas>/` |
| QA HTML and measurements | `icon_set/.local/dist/qa/` |

Build exit codes are **0** for no selected failures, **1** for selected icons
that fail or remain unresolved, and **2** for argument/selection errors such as
a source file with no registered icon. Unexpected runtime errors may also stop
the process; read its diagnostic output.

A normal build publishes passing icons even when others fail. A family with no
usable exports after failures keeps its previous release. Outputs are staged
and replaced by directory, with rollback for publication I/O errors; the whole
set of directories is not one crash-atomic transaction. A failed build does not
mean that every previously exported file has remained unchanged.

## How validation works

Validation has two layers: an ordered vector/model check, followed by rendered
and sampled QA. The main implementations are
`icon_set/validation/validator.py` and `icon_set/validation/library_qa.py`.
Only a full QA result of `pass` is automatically eligible for publication.
Explicit human artwork choices are described separately below.

### 1. The contracts define the rules

The executable rules are loaded from `icon_set/model/contracts/`:

| Contract | Defines |
| --- | --- |
| `icon-profile.v1.json` | Family/profile binding, canvas, stroke, grid, MIC, tolerances |
| `keyshapes.v1.json` | Resolved keyshape dimensions and bounds |
| `negative-space.v1.json` | Hole size, pinch depth, raster sampling, small-circle exception |
| `composition-templates.v1.json` | Supported composition structures and placements |
| `exceptions.v1.json` | Per-icon FREE keyshape declarations and approval records |
| `spacing-reviews.v1.json` | Explicit visual decisions for exact sampled spacing findings |

The shared style is a **4-unit stroke**, round caps and joins, `currentColor`,
and no fill. Authored endpoints lie on a 1-unit integer grid; arc radii must be
positive integers. The runtime also supports Bézier geometry, with structural
checks for its data.

MIC means **minimum ink clearance**, measured between distinct parts:

| Profile | Minimum ink gap | Corresponding equal-width centerline distance |
| --- | --- | --- |
| `SUB32` | 2 units | 6 units |
| `SOLO48` | 4 units | 8 units |
| `CONTAINER64` | 2 units | 6 units |

For two 4-unit strokes, `ink gap = centerline distance − 4`. For example, two
separate SOLO48 strokes whose centerlines are 7 units apart leave only 3 units
of white space and fail the 4-unit requirement. MIC is not a margin to the canvas.

### 2. Eight ordered vector checks

`icon.validate_icon()` runs these checks in order. Later checks generally still
run after a failure, except when invalid structure makes measurement unsafe.

| Stage | What it verifies |
| --- | --- |
| `schema/profile` | Valid identity, family/profile binding, nonempty geometry, supported structures, unique IDs, valid references, and FREE exception metadata. Each primitive belongs to exactly one emitted path. |
| `style/grid` | Fixed stroke/cap/join/grid settings, integer endpoints, valid arc radii, and supported primitive types. |
| `canvas/keyshape bounds` | Actual painted ink stays inside the canvas and fits the selected envelope. Curved extrema and stroke thickness count. |
| `mic` | Clearance between emitted parts, plus exact SOLO48 parallel straight-edge checks inside contours. Ambiguous or uncertified contacts require review. |
| `keyshape` | Runtime dimensions and bounds agree with the locked keyshape contract. |
| `composition` | Supported composition class, allowed output profile, semantic roles, and child placement/constraints. |
| `svg round-trip` | Parsing the exported SVG recovers the expected canvas, canonical style, path IDs, and path data. |
| `reproducibility` | Rendering the same model again produces the identical SVG string. |

Rectangle-family keyshapes require **exact visible bounds**, with design
tolerance 0. A numerical epsilon of `1e-9` absorbs floating-point arithmetic
noise. Circle keyshapes use radial containment, with the ink reaching to within
0.5 units of the target radius. Merely matching a circle's bounding box is not
enough. FREE requires matching bounds, rationale, and an approved per-icon
exception for release.

SOLO48 authoring choices are circle 44×44, square 40×40, landscape rectangles
44×36 or 44×32, and portrait rectangles 36×44 or 32×44, centered on the 48 canvas.

An intentional contact can be declared with a scoped `connect` relationship.
It exempts the relevant pair in the inter-path check, not every gap in the icon.
Composition child ownership prevents rechecking a child's internal parts against
the wrong profile; clearance between different participants still matters.

The exact SOLO48 within-contour check measures parallel straight edges over a
positive overlap, excluding adjacent segments and shared endpoints. Those edges
still need 8 units between centerlines / 4 units between ink edges.

### 3. Symmetry check

Full QA renders the ink and compares horizontal and vertical reflections about
the painted-bounds midpoint. An axis with at least **98% ink overlap** triggers
a centerline comparison on that axis.

The centerline tolerance is **0.0001 units**, the curve chord error limit is
**0.00001 units**, and maximum sample spacing is **0.25 units**. A mismatch
fails QA even if the icon looks almost symmetric. An icon with no likely mirror
axis is not automatically rejected. This is a numerical diagnostic; diagonal
symmetry is outside its scope.

Run a separate symmetry report with an icon ID or a family:

```bash
python3 icon_set/scripts/check_symmetry.py --icon square
python3 icon_set/scripts/check_symmetry.py --family solo
```

The default report is `work/symmetry-check/index.html`, with `results.json`
beside it. Exit codes: 0 for no mismatches, 1 for a mismatch, 2 for input/checker
errors. These commands do not edit icons.

### 4. Sampled internal-spacing review

Full QA also searches for sustained opposing edges within connected geometry.
It samples at intervals up to **0.25 units**, looks for near-parallel opposing
runs at least **2 units** long, and compares their ink gap with the profile MIC.
It excludes adjacent segments, shared endpoints, endpoint neighborhoods, and
complete circular contours, which have separate hole checks.

These findings are approximate review evidence, not certified geometric
failures. **In the current implementation, unresolved findings set
`needs_review = true` and change an otherwise passing result to `review`, which
blocks automatic publication.** The diagnostic's `blocking: false` flag does
not mean unresolved findings can ship: `publication_requires_clear_review` and
`library_qa.inspect_icon()` enforce the review gate.

An explicit visual decision in `spacing-reviews.v1.json` can retain specific
findings. It must match the icon, SVG hash, rules hash, and element pairs and
include a reviewer and reason. All findings must be accounted for to obtain
`internal_spacing.status = "reviewed"`. Changes invalidate stale decisions.
This does not waive exact MIC, symmetry, or hole/pinch checks.

### 5. Rendered holes and pinches

Full QA uses CairoSVG and image analysis to measure enclosed negative space.
The contract sets a minimum authored hole radius of **1 unit** (diameter 2),
solid fill/closure depth of **1 unit**, and **32 raster samples per design unit**.

The hole measurement also renders a thinner, 1-unit measuring stroke. Reducing
the authored 4-unit stroke retreats each edge by `(4 − 1) / 2 = 1.5` units.
Consequently the measuring-mask minimum radius is `1 + 1.5 = 2.5` units, or
diameter 5. Reports retain both the measured diameter and the equivalent
authored-stroke diameter; these numbers describe the same rule at two widths.

The actual 4-unit authored ink is checked as well, because thinning can merge
tiny pockets into larger holes. Pinches are checked on that authored ink at the
full configured 1-unit closure depth. Background labeling connects neighboring
pixels across edges and corners. Potential single-sample artifacts are checked
again at a finer resolution rather than being silently treated as valid holes.

Complete circular contours with **centerline diameters exactly 4 or 6 units**
have an explicit hole-size exception. With stroke 4, these correspond to visible
diameters of **8 or 10 units**. The raw findings remain recorded. Other shapes,
sizes, and circles split by extra strokes do not qualify; spacing and pinch
checks still apply.

These are raster measurements, so inspect near-threshold findings visually.
Missing dependencies or processing failures become checker errors, not an
empty-hole pass.

### 6. Interpret the result and inspect evidence

| Result | Meaning and effect |
| --- | --- |
| Vector `valid` | Ordered vector checks passed; rendered QA is still required. |
| Vector `invalid` | At least one vector error was found. |
| Full QA `pass` | Eligible for automatic build export; gallery approval remains separate. |
| Full QA `fail` | A blocking geometric or rendered rule failed. |
| Full QA `review` | A measurement or spacing finding remains unresolved; automatic export is blocked. |
| Full QA `error` | The checker could not finish; automatic export is blocked. |

The default HTML report is `icon_set/.local/dist/qa/index.html`, available from the
running server at [QA report](http://127.0.0.1:8000/qa/index.html). Per-icon
folders such as `qa/solo/<icon-id>/` contain `metrics.json` and SVG evidence.
With `--debug`, they also contain spacing, internal-spacing, and hole overlays.
Findings name affected elements, coordinates, distances, and relevant thresholds.

The summary `results.json` references result shards under `results/`; it is not
the complete flat list. For programmatic access, call
`icon_set.validation.library_qa.load_results(Path("icon_set/.local/dist/qa"))`.
SVG and rule hashes identify the drawing and measurements represented by a row.

`--debug` controls debug artifacts; `--report` controls HTML reporting. Neither
disables validation. `--no-png` skips export previews, not the raster QA engine.
Disabling both debug and reporting leaves the previous saved QA snapshot
untouched, so check its hashes before treating it as evidence of a new run.

If matching external `qa_overlays.py` results exist in
`icon_set/work/qa_overlays/<family><canvas>/`, their saved distance/hole failures
also gate publication of that exact SVG. Use `--qa-overlays DIR` to select a
different results folder.

## Edit validation and manual artwork

In the icon inspector, **Editing → Browser Edit** supports moving/resizing
strokes, point edits, deletion, keyshape selection, and automatic fitting.
**Run validation** sends the current draft to the server and uses the same
vector, spacing, symmetry, and hole/pinch checks as full build QA.

Changing geometry or keyshape invalidates the previous result. Saving reruns
the server checks and records a JSON handoff. Saving a draft does not itself
publish the edited SVG: choose **Pick → Browser Edit → Display selected version**
to adopt an acceptable saved snapshot.

**Force pass (human reviewed)** requires a reason and a server save. The saved
override records the reviewer, time, source SVG hash, and exact edited graph
hash. Its effective result can be `pass` while the original automatic errors
remain visible. Changing the geometry/keyshape clears the override. This is a
human acceptance of that version, separate from gallery approval.

**Manual Edit** accepts an SVG edited in a design tool. Picking it records a
human source selection. The upload must pass SVG format, canvas, static-content,
and rendering checks; arbitrary uploaded outlines are not treated as having
passed Python primitive validation. Their build status is `human-selected` and
automatic primitive validation is `not-run`.

The persisted source choices are `use_org` (Python original), `use_edited`
(selected browser snapshot), and `use_upload` (selected external SVG). Builds
honor these choices and retain original generated metadata. No upload rewrites
the authored Python module.

## Files, storage, and deployment

The authoritative [development workflow](docs/development-workflow.md) covers
source ownership, daily commands, releases, rollback, and migration.

| Location | Ownership |
| --- | --- |
| `icon_set/model/icons/` | Agent-authored Python originals, tracked in Git |
| `icon_set/metadata/` | Optional curated source metadata, tracked in Git |
| `icon_set/.local/dist/` | Generated development gallery, ignored by Git |
| `icon_set/.local/previews-png/` | Generated PNG previews, ignored by Git |
| `icon_set/.local/state/` | Development-only database, uploads, edits and jobs |
| `icon_set/data/` | Preserved legacy state and supporting datasets |
| External release directory | Explicit production asset snapshot |
| External state directory | Production database and manual artwork |

```bash
python3 -m icon_set doctor
python3 -m icon_set build --no-png
python3 -m icon_set dev --open

# On the deployment machine, choose a new external release directory.
python3 -m icon_set release /srv/pictographic/releases/release-001
python3 -m icon_set production \
  --dist /srv/pictographic/releases/release-001 \
  --database /srv/pictographic/state/feedback.sqlite3 \
  --host 0.0.0.0 --port 8000
```

Default builds use Python originals, do not seed source metadata, and do not
refresh role datasets in place. The production server overlays its saved manual
choices at request time. Export does not copy the development database. For an
update or rollback, change the release path and retain the production state path.

The legacy `icon_set/dist/` and `icon_set/assets/previews-png/` trees are no longer
tracked, but their local files remain available. This migration stages one-time
removals from Git; it does not delete the files. Curated metadata and Python
sources remain tracked. Normal future builds produce no generated Git changes.

Existing installations must migrate their complete saved runtime state before
switching to production mode; see the step-by-step guide. No live production
state is moved automatically. A fresh development server uses `.local/state`,
so old uploads or reviews must be inspected using explicit old paths or migrated
intentionally. Historical work reports may still link to legacy output; active
maintenance scripts and generated authoring skills use the new paths.

Use `watch_deploy.py --branch icon-lib --release-root /srv/pictographic/releases
--database /srv/pictographic/state/feedback.sqlite3 --host 0.0.0.0` for automatic
background builds and publication after a push. It starts the existing gallery
first, then switches completed icon updates without restarting the server. Failed
updates preserve the previous gallery. See
[automatic deployment setup](docs/development-workflow.md#automatic-production-releases-after-a-push)
for state migration and service configuration. The legacy watcher mode with
arguments after `--` still updates code only.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Missing CairoSVG/NumPy/OpenCV/Pillow or a checker `error` | Activate the intended environment and install `requirements-qa.txt`. If CairoSVG reports a missing native Cairo library, install the platform's Cairo runtime too. |
| Codex executable not found | Install/sign in under the server account; check its PATH or set `CODEX_BIN` before starting the server. |
| HTTP 401 on login | Check the supplied reviewer credentials. Pipeline API calls without a session are attributed to `system`. |
| Server cannot find gallery assets | Run `build.py` and check that server/build `--dist` values agree. |
| Port 8000 is already in use | Run `deploy.py --port 8001 --open`, and use that port in API commands. |
| An edited Python icon does not appear | Check its family folder, public filename, unique ID, and Failed build findings; build its file explicitly. |
| A rule change seems ignored | Run `build.py --all`; incremental builds reuse previous icon results. |
| A result says `review` with no hard errors | Read its warnings and internal-spacing findings. Unresolved review is not an automatic pass. |
| Generated icon is missing from Final icons | Acceptance adds it as Ready. Approve the current SVG version separately. |
| Python changes do not change the displayed SVG | Inspect the saved artwork choice; a selected upload or browser snapshot survives rebuilds. |
| Editor save returns 409 | Refresh the icon/version and reconcile the newer saved revision before saving again. |
| Generation says another job/build is running | Wait for it to finish; avoid simultaneous server processes/builds in one repository. |

## Tests and further documentation

Run the Python test suite from the repository root with the QA dependencies
installed:

```bash
python3 -m unittest discover -s icon_set/tests -t .
```

Useful inspection and maintenance commands:

```bash
python3 icon_set/scripts/profile_lab.py show
python3 icon_set/scripts/build.py --help
python3 icon_set/scripts/deploy.py --help
python3 icon_set/scripts/validate_library.py --help
python3 icon_set/scripts/generate_skills.py
```

The last command regenerates skill copies from their sources/contracts. Edit
the sources identified in a skill's header instead of hand-editing a generated
copy.

- [Detailed icon-system reference](icon_set/README.md)
- [Folder and script map](icon_set/STRUCTURE.md)
- [Generation implementation notes](icon_set/GENERATION.md)
- [Symbol language: shapes, grouping, symmetry, and connections](symbol-language.md)
- [Shared drawing techniques](icon_set/skills/icon-design/SKILL.md)
- [Hole and pinch measurement provenance](icon_set/validation/PROVENANCE.md)

This quick start follows the current implementation. Some older reference
sections describe internal spacing as nonblocking or show unauthenticated shell
submission; use the current review gate and authenticated workflow above.
