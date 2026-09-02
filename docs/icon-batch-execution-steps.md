# SVG Batch Adapter

Use this adapter when an explicit set of SVG references is remade in one
execution. Follow the shared stages, commands, type-support limits, QA order, and
repair loop in [icon-pipeline.md](icon-pipeline.md). This page adds batch staging,
whole-batch atom decisions, checkpointing, and family review.

Use [icon-execution-steps.md](icon-execution-steps.md) for one selected SVG and
[icon-rework-execution-steps.md](icon-rework-execution-steps.md) for a
symbol-library rework JSON.

## Why the batch lane is different

Batching adds three legitimate cross-icon operations:

- consolidate atom requests before composition;
- integrate each shared atom once for all call sites;
- review finished icons together for family consistency.

It does not authorize using one icon's source geometry to reinterpret another.

## Batch boundary

- Stage only the explicitly selected SVGs into one clean `sources/` folder. That
  folder is the entire evidence scope.
- Do not stage a whole category, wildcard, or unreviewed source folder.
- No two staged files may share a base subject name. Put `Foo - variant 1` and
  `Foo - variant 2` in different batches.
- Derive each icon's mapping only from its own source, detection JSON, and plot.
- Cross-icon comparison is allowed only during the atom-consolidation gate and
  final family review.
- Record `iconType` per icon. Keep QA inputs separated by type/canvas; do not mix
  design and ship outputs or different profiles in one checker invocation.

## Lane sequence

```text
stage explicit sources
→ batch detection and triage
→ map every icon without composing
→ consolidate and integrate atoms once
→ compose in groups of five through the canonical pipeline
→ family review
→ batch delivery
```

Do not begin composition until every batch mapping and the whole-batch
quality-first reuse-or-extend review are complete.

## 1. Stage the explicit source list

Run from the repository root. Record a batch ID and copy one deliberately selected
file at a time:

```bash
BATCH=batch-01
mkdir -p "work/$BATCH/sources"
cp "test_input/Building - variant 1.svg" "work/$BATCH/sources/"
cp "test_input/Architecture Fence - variant 1.svg" "work/$BATCH/sources/"
```

Check for base-name collisions before detection:

```bash
ls "work/$BATCH/sources" \
  | sed -E 's/ - variant [0-9]+\.svg$//' \
  | sort \
  | uniq -d
```

Any output is a collision. Remove the duplicate from this batch and process it in
a later execution. Keep original source files unchanged.

## 2. Detect the staged folder

```bash
python3 core/batch_detect_svg_shapes.py \
  "work/$BATCH/sources" \
  "work/$BATCH/detection"
```

The detector writes one `*-shapes.json` and `*-preflight.png` per source plus
`batch-summary.json`. Re-running reuses existing reports; pass `--overwrite` only
when a source or detector changed, and record why regeneration was necessary.

## 3. Triage before mapping

Read `batch-summary.json` first:

```bash
python3 - "work/$BATCH/detection/batch-summary.json" <<'PY'
import json, sys
summary = json.load(open(sys.argv[1]))
print(summary['svgCount'], 'sources ·', summary['readyCount'], 'ready ·',
      summary['reviewRequiredCount'], 'review ·', summary['failedCount'], 'failed')
for row in summary['files']:
    if row['status'] != 'ready':
        print('review:', row['source'])
for row in summary['failures']:
    print('FAILED:', row['source'], row['error'])
PY
```

Use this inspection depth:

| Status | Required review |
| --- | --- |
| `ready`, no `specIssues` | Rendered source; consult the plot whenever topology remains ambiguous |
| `review-required` | Rendered source, preflight plot, and direct measurement of source path data |
| `failed` | Resolve the detector failure or omit the icon and report it; never guess |

`ready` means the detector was confident, not that the design decision is
automatic.

## 4. Phase 1 — map the entire batch

Apply the evidence-review and mapping stage from
[icon-pipeline.md](icon-pipeline.md) to every icon before composing any of them.
Write each mapping directly into that icon's editable source under
`sourceAnalysis`; do not keep one scratch mapping and reconstruct provenance later.

Maintain one batch request list:

```text
work/$BATCH/atom-requests.md
```

Each `new-atom` entry records:

- icon and source element IDs;
- contour described in words;
- why existing atoms fail visual-quality, natural-silhouette, topology,
  shape-family, or semantic-role tests;
- proposed generic parametric contract and required size range.

No icon is composed in this phase. Composing easy icons first biases later atom
design toward geometry that already exists.

## 5. Phase 2 — consolidate and integrate atoms

Resolve `atom-requests.md` as one quality-first review:

