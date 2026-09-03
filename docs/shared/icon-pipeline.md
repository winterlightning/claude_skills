# Canonical Icon Pipeline

This document is the single operational sequence for making, checking, repairing,
and delivering Unlimited Shapes icons. The lane adapters link here and describe
only what changes for their input:

- [icon-execution-steps.md](icon-execution-steps.md) — one supplied SVG.
- [icon-batch-execution-steps.md](icon-batch-execution-steps.md) — a staged SVG batch.
- [Normal-icon rework](../icons/rework.md) — a local manifest pack or a symbol-library payload; remote upload is separately authorized.

## Authority

Use these documents in this order:

1. Start with the selected type's skill, local `rules.md`, and generated
   `profile.md`: [normal](../icons/SKILL.md), [sub](../sub-icons/SKILL.md), or
   [container](../container-icons/SKILL.md). These are role/workflow templates,
   not an enumeration of allowed sizes. For a custom named type, use this shared
   pipeline and the [profile configuration guide](profile-configuration.md).
   `core/icon_profiles.json` supplies current geometry and validation settings.
2. [icon-rules.md](icon-rules.md) defines the shared visual and geometry requirements.
3. [atomic-shapes.md](atomic-shapes.md) defines schema-version-2 geometry and
   on-demand Lucide reference use.
4. This page defines execution order and repair loops.
5. The selected lane adapter adds scope, staging, review, and delivery differences.

[icon-authoring-guide.md](icon-authoring-guide.md),
[qa-overlays-guide.md](qa-overlays-guide.md), and
[negative-space-repair-examples.md](negative-space-repair-examples.md) explain
technique and interpretation. They do not replace the three normative documents
above. An installed skill may help execute the work, but it does not override the
in-repository specification.

`core/icon_profiles.json` schema v2 is the machine authority for canvas, stroke,
keyshapes, validation defaults/overrides, inheritance, and container-slot values.
Centers and same-size design/ship compatibility aliases are derived. The Profile Manager,
emitter, validators, generated profile references, and tests consume that source. Update the
affected type's `rules.md` when a profile change also alters its purpose or
delivery contract. [icon-types.md](icon-types.md) is the routing guide.

Check its generated Markdown profile references with:

```bash
python3 core/generate_profile_assets.py --check
```

After an authorized direct profile edit, run the command without `--check` to
regenerate mirrors, then run the check form. The [profile manager](profile-configuration.md)
validates and regenerates mirrors when it saves. Neither route migrates icons;
configuration changes require fresh emission, QA, and native-size acceptance.

See [scripts.md](scripts.md) for the exhaustive command, module, exit-behavior,
and type-support matrix.

## Profile support

Declare the type first. The canonical emitter and validators use the selected
profile throughout the pipeline.

