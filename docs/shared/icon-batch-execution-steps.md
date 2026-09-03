# SVG Batch Adapter

Use this adapter when an explicit set of SVG references is remade in one
execution. Follow the shared stages, commands, type-support limits, QA order, and
repair loop in [icon-pipeline.md](icon-pipeline.md). This page adds batch staging,
shared construction review, checkpointing, and family review.

Use [icon-execution-steps.md](icon-execution-steps.md) for one selected SVG and
[normal-icon rework](../icons/rework.md) for a
local manifest pack or symbol-library rework JSON.

## Why the batch lane is different

Batching adds three legitimate cross-icon operations:

- identify recurring construction motifs without changing the individual briefs;
- compare relevant reference examples and record intentional family decisions;
- review finished icons together for family consistency.

It does not authorize using one icon's source geometry to reinterpret another.

## Batch boundary

- Stage only the explicitly selected SVGs into one clean `sources/` folder. That
  folder is the entire evidence scope.
- Do not stage a whole category, wildcard, or unreviewed source folder.
- No two staged files may share a base subject name. Put `Foo - variant 1` and
  `Foo - variant 2` in different batches.
- Derive each icon's mapping only from its own source, detection JSON, and plot.
- Cross-icon comparison may inform motif consistency and family review, but
  cannot replace an individual icon's meaning. The bundled Lucide corpus is
  an additional style/construction reference, not part of the subject input set.
- Record `iconType` per icon. Keep QA inputs separated by type/canvas; do not mix
  duplicate canonical/compatibility aliases or different profiles in one checker invocation.

## Lane sequence

```text
stage explicit sources
→ batch detection and triage
→ map source meaning and inspect relevant original/debug reference pairs
→ record common construction principles where useful
→ compose exact elements in checkpointed groups through the canonical pipeline
→ family review
→ batch delivery
```

Resolve each icon's brief, source mapping and material review questions before
composing it. An unresolved icon does not prevent safe work on other batch items.

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

## 4. Map source meaning and reference choices

Apply the evidence-review and mapping stage from
[icon-pipeline.md](icon-pipeline.md) to each icon before composing it.
Write each mapping directly into that icon's editable source under
`sourceAnalysis`; do not keep one scratch mapping and reconstruct provenance later.

Search relevant Lucide subjects and construction families as described in
[the geometry guide](atomic-shapes.md). Inspect original/debug pairs and exact
geometry. Store per-icon `sourceAnalysis.lucideReferences` with names, reasons
and applied principles. Neither a reference's subject nor another batch icon
may introduce a feature absent from this icon's brief.

## 5. Review common construction principles

Use `batch-notes.md` to record useful shared decisions, such as corner treatment,
enclosure proportions, tangent joins or the clearance around attached modifiers.
Preserve differences needed for recognition. Do not maintain atom requests,
extend registries, regenerate shape assets, or set a target number of elements.
The current source geometry remains directly editable even when a contour is
used only once.

## 6. Compose in checkpointed groups

Choose a manageable checkpoint group. For each icon, enter the canonical pipeline at “Compose
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
validation checks its configured slot and full protected clear region; retain filled-preview visual
evidence as the combined-use review.

Checkpoint after each group. Do not carry an unresolved failure into the next
group.

## 7. Validate the completed batch

Point each profile's grid gate at one file per icon. The same-size `-design.svg`
alias can be selected conveniently when the folder also contains canonical SVGs;
this is not a second-size check. For a normal-only group:

```bash
python3 core/check_svg_grid.py \
  "work/$BATCH"/output/*-design.svg \
  --icon-type normal \
  --expected design \
  --output-dir "work/$BATCH/qa/grid"
```

Run the per-icon overlap, declared keyshape, and hole/pinch commands from the
canonical pipeline. Read each report rather than relying only on exit status.
After any repair, edit the version-2 geometry JSON, re-emit, and rerun all affected gates,
including declared keyshape containment.

For every icon confirm:

- each essential detector element has a resolved decision;
- intended subject topology is preserved; any simplification or reconstruction
  of an [extraction-clearance artifact](icon-rules.md#extracted-prototypes-restore-missing-geometry)
  is documented;
- identity-bearing openings have recorded passing painted clearance;
- no borrowed motif was forced into an inappropriate shape family;
- every required automated gate passes for the declared profile;
- the icon and its openings remain recognizable at native size.

## 8. Perform family review

Generate one sheet of all finished native icons, with each icon shown at its
native dimensions. Do not produce a second magnified or reduced review export:

```bash
python3 core/render_svg_contact_sheet.py \
  "work/$BATCH/output" \
  "work/$BATCH/qa/family-contact-sheet.png" \
  --icon-type normal --preview-scale 1 --columns 10
```

Use a canonical-only folder or the tool's alias filtering to avoid duplicate
`-design.svg` images. The example uses configured `normal` dimensions. Use
`--icon-type sub`, `--icon-type container`, or a custom configured name for its
respective family; do not mix profiles on one sheet. Optional `--true-size`
must equal the selected profile's native size. Manual zoom can aid diagnosis,
but the acceptance verdict remains at native dimensions.

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
- selected reference examples and shared construction principles;
- per-icon decisions, simplifications, omissions, exceptions, and blocked gates;
- group checkpoint results and family-review findings.

Also include `batch-summary.json` and the family contact sheets. The batch is
complete only when every delivered icon traces source element → maker decision →
editable element → SVG → QA, and the family review is complete. End after this batch.

## Stop conditions

Stop the affected icon and report it when:

- a staged source and detection report do not correspond;
- detection failed and cannot be regenerated;
- the staged folder contains an undeclared SVG or base-name collision;
- an essential feature remains unexplained;
- an essential form cannot be represented safely by the supported geometry schema;
- the output location or a required type-aware gate is unavailable;
- a user decision would materially change the subject.

Continue safe work on unaffected items and list every real omission, its stopping
step and reason. Scope does not expand beyond this batch.
