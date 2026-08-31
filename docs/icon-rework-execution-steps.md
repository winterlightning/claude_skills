# Icon Rework Execution Steps (JSON input)

Follow this runbook when the input is a **symbol-rework JSON** from the symbol
library rather than a folder of SVG files, and the finished icons are posted
back to the library as each symbol's new final.

```bash
curl -sS "https://symlib.pictographic.ai/download-wrong-icons-json?cat=Building+Construction"
```

Use [icon-execution-steps.md](icon-execution-steps.md) when one SVG is handed
over directly, and [icon-batch-execution-steps.md](icon-batch-execution-steps.md)
when a folder of SVG references is staged by hand. This runbook keeps the
specification and the per-icon discipline of both and changes three things: the
brief comes from JSON fields, the source drawing is resolved through a priority
ladder, and the result is uploaded instead of only delivered.

## What is different here

| | SVG runbooks | This runbook |
| --- | --- | --- |
| Input | one or more `.svg` files | one JSON payload, `kind: "rework"` |
| Design brief | the source drawing itself | `concept` + `minimal_description` |
| Source drawing | supplied | resolved: current final → reference → authored from the brief |
| Goal | faithfully simplify the source | **satisfy the brief**; the source is only a starting drawing |
| Output | delivered to a folder | delivered **and** POSTed back as the symbol's final |
| Uploaded file | — | the **48×48 design SVG** (`<name>-design.svg`, 4u stroke) |

### R0 — the brief outranks the source drawing

Every symbol in this payload carries `wrong: true`. The library is saying the
current drawing depicts the wrong thing. The current final is still valuable —
it is already on-spec 48u geometry and often reusable structure — but it is
**not** the statement of what the icon should show.

- `minimal_description` is the authoritative subject and feature budget.
- `concept` is the authoritative name of the thing.
- The staged source SVG is evidence of geometry and craft, never of meaning.
- Where the drawing and the brief disagree, the brief wins, and the disagreement
  is recorded as a mapping decision with a reason.

This inverts the fidelity rule of the SVG runbooks. Do not "faithfully
reproduce" a drawing that was rejected for being unfaithful.

### R1 — judge the current final against the brief before remaking it

`minimal_description` is not only the design brief; it is the **test** the
existing drawing has to be measured against. `wrong: true` is the library's
claim, not a finding you may assume. Before mapping a symbol whose source came
from an existing drawing — `files.final` or `files.prototype` — decide whether
that drawing actually implements the brief, and record the verdict in
`sourceAnalysis.briefCompliance`:

| verdict | meaning | what follows |
| --- | --- | --- |
| `correct` | the drawing shows the brief's subject, carries every required cue, and adds nothing the brief does not authorize | do not redesign it — rebuild it as an editable atomic source, emit, and report the disagreement with the library's `wrong` flag |
| `partial` | the subject is right but a required cue is missing, or the drawing exceeds the feature budget | remake, keeping the parts that already comply |
| `wrong` | the subject is wrong, or the identity-bearing form is absent | remake from the brief |

Record it with evidence, not as a bare label:

```json
"briefCompliance": {
  "verdict": "partial",
  "requiredFeatures": ["rectangular frame", "one panel shifted left",
                       "clear opening on the right", "one small handle"],
  "present":  ["rectangular frame", "clear opening on the right"],
  "missing":  ["one panel shifted left — the frame reads as a single plane"],
  "excess":   ["two chevron marks where the brief authorizes one handle"],
  "reason":   "subject correct, panel offset absent and handle count exceeded"
}
```

`requiredFeatures` is read off the brief, and every entry must land in exactly
one of `present`, `missing`, or `excess`. A verdict without that accounting is
not a verdict.

Two consequences worth stating plainly:

A `correct` verdict on a **prototype** means only that the subject and features
match; the prototype's geometry is still foreign-grid and must be rebuilt from
atoms regardless.

- **A `correct` verdict is a real possible outcome and must be reported, not
  suppressed.** If the library flagged a symbol that already satisfies its brief,
  the useful output is that finding. Reproducing it as a clean editable source is
  still worthwhile — the batch then has a traceable source for it — but do not
  redraw it into something different merely to justify the rework.
