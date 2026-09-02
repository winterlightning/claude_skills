# Unlimited Shapes Icon Documentation

Start with the rules, choose one input lane, and follow one shared pipeline. The
documentation is organized so numeric rules are defined once and the runbooks do
not repeat them.

## Source-of-truth order

1. [Icon types](icon-types.md) — choose `normal`, `sub`, or `container` and read
   its purpose and delivery contract. Exact profile geometry comes from
   `core/icon_profiles.json` and its generated reference.
2. [Icon style rules](icon-rules.md) — binding visual and numeric rules, R1–R9.
3. [Atomic shapes](atomic-shapes.md) — reusable primitive contract and catalog;
   the current catalog never outranks visual quality.
4. [Canonical icon pipeline](icon-pipeline.md) — the only shared execution and
   repair sequence, with the script attached to each gate.
5. One lane adapter:
   - [one supplied SVG](icon-execution-steps.md);
   - [an explicit SVG batch](icon-batch-execution-steps.md);
   - [a symbol-library rework JSON](icon-rework-execution-steps.md).

An installed agent skill can help perform the workflow, but it does not override
the in-repository specification above.

## Pipeline at a glance

```text
Input lane → type → detection → evidence mapping
→ quality-first reuse-or-extend decision → editable JSON
→ emit → structural → grid → overlap → keyshape → holes/pinches
→ true-size review → deliver → rework-only approved upload
```

Every repair returns to editable JSON, re-emits both SVG sizes, and reruns all
affected downstream gates. See [icon-pipeline.md](icon-pipeline.md) for commands,
artifacts, pass criteria, the repair loop, and the current type-support matrix.

## Choose the input lane

| Request | Use | What the adapter adds |
| --- | --- | --- |
| Exactly one chosen SVG | [Single-icon adapter](icon-execution-steps.md) | Single-file evidence boundary and delivery |
| An explicit set of SVGs | [Batch adapter](icon-batch-execution-steps.md) | Staging, whole-batch reuse-or-extend review, checkpoints, and family review |
| A `kind: "rework"` JSON payload | [Rework adapter](icon-rework-execution-steps.md) | Brief authority, source-priority ladder, concept review, and controlled upload |

Do not turn a single-file request into a sibling scan or a batch request. Do not
turn a staged batch into a category sweep.

## Profile-aware workflow

- `core/icon_profiles.json` is the machine authority for normal, sub, and
  container canvas, stroke, keyshape, and slot data. [Icon types](icon-types.md)
  explains how those profiles are used; generated mirrors feed the browser and
  human-readable profile table.
- The browser editor selects all three profiles and exports a canonical-schema
  editable JSON scaffold. Its explicit `sourceAnalysis.incomplete: true` marker
  must be resolved before `core/validate_icon.py` accepts it; the emitter and
  validator infer the profile from that JSON.
- Grid, painted-keyshape, and hole/pinch QA run against the declared profile, so
  sub icons retain their 32×32 → 16×16 geometry and true-size 16px review.
- Container validation checks the fixed slot metadata and rejects container paint
  entering the full centered 32×32 clearance square. The non-shipping filled
  preview still requires combined visual review at the 32px container ship size.

## Supporting guides

- [Icon authoring guide](icon-authoring-guide.md) — composition technique and
  common visual checks.
- [Script and module inventory](scripts.md) — exhaustive command, input/output,
  exit-behavior, and type-support reference.
- [Core scripts guide](core-scripts-guide.md) — concise workflow overview and
  pointer to the inventory.
- [Hole and pinch QA](qa-overlays-guide.md) — operation and interpretation of the
  rendered negative-space gate.
- [Negative-space repair examples](negative-space-repair-examples.md) — worked R9
  repairs and sizing math.
- [Process one supplied SVG](README-svg-input-processing.md) — portable request
  template for a single SVG using any declared profile.
- [Sub-icon handoff](README-sub-icon-making.md) and
  [container handoff](README-container-icon-making.md) — type-specific request
  templates; the normative type contract remains in [icon-types.md](icon-types.md).

## Repository map

| Path | Role |
| --- | --- |
| `core/` | Python geometry, emission, validation, QA, asset generation, and tests |
| `frontend/` | Profile-aware browser composition aid and generated profile/atom mirrors |
| `assets/shapes/` | Generated standalone atom assets |
| `docs/` | Specifications, canonical pipeline, adapters, and review guides |
| `work/` | Source evidence, editable compositions, output, and QA work products |

Run repository commands from the project root. Keep generated evidence out of the
original source folder, and never edit generated atom assets or flattened final
paths as the source of a repair.
