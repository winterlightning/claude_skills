# Icon Batch Processing Execution Steps

Follow this runbook when a set of SVG references — nominally 20 — is traced,
simplified, and remade as Unlimited Shapes icons in one execution.

Use [icon-execution-steps.md](icon-execution-steps.md) instead when exactly one
icon is selected. The two runbooks share the same specification and the same
per-icon discipline; this one adds a staged scope boundary, a shared skill read,
an atom-consolidation gate, and a family review.

## Why batch

Batching is not only a throughput change. Three things are impossible in a
single-icon execution and become available here:

- **Atom decisions get a wider view.** Seeing that six icons need the same
  contour produces a better parametric contract than inferring it from one.
- **Atom work is paid once.** Registry, renderer, detector, asset, docs, and
  tests are touched one time for the whole batch instead of per icon.
- **Family consistency is reviewable.** Stroke rhythm, optical weight, and
  shared motifs can only be judged with the finished icons side by side.

The token cost of the skill and its references is also paid once rather than
20 times.

## Batch boundary

The single-icon runbook forbids opening sibling variants. That rule is unchanged
here and is enforced physically rather than by instruction:

- Stage the selected sources into one batch folder. **That folder is the entire
  evidence scope.** Do not open any SVG outside it.
- **No two icons in a batch may share a base name.** `Foo - variant 1` and
  `Foo - variant 2` must go in different batches. This is the anti-contamination
  rule the single-icon runbook enforces by fiat.
- Each icon's mapping is derived only from its own source, detection JSON, and
  plot. Do not use another icon in the batch to improve, correct, or reinterpret
  the icon in hand.
- Cross-icon comparison is permitted in exactly two places: the atom
  consolidation gate (Step 6) and the family review (Step 9). Both operate on
  atom contracts and finished output, never on one icon's source geometry.

## Required order

```text
1.  Select and stage the batch
2.  Run batch shape detection on the staged folder only
3.  Triage from batch-summary.json
4.  Load SKILL.md + required references (once for the batch)
5.  Analyse and map every icon           [phase 1 — no composition yet]
6.  Consolidate and integrate new atoms  [phase 2 — gate]
7.  Compose, in checkpointed groups of 5 [phase 3]
8.  Validate every icon
9.  Family consistency review
10. Deliver
```

Do not begin any composition before steps 1–6 are complete for the whole batch.

## Prerequisites

This runbook assumes two scripts exist. Without them the per-icon call count
makes a 20-icon batch unworkable:

| script | role |
| --- | --- |
| `python3 core/emit_icon.py <name>` | resolves an editable source's `instances` through the Python registry and each instance's rigid transform into `-design.svg` (48u) and `.svg` (24px), guaranteeing exact half-scale |
| `python3 core/validate_icon.py <name>` | samples real path centerlines and reports painted clearance per pair, canvas safety, centered keyshape containment, angle discipline, cubic checks, and emitted SVG properties |

Do not hand-roll either one inside an execution. Fix the script instead.

## Step 0 — Work from the project root

```bash
cd /Applications/Workspaces/pictographic/unlimited_shapes
python3 -m pip install -r requirements.txt
```

Keep every selected reference file unchanged. Write detection and icon outputs to
separate folders.

## Step 1 — Select and stage the batch

Record the batch id and the explicit list of source paths. Copy them into a
staged source folder:

```bash
BATCH=batch-01
mkdir -p "work/$BATCH/sources"
cp "test_input/Building - variant 1.svg"        "work/$BATCH/sources/"
cp "test_input/Architecture Fence - variant 1.svg" "work/$BATCH/sources/"
# … one cp per selected icon
```

Then check the batch is legal before going further:

```bash
ls "work/$BATCH/sources" | sed -E 's/ - variant [0-9]+\.svg$//' | sort | uniq -d
```

Any output is a base-name collision. Remove the duplicates from this batch and
process them in a later one.

Do not stage a whole folder, a wildcard, or a category sweep. Every file in the
batch is named deliberately.

## Step 2 — Run batch detection

```bash
python3 core/batch_detect_svg_shapes.py \
  "work/$BATCH/sources" \
  "work/$BATCH/detection"
```

This writes one `*-shapes.json` and one `*-preflight.png` per source, plus
`work/$BATCH/detection/batch-summary.json`.

Re-running reuses existing reports; pass `--overwrite` when a source changed or a
detector change must be reflected. Record any regeneration and why.

## Step 3 — Triage from the batch summary

Read `batch-summary.json` first. It carries per-file `status` plus batch totals.

```bash
python3 - <<'EOF'
import json
s = json.load(open('work/batch-01/detection/batch-summary.json'))
print(s['svgCount'], 'sources ·', s['readyCount'], 'ready ·',
      s['reviewRequiredCount'], 'review ·', s['failedCount'], 'failed')
print('errors', s['errorCount'], '· warnings', s['warningCount'])
for f in s['files']:
    if f['status'] != 'ready':
        print(' review:', f['source'])
for f in s['failures']:
    print(' FAILED:', f['source'], f['error'])
EOF
```