- **An `excess` entry is the most common real defect in this payload.** Briefs
  here are explicitly budgeted ("Add only one small handle", "Use one diagonal
  brace as the identifying cue"). A drawing that adds a second cue fails the
  brief even when it is well drawn and passes every numeric gate.

## Fields this process uses

Only these fields drive the work. Everything else in the payload is metadata.

#### Per symbol — required

| Field | Role |
| --- | --- |
| `sid` | identity; keys the staged files and the upload URL |
| `concept` | the subject to draw, and the readable half of the icon name |
| `minimal_description` | **the brief** — subject, required features, and the explicit feature budget ("Add only one small handle") |
| `files.final` | source candidate 1 — the current shipped icon |
| `files.reference_svg`, `references[].path` where `chosen: true` | source candidate 2 — the pictoicon reference |
| `files.prototype` | source candidate 3 — the earlier foreign-grid drawing, used only when 1 and 2 are absent |
| `upload_url` | where the finished design SVG is POSTed |

#### Per symbol — context only, never a feature list

| Field | Why it is not the brief |
| --- | --- |
| `description` | describes the busy original in full detail; read it only to disambiguate the brief, never to add features the brief left out |
| `name`, `icons`, `name_source` | library labels; `concept` is the subject |
| `wrong`, `had_final`, `instances`, `n_icons` | status counters — `wrong` is the library's claim, tested by R1, never assumed |
| `pictoicon_url` | landing page, not a drawing |

#### Batch level

| Field | Role |
| --- | --- |
| `kind` | must be `"rework"`; anything else is a stop condition |
| `label` | batch name and default folder name |
| `symbols`, `count`, `skipped` | the batch scope |
| `api.base`, `api.label` | upload host and the variant label recorded per upload |
| `api.path`, `api.method`, `api.body` | `POST` raw SVG text, UTF-8 — not JSON |

Reading a field outside the required set to decide what to draw is a process
error. `description` in particular describes the drawing being replaced.

## Source priority ladder

Resolve exactly one source drawing per symbol, highest available first:

```text
1. files.final          the current shipped icon        → detect and remake
2. files.reference_svg  the chosen pictoicon            → detect and remake
3. files.prototype      the earlier foreign-grid        → detect and remake,
                        drawing, read with the brief      reading it with the brief
4. none of those        author a draft SVG from the     → detect and remake
                        brief, then treat it as the
                        source like any other
```

Every rung ends in the same place — a drawing in `sources/`, detected, then
remade. What changes down the ladder is how much the drawing can be trusted, and
R0/R1 apply at every rung.

**Rung 3 — the prototype.** It is a foreign-grid drawing: a 26-unit viewBox, a
1.5 stroke, and a literal color rather than `currentColor`. It is also, usually,
the drawing the library already rejected. Use it for what it is good for —
subject, part count, arrangement, which features the icon was trying to show —
and never for geometry, canvas, stroke, or proportion. Normalize it mentally to
the 48u canvas and expect the detector to report `review-required`; that status
is normal here and means measure the path data rather than reading the plot.

Because a prototype is only reached when nothing better exists, read it
**together with** `minimal_description`, never alone. Where they disagree the
brief wins, exactly as in R0, and the disagreement is recorded in
`briefCompliance` as if the prototype were a final.

**Rung 4 — the authored draft.** A real two-step: write
`sources/<icon-name>.svg` from `concept` + `minimal_description` first, then run
it through detection and the normal remake like every other rung. Do not compose
an icon directly from prose — the draft exists so every symbol reaches
composition with the same evidence bundle.

An authored draft is a legible sketch on the 48u canvas, not a finished icon.
Its job is to fix subject, part count, and arrangement so detection and mapping
have something to measure. Mark it `sourceOrigin: "brief"` and say so in the
delivery notes.

`batch.json` records which rung each symbol used as `sourceOrigin`
(`final`, `reference`, `prototype`, or `brief`). Carry that value into
`sourceAnalysis.sourceOrigin`; it is what tells a later reader how much evidence
the icon was actually built from.

## Required order

```text
1.  Fetch and stage the batch
2.  Read the briefs and confirm the field set
3.  Resolve and verify one source per symbol
4.  Run batch shape detection on the staged sources only
5.  Triage from batch-summary.json
6.  Load SKILL.md + required references (once for the batch)
7.  Map every symbol against its brief      [phase 1 — no composition yet]
8.  Consolidate and integrate new atoms     [phase 2 — gate]
9.  Compose, in checkpointed groups of 5    [phase 3]
10. Validate every icon
11. Concept review, then family review
12. Upload: dry run, confirm, POST
13. Deliver
```

Do not begin composition before steps 1–8 are complete for the whole batch.
Do not POST anything before step 12.

## Step 0 — Work from the project root

```bash
cd /Applications/Workspaces/pictographic/claude_skills
python3 -m pip install -r requirements.txt
```

## Step 1 — Fetch and stage the batch

```bash
python3 core/fetch_rework_batch.py --cat "Building Construction"
```

Add `--json sample_response.json` to stage a saved payload instead of fetching,
`--out <folder>` to choose the batch folder, and `--overwrite` to re-download
sources that are already staged. The script fetches the payload, walks the
source ladder for every symbol, and writes:

```text
work/rework-<label>/
├── manifest.json      the payload plus each symbol's `upload` file path
├── batch.json         resolved per-symbol rows: icon name, brief, source origin
├── briefs.md          the human-readable brief sheet
├── upload.py          copied from the project root, ready to run in place
├── sources/           one resolved source SVG per symbol
├── detection/         *-shapes.json, *-preflight.png, batch-summary.json
├── editable/          <icon-name>.json composition sources
├── output/            <icon-name>-design.svg and <icon-name>.svg
└── qa/                grid/, keyshape/, holes/, overlap audits
```

Icon names are `<sid-kebab>-<concept-kebab>` — unique per symbol, kebab-case as
`emit_icon.py` requires, and readable in a folder listing. The staged batch
folder is the **entire evidence scope**. Do not open an SVG outside it, and do
not fetch a second category into the same folder.

The script exits non-zero on an icon-name collision. Resolve it before going
further; two symbols sharing a name would overwrite each other's output and each
other's upload.

## Step 2 — Read the briefs

Read `briefs.md` end to end before any other work. For each symbol confirm:

- The `concept` names a subject you can draw.
- The `minimal_description` states a feature budget, and you can count the parts
  it authorizes. "Add only one small handle" is a limit, not a suggestion.
- The source origin is what you expect.

Note every brief whose feature budget the current source clearly exceeds. Those
are the icons the rework exists for — and note the ones where the current source
already looks compliant, because R1 has to reach a verdict on those too.

## Step 3 — Verify the resolved sources

Open every staged source and confirm it renders as a drawing. Check
`batch.json` → `sourceCounts`, which reports how many symbols came from each
rung. A batch weighted toward `prototype` and `brief` needs more design judgement
than one weighted toward `final`, and its delivery notes should say so.

For any symbol with `sourceOrigin: "brief"`, author `sources/<icon-name>.svg`
now, before detection:

- 48×48 viewBox, `fill="none"`, `stroke="currentColor"`, 4u stroke, round caps
  and joins.
- Only the parts the brief authorizes.
- Lines, arcs, and quadratics — never cubics, at any stage.

Re-run `core/fetch_rework_batch.py` with the same `--out` if a source needs
re-resolving; existing files are kept unless `--overwrite` is passed.

## Step 4 — Run batch detection

```bash
BATCH=work/rework-building-construction
python3 core/batch_detect_svg_shapes.py "$BATCH/sources" "$BATCH/detection"
```

Pass `--overwrite` when a source changed. A source that arrived from `files.final`
is already on-canvas and normally detects clean; that says the geometry is
legible, not that the subject is right.

## Step 5 — Triage from the batch summary

```bash
python3 - <<'EOF'
import json
s = json.load(open('work/rework-building-construction/detection/batch-summary.json'))
print(s['svgCount'], 'sources ·', s['readyCount'], 'ready ·',
      s['reviewRequiredCount'], 'review ·', s['failedCount'], 'failed')
for f in s['files']:
    if f['status'] != 'ready':
        print(' review:', f['source'])
for f in s['failures']:
    print(' FAILED:', f['source'], f['error'])
EOF
```

Triage sets inspection depth exactly as in the batch runbook: `ready` needs the
rendered source; `review-required` needs the rendered source, the preflight plot,
**and** direct measurement of the path data; `failed` must be resolved or the
symbol dropped from the batch and reported.

Reference- and prototype-origin sources arrive on a foreign canvas (1024u
pictoicons and 26u prototypes are both normal) and land in `review-required` more
often. That is expected; measure the path data rather than reading proportions
off the plot.

## Step 6 — Load the icon-making skill (once)

Invoke `$unlimited-shapes-icons` if the skill is installed for this workspace.
When it is not, the in-repo specification is authoritative and must be read
completely before mapping:

```text
docs/icon-rules.md            numbered canonical specification
docs/atomic-shapes.md         the primitive contract
docs/icon-authoring-guide.md  day-to-day authoring reference
docs/qa-overlays-guide.md     hole and pinch QA operation
docs/negative-space-repair-examples.md   worked R9 repairs
docs/core-scripts-guide.md    what each core script checks
```

Read these once for the batch, not once per symbol, and read the current atom
catalog before any mapping:

```bash
grep -n "id: '" frontend/js/shapes.js
```

## Step 7 — Phase 1: map every symbol against its brief

For every symbol, before composing anything:

1. Render the staged source and inspect it at a comparable square size.
2. Apply the Step 5 inspection depth.
3. **Judge the source against the brief (R1).** Read `minimal_description`,
   enumerate the features it requires, and account for every one as `present`,
   `missing`, or `excess` against the staged drawing. Record the resulting
   `briefCompliance` verdict — `correct`, `partial`, or `wrong` — before any
   mapping decision. This judgement is the reason the symbol is in the batch,
   and it determines how much of the existing drawing survives.
4. Record one decision per identity-bearing element or semantic group:
   `existing-atom`, `new-atom`, `simplify`, `omit`, `merge`, `manual`. Excess
   parts the brief does not authorize are `omit`, with the brief quoted as the
   reason.
5. Record `relationships` — connected, ordinary-distinct, visual-opening,
   intentional-overlap.
6. Record `spacingChecks` for every identity-bearing opening: centerline
   distance, painted clearance, minimum, pass/fail.
7. Resolve every `manualReview` element semantically.

Write each symbol's analysis into its editable source under `sourceAnalysis` as
you go, carrying the JSON provenance with it:

```json
{
  "name": "sym-000723-right-hand-sliding-door",
  "canvas": 48,
  "strokeWidth": 4,
  "keyfitCheck": { "targetToken": "square-40" },
  "sourceAnalysis": {
    "sid": "sym_000723",
    "concept": "Right Hand Sliding Door",
    "brief": "An open right-sliding door: a rectangular frame with one panel shifted left, leaving a clear opening on the right. Add only one small handle.",
    "sourceOrigin": "final",
    "sourcePath": "sources/sym-000723-right-hand-sliding-door.svg",
    "briefCompliance": {
      "verdict": "partial",
      "requiredFeatures": ["rectangular frame", "one panel shifted left",
                           "clear opening on the right", "one small handle"],
      "present": ["rectangular frame", "clear opening on the right"],
      "missing": ["one panel shifted left"],
      "excess": ["second chevron mark"],
      "reason": "subject correct, panel offset absent and handle count exceeded"
    },
    "briefDiff": [
      { "briefRequires": "one small handle", "sourceShows": "two chevron marks", "decision": "omit" }
    ],
    "mappings": [],
    "relationships": [],
    "spacingChecks": []
  },
  "instances": []
}
```

Maintain one running `atom-requests.md` for the batch, exactly as in the batch
runbook: icon, source element ids, the contour in words, why each existing atom
fails the topology / shape-family / semantic-role test, and the proposed
parametric contract.

**No composition happens in this phase.**

## Step 8 — Phase 2 gate: consolidate and integrate atoms

Resolve `atom-requests.md` as a whole list: dedupe, re-test each survivor against
the catalog, design each contract against every call site, integrate once
(registry, renderer allowlist and geometry, generated asset, detector
classification where reliable, documentation, tests), then verify before use.

```bash
python3 core/generate_assets.py
python3 -m unittest discover -s core -p 'test_*.py'
```

**Proliferation check.** More than about one symbol in four requesting a new atom
means features are being traced rather than simplified — re-read the briefs
before integrating anything. Briefs in this payload are explicitly minimal; they
should generate fewer atom requests than a raw SVG batch, not more.

## Step 9 — Phase 3: compose in checkpointed groups of 5

Apply the active specification: 48×48 design canvas, 24×24 ship canvas, 1u minor
/ 4u major grid, and four centered painted keyshapes — circle Ø44u (2u cardinal
padding), square 40×40u (4u per side), portrait 36×44u (6u sides / 2u ends),
landscape 44×36u (2u sides / 6u ends). The keyshape is the padding boundary:
paint must reach its cardinals or edges and stay entirely inside it, and circle
paint may not enter the corners of its 44×44 bounding box. Regular stroke 4u
design / 2px ship, `currentColor`, no fill, centered stroke, round caps and
joins, ordinary radii 4u or 8u, straight-line angles in 15° increments, arcs and
quadratics only, 4u centerline collision floor, identity-bearing openings at 4u
painted clearance (8u centerline) and never below 3u (7u centerline), 3u overlap
cutout where separation is required, symmetry for naturally symmetrical subjects.

Prefer whole design units, and prefer **even** ones so every ship coordinate
lands on a whole pixel. Never apply a global scale to a completed or flattened
icon — resize or recompose the atoms and re-snap ordinary axis-aligned and 45°
endpoints to whole units.

Render and inspect the composition at 48u and true-size 24px **before** declaring
the keyshape. A dominant large circular or radial body selects `circle-44`; a
dominant large four-cornered body selects `square-40`; tall selects
`portrait-36x44`; wide selects `landscape-44x36`. Small internal windows,
handles, badges, or insets do not decide it. Save the visualization and record
`keyfitCheck.targetToken` with a one-line visual rationale.

Emit and validate each group of five:

```bash
for name in <five icon names>; do
  python3 core/emit_icon.py "$BATCH/editable/$name.json" --out-dir "$BATCH/output"
  python3 core/validate_icon.py "$BATCH/editable/$name.json" --dir "$BATCH/output"
done
```

Checkpoint after each group. Do not carry an unresolved failure into the next.

## Step 10 — Validate every icon

Run the grid gate on the design outputs first; it blocks everything downstream.

`emit_icon.py` writes both canvases into `output/`, so the design gate must be
pointed at the `-design.svg` files by glob. Handing it the whole folder fails
every 24×24 ship file on canvas grounds and buries the real results:

```bash
python3 core/check_svg_grid.py "$BATCH"/output/*-design.svg \
  --expected design --output-dir "$BATCH/qa/grid"
```

Read the printed per-file lines, not just the command's exit status.

```bash
python3 core/render_overlap_audit.py \
  "$BATCH/editable/<name>.json" "$BATCH/qa/<name>-overlap-audit.svg"
python3 core/check_keyfit.py "$BATCH/output/<name>.svg" \
  --expected-editable-dir "$BATCH/editable" --output-dir "$BATCH/qa/keyshape"
python3 core/qa_overlays.py "$BATCH/output/<name>.svg" \
  --output-dir "$BATCH/qa/holes" --min-radius-design-u 1
```

Do not continue while the grid gate reports a wrong canvas, wrong normalized
stroke, cubic geometry, an off-grid straight angle, or fractional ordinary
axis/45° endpoints. Fix the editable composition and re-emit; never round a
flattened path blindly.

Repair a failing hole or pinch with the R9 ladder — enlarge the opening,
rebalance the composition, or remove a whole part — never by moving parts into
each other until the gap closes. Re-measure keyshape after any repair;
enlarging can cross the boundary and removing can leave a required cardinal
unreached.

Confirm per icon:

- `check_svg_grid.py` passes the design output.
- Every essential detector element has a resolved mapping.
- Every part the brief does not authorize is explicitly `omit`ted, not silently
  carried over from the source.
- Every identity-bearing opening measures a passing painted clearance; numeric
  collision-floor compliance alone is insufficient.
- No atom was overfit to a different shape family.
- `qa_overlays.py` reports no undersized hole and no pinched junction.
- `check_keyfit.py` confirms the declared keyshape after every repair.
- The subject and every opening are recognizable at the true 24px size.

## Step 11 — Concept review, then family review

**Concept review is specific to this runbook and is the acceptance test.** Put
each finished icon beside its `concept` and `minimal_description` and answer two
questions:

1. Reading only the brief, would you draw this icon?
2. Seeing only the icon, would you name it this concept?

A "no" means the rework failed at its actual purpose, however clean the QA is.

Then check each icon against its own R1 verdict:

- `wrong` or `partial` — the output must differ from the staged source in exactly
  the ways `missing` and `excess` named. An output materially identical to a
  source judged `partial` means the verdict was recorded and then ignored.
- `correct` — the output should match the staged source, and the batch notes must
  carry the disagreement with the library's `wrong` flag and the evidence for it.

Every `requiredFeatures` entry must be visible in the finished 24px icon, and
nothing outside that list may appear in it.

Then run the family review from the batch runbook: one true-24px grid and one
96px grid of every finished ship icon, checked for consistent optical weight,
consistently drawn shared motifs, consistent gap rhythm, a shared stance and
margin discipline, and no near-duplicates within the batch.

## Step 12 — Upload

`upload.py` reads `manifest.json` **beside itself**, so run it from inside the
batch folder. `fetch_rework_batch.py` already put both there and already pointed
each symbol's `upload` at its 48×48 design SVG.

Dry run first, always:

```bash
cd "$BATCH"
python3 upload.py --dry-run
```

Confirm the dry run lists exactly the symbols that passed step 11, that every
one resolves to a `-design.svg`, and that the host is the intended one. A `skip`
line means the file is missing — resolve it rather than uploading a partial
batch, unless a symbol was deliberately dropped and is reported as such.

Uploading replaces a live symbol's final in the shared library. **Get explicit
confirmation from the requester before the real run**, and never POST an icon
that has not passed step 11.

```bash
python3 upload.py                      # posts to manifest api.base, label api.label
python3 upload.py --name rework-2      # label this variant differently
python3 upload.py --base https://staging-host
```

Each POST sends raw SVG text as `image/svg+xml; charset=utf-8` to
`/api/v1/symbols/<sid>/final?name=<label>`. Record the printed per-symbol result.
Re-run after fixing failures; the uploader is safe to repeat and skips whatever
is missing.

## Step 13 — Deliver

Per symbol:

- Editable source with `sourceAnalysis` carrying `sid`, `concept`, `brief`,
  `sourceOrigin`, `briefCompliance`, `briefDiff`, mappings, relationships, and
  `spacingChecks`.
- `<icon-name>-design.svg` — the uploaded file.
- `<icon-name>.svg` — the 24×24 ship output.
- Its detection JSON and preflight plot.

Per batch — one document:

- `batch-notes.md`: batch label and category, the symbol list with source origin
  per symbol, triage counts, every new atom with contract and call sites,
  registry/doc/test changes, a per-symbol table of R1 verdicts, brief-diff
  decisions and simplifications, the concept and family review findings, and the
  upload result per `sid`. List every symbol judged `correct` separately — that
  set is a report back to the library about its `wrong` flags.
- `manifest.json`, `batch.json`, `briefs.md`, and `detection/batch-summary.json`.
- The family contact grids.

The batch is complete only when every symbol traces from JSON brief → R1 verdict
→ resolved source → detector element → maker decision → atom instance → design
SVG → upload result, and both reviews have been done.

End the execution after delivering this batch. Do not fetch another category
automatically.

## Stop conditions

Stop and report the blocker instead of guessing when:

- `kind` is not `"rework"`, or the payload has no symbols.
- Two symbols resolve to the same icon name.
- A symbol has no `files.final`, no `files.reference_svg`, no `files.prototype`,
  **and** no `minimal_description` — there is then nothing to draw from.
- A `minimal_description` and its `concept` describe different subjects.
- A `minimal_description` is too vague to enumerate `requiredFeatures` from, so
  R1 cannot reach a verdict and the remake would be a guess.
- Detection failed for a staged source and cannot be regenerated.
- More than about a quarter of the batch is requesting new atoms.
- A necessary atom would require prohibited cubic geometry or would encode a
  whole icon.
- The upload host rejects a symbol, or the dry run shows a host or symbol set
  you did not expect.
- The requester has not confirmed the real upload run.

Stopping applies to the affected symbol. Finish every other symbol in the batch
and report explicitly which ones were left out, at which step, and why.