1. Deduplicate differently worded requests for the same contour.
2. Re-test each survivor against the current catalog.
3. Design one contract against every call site and size range.
4. Integrate registry, renderer/validator, generated asset, detector support when
   reliable, documentation, and tests.
5. Render each new atom at small, normal, wide, and tall sizes before use.

```bash
python3 core/generate_assets.py
python3 -m unittest discover -s core -p 'test_*.py'
```

A high new-atom rate is a review signal, not a quota or stop condition. Re-read
the mappings to remove duplicates, frozen traces, and whole-icon atoms, but retain
every generic parametric atom that materially improves visual quality. Never
force catalog reuse merely to lower the ratio. A newly added atom remains subject
to the same quality and overfitting tests for later icons.

## 6. Phase 3 — compose in checkpointed groups

Work in groups of five. For each icon, enter the canonical pipeline at “Compose
editable JSON” and continue through its profile-aware emission and QA gates.

The emitter and structural validator infer each profile from editable JSON. Use
explicit JSON paths rather than bare icon names:

```bash
for name in icon-a icon-b icon-c icon-d icon-e; do
  python3 core/emit_icon.py \
    "work/$BATCH/editable/$name.json" \
    --out-dir "work/$BATCH/output"
  python3 core/validate_icon.py \
    "work/$BATCH/editable/$name.json" \
    --dir "work/$BATCH/output"
done
```

Then run the remaining grid, overlap, declared-keyshape, hole/pinch, and true-size
stages in the order defined by [icon-pipeline.md](icon-pipeline.md). Pass the
matching `--icon-type` to profile-selected QA commands. Container structural
validation checks its slot and full 32×32 clear region; retain filled-preview visual
evidence as the combined-use review.

Checkpoint after each group. Do not carry an unresolved failure into the next
group.

## 7. Validate the completed batch

Point each profile's design grid gate only at its `-design.svg` files; the output
folder also contains ship files. For a normal-only group:

```bash
python3 core/check_svg_grid.py \
  "work/$BATCH"/output/*-design.svg \
  --icon-type normal \
  --expected design \
  --output-dir "work/$BATCH/qa/grid"
```

Run the per-icon overlap, declared keyshape, and hole/pinch commands from the
canonical pipeline. Read each report rather than relying only on exit status.
After any repair, edit the atomic JSON, re-emit, and rerun all affected gates,
including declared keyshape containment.

For every icon confirm:

- each essential detector element has a resolved decision;
- source topology is preserved or the simplification is documented;
- identity-bearing openings have recorded passing painted clearance;
- no atom was overfit to a different shape family;
- every required automated gate passes for the declared profile;
- the icon and its openings remain recognizable at true ship size.

## 8. Perform family review

Generate one sheet of all finished ship icons at true size and inspect a second
magnified view of the same raster decisions:

```bash
python3 core/render_svg_contact_sheet.py \
  "work/$BATCH/output" \
  "work/$BATCH/qa/family-contact-sheet.png" \
  --true-size 24 --preview-scale 4 --columns 10
```

Use a ship-only folder if `output/` also contains design SVGs. The example is
for a normal family. Use `--true-size 16` for a separately reviewed sub family
and `--true-size 32` for a separately reviewed container family; do not mix
profiles on one sheet.

Review:

- consistent optical weight;
- one treatment for shared motifs unless a difference is intentional;
- consistent gap rhythm, stance, and margin discipline;
- no near-duplicate icons within the batch;
- no individually valid icon that reads as a family outlier.

Revise outliers through editable JSON and rerun their gates before refreshing the
sheet.

## 9. Deliver the batch

Per icon, deliver the artifacts required by [icon-pipeline.md](icon-pipeline.md).
Per batch, deliver one `batch-notes.md` containing:

- batch ID and exact source list;
- type and triage status per icon;
- every new atom, contract, and call site;
- registry, asset, documentation, and test changes;
- per-icon decisions, simplifications, omissions, exceptions, and blocked gates;
- group checkpoint results and family-review findings.

Also include `batch-summary.json` and the family contact sheets. The batch is
complete only when every delivered icon traces source element → maker decision →
atom instance → SVG → QA, and the family review is complete. End after this batch.

## Stop conditions

Stop the affected icon and report it when:

- a staged source and detection report do not correspond;
- detection failed and cannot be regenerated;
- the staged folder contains an undeclared SVG or base-name collision;
- an essential feature remains unexplained;
- a required atom needs prohibited geometry or encodes a whole icon;
- the output location or a required type-aware gate is unavailable;
- a user decision would materially change the subject.

Do not stop solely because many icons need new atoms. Apply the generic parametric
atom contract to each request, continue safe work, and list every real omission,
its stopping step, and reason.