Triage sets the depth of inspection each icon gets in Step 5:

| status | required inspection |
| --- | --- |
| `ready`, no `specIssues` | rendered source at a comparable square size; consult the plot only if the source render is ambiguous |
| `review-required` | rendered source **and** preflight plot **and** direct measurement of the source path data |
| `failed` | resolve or drop from the batch; never guess its geometry |

`review-required` is where remakes actually go wrong. It means the detector could
not name the geometry, so the maker must. Measure the path segments rather than
reading proportions off the plot.

Do not use a lighter inspection than the table requires. A `ready` status means
the detector was confident, not that the topology is obvious.

## Step 4 — Load the icon-making skill (once)

Invoke `$unlimited-shapes-icons`. The installed entrypoint for this workspace is:

```text
/Applications/Workspaces/pictographic/unlimited_shapes/.agents/skills/unlimited-shapes-icons/SKILL.md
```

Read `SKILL.md` completely, then all required references:

```text
references/icon-style-rules.md
references/detection-to-atom-pipeline.md
references/negative-space-and-topology.md
```

Read these once for the batch. Do not re-read them per icon, and do not rely on
memory from an earlier session — the skill is the current source of workflow
instructions.

Also read the current atom registry once, before any mapping:

```bash
grep -n "id: '" frontend/js/shapes.js
```

## Step 5 — Phase 1: analyse and map every icon

For every icon in the batch, and before composing anything:

1. Render the source at a comparable square size and inspect it.
2. Apply the Step 3 inspection depth.
3. Record the source-element mapping — one decision per identity-bearing element
   or semantic group: `existing-atom`, `new-atom`, `simplify`, `omit`, `merge`,
   `manual`.
4. Record `relationships` — connected, ordinary-distinct, visual-opening,
   intentional-overlap.
5. Record `spacingChecks` for every identity-bearing opening: centerline
   distance, painted clearance, minimum, pass/fail.
6. Resolve every `manualReview` element semantically.

Write each icon's mapping into its editable source under `sourceAnalysis` as you
go. Do not batch the mappings into one scratch file and reconstruct them later.

Maintain one running list for the batch:

```text
work/$BATCH/atom-requests.md
```

Each `new-atom` decision appends an entry: icon, source element ids, the contour
described in words, why each existing atom fails the topology / shape-family /
semantic-role test, and the proposed parametric contract.

**No composition happens in this phase.** An icon whose essential feature has no
atom yet cannot be composed, and composing the easy ones first biases the atom
design toward whatever was drawn already.

## Step 6 — Phase 2 gate: consolidate and integrate atoms

Open `work/$BATCH/atom-requests.md` and resolve the whole list at once.

1. **Dedupe.** Several icons frequently describe the same contour in different
   words. Merge them into one request with several call sites.
2. **Re-test each survivor against the catalog.** With the batch view, a request
   that looked essential for one icon is sometimes a `simplify` for all of them.
3. **Design each contract against every call site.** A contract that only fits
   the icon that raised it is an icon component, not an atom. Check it stays
   meaningful across the width/height range all its call sites need.
4. **Integrate once**, per the detection-to-atom pipeline: registry, renderer
   allowlist and geometry, generated asset, detector classification where the
   family is reliably recognisable, documentation and catalog counts, tests.
5. **Verify before use.** Render each new atom at small, normal, wide, and tall
   sizes; confirm it stays in its local box, holds a constant centred stroke, and
   emits no cubic. Run both suites:

```bash
python3 core/generate_assets.py
python3 -m unittest discover -s core -p 'test_*.py'
cd core && python3 -m unittest test_detect_svg_shapes && cd ..
```

**Proliferation check.** If more than about one icon in four is requesting a new
atom, stop and re-read the mappings before integrating anything. That ratio
normally means features are being traced rather than simplified.

Do not create an atom for a feature only one icon needs *and* that icon could
honestly simplify. Do not contort a later icon onto an atom created earlier in
the same batch — an atom you just made is still subject to the overfitting rule.

## Step 7 — Phase 3: compose in checkpointed groups of 5

Work through the batch in groups of five. For each icon apply the active
specification: 48×48 design canvas, 24×24 ship canvas, 1u minor / 4u major
grid, and four centered painted keyshapes: circle Ø44u, square 40×40u,
portrait 36×44u, and landscape 44×36u. The keyshape is the padding boundary;
paint must reach its cardinals or edges and remain inside it. Circle paint may
not enter the corner regions of its 44×44 bounding box. Use a 4u design /
2px ship stroke, `currentColor`, no fill, centred stroke, round caps and joins,
ordinary radii 4u or 8u, straight-line angles in 15° increments, arcs and
quadratics only, minimum 4u centerline distance between ordinary distinct parts
as a collision floor, identity-bearing openings at 4u painted clearance (8u
centerline) and never below 3u (7u centerline), 3u overlap cutout where
separation is required, symmetry for naturally symmetrical subjects.