| Type | Numeric profile | Automated path | Additional review and delivery |
| --- | --- | --- | --- |
| `normal` | [Normal profile](../icons/profile.md) | Profile-aware emission, structural, grid, overlap, keyshape, and hole/pinch QA | [Normal rules](../icons/rules.md) |
| `sub` | [Sub profile](../sub-icons/profile.md) | The same core path using the sub profile | [Sub rules](../sub-icons/rules.md) |
| `container` | [Container profile](../container-icons/profile.md) | The same outer gates plus declared slot and clearance validation | [Empty and filled review](../container-icons/rules.md#filled-preview) |

Authoring, canonical output, and acceptance review use the same resolved native
canvas and stroke. Built-in defaults are normal/main 48px, sub 32px, and container
64px at 4px stroke, but custom profiles and edited values are valid. A container
preview uses its configured outer canvas and translates a separately authored
accepted-profile insert into the slot without scaling.

## Workflow map

```mermaid
flowchart LR
    A[Choose input lane and icon type] --> B[Resolve source SVG and detect geometry]
    B --> C[Review evidence and map source elements]
    C --> D[Choose the strongest natural silhouette]
    D --> E[Inspect relevant original and debug references]
    E --> H[Compose exact editable elements]
    H --> I[Emit native-size SVG]
    I --> J[Structural validation]
    J --> K[Grid gate]
    K --> L[Overlap review]
    L --> M[Native canvas and declared keyshape gate]
    M --> N[Hole and pinch gate]
    N --> O[True-size visual review]
    O --> P{Looks good and all required gates pass?}
    P -- No --> Q[Repair editable geometry]
    Q --> D
    P -- Yes --> R[Deliver]
    R --> S[Rework lane only: dry-run, approval, upload]
```

The required order is:

```text
route → resolve source → detect → map → inspect relevant references → compose exact elements → emit → structural
→ grid → overlap → native canvas/keyshape → holes/pinches → true-size review → deliver
```

`validate_icon.py` includes some spacing and keyshape checks. Treat those as an
early structural baseline; the grid gate still blocks the later rendered overlap,
keyshape, and negative-space acceptance gates.

## Suggested artifact layout

Keep source evidence, editable composition, emitted output, and QA separate:

```text
work/<job>/
├── sources/
├── detection/
│   ├── <name>-shapes.json
│   └── <name>-preflight.png
├── editable/
│   └── <name>.json
├── output/
│   ├── <name>.svg          # canonical native SVG
│   └── <name>-design.svg   # same-size compatibility alias
└── qa/
    ├── grid/
    ├── overlap/
    ├── keyshape/
    ├── holes/
    └── previews/
```

Run commands from the repository root. Install the Python dependencies before
using the raster QA tools:

```bash
python3 -m pip install -r requirements.txt
```

## 0. Route the request

Choose exactly one input lane:

| Input | Adapter | Intake script |
| --- | --- | --- |
| Subject or short description without an SVG | Selected type's skill and the brief-only intake below | none |
| One selected SVG | [single-icon adapter](icon-execution-steps.md) | none |
| Explicit staged set of SVGs | [batch adapter](icon-batch-execution-steps.md) | none |
| Symbol rework JSON | [rework adapter](../icons/rework.md) | `core/fetch_rework_batch.py` |
| Local manifest-based rework pack | [local pack lane](../icons/rework.md#local-manifest-pack-lane) | `core/rework_pack.py inspect`, then `prepare` |

Then declare exactly one `iconType` per editable icon. Select its keyshape from
the resolved profile's keyshapes (built-in `profile.md` or generated aggregate)
by visually inspecting the dominant whole-icon
silhouette at its native size. A small wheel, button, window,
badge, or inset does not choose the whole icon's keyshape.

### Brief-only intake

When the user supplies a subject without an SVG, record the description and its
required cues. Create a preliminary `sources/<name>.svg` on the selected design
profile to establish subject, part count, and arrangement. This is an authored
draft, not an external reference or final composition. Follow shared geometry
and paint conventions without adding details absent from the request.

Record `sourceOrigin: "brief"` and the user description under `sourceAnalysis`,
then detect and map the draft using the same stages below. For several requested
subjects, create one draft per subject and use the batch adapter after staging.
The symbol-library rework adapter adds its own brief-compliance and upload
contract only when the input is an actual rework payload.

## 1. Detect the source before composition

For one SVG:

```bash
python3 core/detect_svg_shapes.py <source.svg> \
  --output <detection>/<name>-shapes.json \
  --plot <detection>/<name>-preflight.png
```

For an authorized batch:

```bash
python3 core/batch_detect_svg_shapes.py <sources-folder> <detection-folder>
```

Use `--strict` for automated single-file preflight when manual review must produce
a nonzero status. Use `--overwrite` for batch detection only when a source or the
detector changed. Detection is evidence, not permission to trace or an automatic
geometry decision. Legacy suggested atoms are conveniences; ignore them whenever they would
weaken the natural silhouette, recognition, or visual quality.

The detector normalizes source analysis to its reference grid. Those coordinates
are evidence; compose on the selected profile's configured native canvas.
Detection does not convert a sub or container into a normal icon.

## 2. Review evidence and map the source

Inspect the source rendering, detection JSON, and preflight plot together. Review:

- `summary.readyForIconMaker` or the batch status.
- Every source element ID.
- `makerPreflight.suggestedAtoms` and `makerPreflight.manualReview`.
- Every `specIssues` warning or error.
- Foreground/background order, connections, openings, overlaps, and contour ends.

Before treating a gap or truncated part as a design feature, apply the
[extracted-prototype rule](icon-rules.md#extracted-prototypes-restore-missing-geometry).
Distinguish clearance left by a removed overlapping object from intentional
openings or overlaps still needed in the new composition. Plan reconstruction
of the complete intended form; do not copy the extraction artifact into the
standalone result. Keep the source SVG unchanged as evidence.

For every identity-bearing element or semantic group, record one mapping decision:

- `rebuild` into exact editable geometry
- `preserve` a source form that already fits the brief and current profile
- `simplify`
- `omit`
- `merge`
- `manual`

Carry the detector IDs and reasons into `sourceAnalysis.mappings`. Also record
`sourceAnalysis.relationships` for `connected`, `ordinary-distinct`,
`visual-opening`, and `intentional-overlap` pairs. Each identity-bearing opening
needs a `spacingChecks` entry with the measured centerline distance, painted
clearance, minimum, and pass/fail result.

For a reconstructed region, use `rebuild` on the affected element or semantic
group and explain the missing geometry, evidence for its continuation, and
restoration. The reconstruction is a source-mapping decision, not an extra
feature or a QA waiver. Review the restored contour at native size as well as
running the normal geometry and spacing gates.

Use stable element IDs in version-2 relationship pairs, including
`spacingChecks[].elements: ["element-a", "element-b"]`. The older
`instances` pair field is only for compatibility with legacy documents.

Do not compose while an essential feature or unresolved detector warning remains
unexplained. `sourceAnalysis.incomplete: true` is an explicit validation failure;
do not use it as a delivery waiver.

## 3. Select references and construction principles

Choose the cleanest recognizable form from the brief and source evidence.
Search for a relevant Lucide subject or construction family, then inspect the
original/debug pair and its exact geometry:

```bash
python3 core/lucide_reference.py search 'cloud' --limit 6
python3 core/lucide_reference.py inspect cloud --json
```

Record `sourceAnalysis.lucideReferences` entries with `name`, `reason` and
`principles`. Useful principles describe contour flow, corner construction,
relative proportions, gaps, or attachments—not merely “looks like Lucide.”
If there is no relevant match, say so and build from the semantic brief.

Lucide's original 24px SVG canvas stays unchanged as reference evidence, not
as a production or acceptance-review target for this system. Debug segment boundaries
are generated analysis, not a required output structure or proof of design
intent. References cannot add features absent from the brief. Whole-unit grid
preferences and aggregate frequency summaries are guidance, not a strict angle,
radius, element-count or reuse quota. New geometry needs no registry extension
or shape-asset generation. See [the geometry guide](atomic-shapes.md).

## 4. Compose editable JSON

The schema-version-2 editable JSON is the source of truth for repair and re-emission. It
must declare at least:

- a stable kebab-case `name`;
- `iconType`, `canvas`, and `strokeWidth`;
- `keyfitCheck.targetToken` plus a short visual rationale;
- `schemaVersion: 2` and ordered `elements` with unique `id`, optional `role`,
  supported `tag`, and geometry-only `attrs`;
- `sourceAnalysis` mappings, relationships, and spacing checks;
- `containerSlot` for a container.

Render and inspect the composition at its declared native size before finalizing
the keyshape. Fit by recomposing editable coordinates.
Never globally scale or patch flattened output paths.

Exact edge/cardinal contact is the default keyfit mode. Intrinsically thin/sparse
subjects may declare `keyfitCheck.mode: "optical"`, a meaningful `rationale`, and
design-unit `paintedBounds: [left, top, right, bottom]`. Validate measured bounds
against that declaration and token containment; do not distort a natural glyph
or waive overflow to achieve fit. See shared R1 for this reviewed exception.

Author and repair the editable JSON directly. Before validation, complete
`sourceAnalysis` with the source mapping, relationship, painted-clearance, and
visual-rationale evidence required by this pipeline. Unfinished analysis remains
marked `sourceAnalysis.incomplete: true` and is not ready for delivery.

## 5. Emit canonical outputs

For every profile:

```bash
python3 core/emit_icon.py <editable-icon.json> --out-dir <output-folder>
```

The emitter reads `iconType` from editable JSON and writes canonical `<name>.svg`
at that configured native canvas and stroke, with 1u = 1px. `<name>-design.svg` remains a same-size compatibility alias,
not a second resolution; internal `design`/`ship` names and checker selectors
also resolve to identical dimensions. Do not produce half-size outputs.
Omitted `iconType` uses configured `defaultIconType` (initially `normal`) only
for backward compatibility; new sources declare it explicitly.

For a container's additional [filled preview](../container-icons/rules.md#filled-preview),
use the [preview manifest format](../container-icons/rules.md#preview-manifest)
to reference the separately authored container and sub sources:

```bash
python3 core/compose_container_preview.py <preview-manifest.json> \
  --out-dir <qa-folder>/previews
```

Do not replace the editable empty-container source with the combined preview.

## 6. Run structural validation

For every profile:

```bash
python3 core/validate_icon.py <editable-icon.json> --dir <output-folder>
```

Fix the editable JSON and re-emit when this fails. Never patch only one emitted
SVG. The validator resolves the editable source's configured `iconType`, including
custom names.
For a container it also requires the exact slot metadata and rejects container
paint whose stroke enters the protected region in its profile. Run that
gate on the empty production container, not the deliberately filled review
preview.

## 7. Pass the grid gate

Run the gate on canonical native SVGs (or their same-size compatibility aliases)
for one profile:

```bash
python3 core/check_svg_grid.py <native-svg-or-native-folder> \
  --icon-type <profile-name> \
  --expected design \
  --output-dir <qa-folder>/grid
```

The `--expected design` selector is retained for compatibility; it now means the
same native canvas and stroke as `ship`. Avoid duplicate canonical/alias rows in
one run. Stop on a wrong canvas, wrong normalized stroke, unsafe geometry attributes, or unresolved
fractional-placement findings. Intentional cubics and non-default radii are
allowed; apply documented optical/grid exceptions where required. Correct the editable source,
re-emit, and rerun; do not blindly round flattened paths.

One invocation uses one profile. Separate mixed-type batches before running this
gate.

## 8. Review declared overlaps and spacing

For each editable icon with two-element spacing checks:

```bash
python3 core/render_overlap_audit.py \
  <editable-icon.json> <qa-folder>/overlap/<name>-overlap-audit.svg
```

Inspect every generated panel. The command visualizes transformed paths and
envelopes using dense centerline sampling plus stroke radius rather than an exact
Boolean stroke outline; it does not make the final visual decision for you. If the
source has no two-element spacing checks, “nothing to audit” is expected rather
than proof of a failure.

## 9. Validate the declared painted keyshape

`validate_icon_keyshapes.py` is a mandatory, completion-blocking gate for every
production SVG, including its same-size `-design.svg` alias. It verifies native
`width`, `height`, and `viewBox`, the configured stroke, the declared painted
keyshape, and the protected slot when the selected profile has one. Canvas and
keyshape values come from `core/icon_profiles.json`, including custom profiles;
neither canvas size nor a convenient matching token is inferred from the artwork.

For one native SVG, bind its editable source explicitly:

```bash
python3 core/validate_icon_keyshapes.py <native.svg> \
  --editable <editable-icon.json> \
  --icon-type <profile-name> \
  --output-dir <qa-folder>/keyshape
```

For both emitted aliases or a flat output folder:

```bash
python3 core/validate_icon_keyshapes.py <native-svg-folder> \
  --expected-editable-dir <editable-folder> \
  --output-dir <qa-folder>/keyshape
```

Editable metadata is required: schema version 2, explicit `iconType`, `canvas`,
`strokeWidth`, and `keyfitCheck.targetToken`. With `--expected-editable-dir`, both
`<name>.svg` and `<name>-design.svg` use `<name>.json`. Use `--editable` for one
renamed delivery such as `<sid>_generated.svg`; its filename need not match the
editable name. An optional `--icon-type` must agree with the editable declaration.

The gate uses `check_keyfit.py` internally for stroke-inclusive raster bounds,
canvas overflow, circle containment, and exact or declared optical fit. Do not
run that same raster check a second time by default or use its diagnostic
threshold overrides to bypass this gate. Unsupported SVG styling, transforms,
hidden definitions, or references fail: repair the editable source and emit the
canonical flat SVG rather than approximating or ignoring those features.

Inspect the fresh `canvas-keyshape-results.json` and every expected row, plus the
per-input `canvas-keyshape.json`, `.keyfit.json`, and `_keyfit.png` under
`files/<stem>-<pathhash>-<runid>/`. Require exit `0`, `ok: true`, no failed rows, and complete
coverage of the intended outputs; a missing or stale output/report is not a pass.
Exit `1` includes validation, read, and dependency failures; `2` is CLI misuse.
The checker does not modify SVGs, editable sources, or profiles.

Run this gate on the empty production container. Its deliberately filled preview
is a separate combined-use review artifact, not a replacement production input.
A pass here does not replace structural, grid, spacing/overlap, hole/pinch, or
native-size visual acceptance.

## 10. Pass the hole and pinch gate

For a clean native SVG:

```bash
python3 core/qa_overlays.py <ship.svg> \
  --icon-type <profile-name> \
  --output-dir <qa-folder>/holes
```

Read `hole-diameters.json`, the per-icon metrics, the overlay, and the HTML report.
The report status is the verdict; process exit status alone is not proof of a pass.
Omit threshold overrides so the profile's configured radius and fill-depth gates
apply. Treat explicit relaxed CLI values as diagnostics, not delivery acceptance.
Use one declared profile per invocation so measurements normalize to the correct
design canvas.

## 11. Perform true-size visual review

Numeric success does not prove recognition, balance, or family consistency.
Inspect the canonical SVG at the selected profile's native size only. For a flat
family folder, create a native-size contact sheet:

```bash
python3 core/render_svg_contact_sheet.py <native-svg-folder> <contact-sheet.png> \
  --icon-type <profile-name> --preview-scale 1 --columns 10
```

The type selects its native size; optional `--true-size` must match that value.
Use one profile per sheet and exclude duplicate compatibility aliases. Follow the
type's rules for additional review states, including a container-native filled
preview. Manual zoom and internal raster supersampling may diagnose
geometry; they do not create another required export or replace native review.

An older half-size verdict does not establish native-size acceptance. For an
explicitly requested migration, emit and actually review the new native SVG,
then record fresh size/hash evidence; changing metadata alone is not a review.
Canvas, stroke, keyshape, or validation changes likewise require new emission,
QA and review, even when the rendered bytes happen to stay unchanged. Do not
rebuild historical work folders merely because profile rules changed.

Reject an awkward, unnatural, or weakly recognizable silhouette even when every
numeric gate passes. Return to the semantic brief, reference evidence and exact
editable geometry when the construction caused the compromise. Do not increase
element count as a proxy for visual improvement.

## Repair loop

Any geometry change returns to editable JSON and then to emission. Work down the
R9 repair ladder:

1. Enlarge the opening.
2. Rebalance the composition so the crowded detail can carry legal space.
3. Remove a complete non-identity-bearing part and record the omission.

Never squeeze a hole shut, delete an arbitrary path fragment, or clip the defect.
Do not change the declared profile or keyshape, switch to optical mode, or relax
validation settings merely to obtain a pass. Fit the intended form by repairing
editable geometry; a real semantic or profile change needs its own justification
and any required user decision.

Repeat **validate → repair editable geometry → regenerate both native SVG aliases
→ rerun all affected gates** until the expected outputs pass. After each repair,
rerun structural, grid, overlap, `validate_icon_keyshapes.py`, hole/pinch, and
true-size checks. A local repair moves paint and can break a previously passing
outer gate. Do not mark the icon complete while a required output or fresh report
is missing, stale, or failing. If satisfying the gates would require guessing
about the subject or changing the authorized scope, report the blocker instead.

## Delivery gate

Deliver only when every required gate passes. The handoff includes:

- schema-version-2 editable JSON;
- canonical `<name>.svg` at the declared native size; any retained `-design.svg`
  is a same-size compatibility alias, not another required delivery resolution;
- source detection JSON and preflight plot when a source SVG existed;
- mapping, relationship, spacing, and keyshape rationale metadata;
- grid, overlap, fresh native canvas/keyshape results covering both emitted
  aliases, negative-space, and true-size evidence;
- intentional simplifications, omissions, approved exceptions, and blocked gates;
- container slot metadata and filled preview when applicable;
- selected Lucide references and applied construction principles, or an explicit
  note that no useful match was found.

The trace must remain readable from brief/source element → maker decision → editable
element → emitted SVG → QA evidence. Rework uploads happen only after this gate
and the additional approval sequence in the rework adapter.

## Stop instead of guessing

Stop the affected icon and report the blocker when:

- source evidence and detection artifacts do not correspond;
- a required source, report, or output location is unavailable;
- an essential form cannot be represented safely by the supported geometry schema;
- a semantic decision would materially change the intended subject;
- a required checker or dependency is unavailable;
- the output cannot be traced back to editable geometry source.

For a batch, continue safe work on unaffected icons and list every omission with
its stopping step and reason.