Prefer whole design units. Prefer **even** design coordinates so every ship
coordinate lands on a whole pixel and each 2px stroke centres on a pixel.

Treat each keyshape as an exact painted padding boundary. All four cardinals or
outer painted edges must match it and no paint may cross it. Do not apply an arbitrary global scale to a completed or
flattened icon. Resize or recompose the source atoms and re-snap ordinary
axis-aligned and 45-degree endpoints to whole design units.

Then emit and validate the group:

```bash
for name in icon-a icon-b icon-c icon-d icon-e; do
  python3 core/emit_icon.py "$name" && python3 core/validate_icon.py "$name"
done
```

**Checkpoint after each group of five.** Inspect the five contact sheets, confirm
every validator run is clean, and confirm the group still matches the style of
the groups before it. Do not carry an unresolved failure into the next group.

## Step 8 — Validate every icon

Before spacing, hole, and keyshape checks, run the batch grid gate on the design
outputs:

```bash
python3 core/check_svg_grid.py <batch-design-folder> \
  --expected design \
  --output-dir <batch-grid-qa-folder>
```

Resolve every failure in the editable atomic composition, re-emit, and rerun the
gate. Do not repair a flattened path by blindly rounding coordinates. A batch
must not mix 24×24 ship canvases into a 48×48 design-output folder.

`validate_icon.py` covers the numeric half: half-scale equivalence, canvas
safety, angle and radius tokens, cubic check, collision floor, declared
connections, painted clearance per declared opening, symmetry.

Numeric validation is necessary and not sufficient. For every icon also inspect
together:

1. Rendered source at a comparable square size.
2. Detection plot, when the icon was `review-required`.
3. The 48u design output.
4. The true-size 24px ship output.

Build one contact sheet per icon so this costs a single image, not four:

```bash
# source 192 · design 192 · ship 48 magnified · ship 24 magnified · ship 24 true size
```

Confirm per icon:

- `check_svg_grid.py` passes the design output.
- Every essential detector element has a resolved mapping.
- Foreground/background order, connections, contour terminations, and openings
  match the rendered source or carry a documented simplification.
- Every identity-bearing opening measures a passing painted clearance; numeric
  collision-floor compliance alone is insufficient.
- `core/qa_overlays.py` reports no undersized hole and no pinched
  junction for the icon. Repair a failing zone with the R9 ladder — enlarge the
  opening, rebalance the composition, or remove a whole part — never by moving
  parts into each other until the gap closes.
- `check_keyfit.py` passes the same declared keyshape after any such repair.
  Enlarging can cross the selected boundary; rebalancing and removing can make
  the artwork miss a required edge or cardinal. Re-measure keyshape before holes.
- No atom was overfit to a different shape family.
- The subject and every opening are recognisable and optically balanced at the
  true 24px size, not only enlarged.

## Step 9 — Family consistency review

This step exists only in the batch runbook. Build one grid of every finished ship
icon at true 24px, and a second grid at 96px, and inspect them together.

Confirm across the batch:

- Optical weight is consistent; no icon reads markedly heavier or lighter.
- Shared motifs are drawn the same way — a railing, a roof, an opening, a base
  should not use three different treatments across the batch without reason.
- Repeated gaps use a consistent rhythm.
- Icons intended as a family share a stance and a margin discipline.
- No two icons in the batch are near-duplicates of each other.

Revise the outliers. A single icon that passes every rule can still be wrong for
the family.

## Step 10 — Deliver

Per icon:

- Editable icon source with `sourceAnalysis` mappings, relationship
  classifications, and `spacingChecks`.
- 48×48 `-design.svg`.
- 24×24 clean ship `.svg`.
- Its detection JSON and preflight plot.

Per batch — one document, not one per icon:

- `batch-notes.md` covering the batch id, the source list, the triage counts,
  every new atom with its contract and call sites, the registry/doc/test changes,
  a per-icon table of decisions and simplifications, and the family review
  findings.
- `batch-summary.json` from detection.
- The family contact grids.

When new atoms were created, also include their IDs, registry implementation,
generated assets, renderer/validator/detector integration, documentation, and
passing tests.

The batch is complete only when every icon can be traced from source element →
maker decision → atom instance → final SVG, and the family review has been done.

End the execution after delivering the batch. Do not continue to another batch
automatically.

## Stop conditions

Stop and report the blocker instead of guessing when:

- A staged source and its detection report do not correspond.
- Detection failed for a source and cannot be regenerated.
- The batch contains a base-name collision that was not caught in Step 1.
- More than about a quarter of the batch is requesting new atoms.
- A necessary atom would require prohibited cubic geometry or would encode a
  whole icon.
- A user decision would materially change a subject or its intended meaning.
- The output location is unavailable.

Stopping applies to the affected icon. Finish the rest of the batch, and report
explicitly which icons were left out and why.
