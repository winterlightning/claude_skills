# Script and Module Inventory

This is the command contract for the icon pipeline. Use
[icon-pipeline.md](icon-pipeline.md) for execution order, [icon-rules.md](icon-rules.md)
for binding design rules, and [icon-types.md](icon-types.md) for profile values.
Run commands from the repository root unless a row says otherwise.

## Type-support labels

- **Full** — the tool understands that profile and performs its stated job.
- **Generic** — the tool is profile-neutral and can process that type, but does
  not enforce profile policy.
- **Outer only** — it handles a container's ordinary outer artwork but does not
  inspect the protected slot.
- **Input only** — the type is accepted as a referenced component, not emitted
  as the command's primary artifact type.
- **No** — the command is hard-coded to a different profile or workflow.
- **N/A** — type support does not apply to that maintenance task.

`normal` remains the default when editable JSON omits `iconType`. Commands with
an `--icon-type` option must be given the profile of standalone SVG input; when
editable JSON is supplied, its declaration is authoritative.

## Pipeline commands

| Program | Stage and inputs | Outputs or side effects | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`core/detect_svg_shapes.py`](../core/detect_svg_shapes.py) | Detect one reference SVG. Input: `input`; optional `--output`, `--plot`, `--strict`, `--compact`, `--show`. | JSON to stdout or `--output`; optional plot image or interactive window. Does not compose an icon. | `0` analyzed; `3` manual review under `--strict`; `1` analysis/I/O error; `2` usage error. | Generic | Generic | Generic |
| [`core/batch_detect_svg_shapes.py`](../core/batch_detect_svg_shapes.py) | Detect `*.svg` recursively. Inputs: `input_dir output_dir`; optional `--overwrite`, `--progress-every`. | Per-source `-shapes.json` and `-preflight.png`; `batch-summary.json`. Existing results are reused unless overwritten. | `0` with no per-file failures; `1` invalid/empty input or any failed source; `2` usage error. Review-required results alone do not make the command fail. | Generic | Generic | Generic |
| [`core/fetch_rework_batch.py`](../core/fetch_rework_batch.py) | Stage a symbol-library rework payload from exactly one of `--cat`, `--url`, or `--json`; optional `--base`, `--out`, `--overwrite`, `--uploader`. | Fetches/copies one source per symbol; writes `manifest.json`, `batch.json`, `briefs.md`, subfolders, and a batch-local `upload.py`; prunes stale staged source names. | `0` staged; `1` malformed input, fetch/copy error, missing uploader, or name collision; `2` usage error. | Full | No | No |
| [`core/emit_icon.py`](../core/emit_icon.py) | Emit an editable icon JSON; optional `--out-dir`. The document selects the icon profile. | `<name>-design.svg` and exact half-scale `<name>.svg`. Creates the output folder. | `0` emitted; nonzero on invalid JSON, name, profile, geometry, or write error; `2` usage error. | Full | Full | Full |
| [`core/compose_container_preview.py`](../core/compose_container_preview.py) | Compose a non-shipping filled-preview manifest that references one container JSON and one accepted sub-icon JSON; requires `--out-dir`. | Validates both profiles, slot/keyshape compatibility, and half scaling; writes a preview design/ship SVG pair without creating a flattened editable source. | `0` preview pair emitted; nonzero on manifest, profile, keyshape, geometry, or write error; `2` usage error. | No | Full | Full |
| [`core/validate_icon.py`](../core/validate_icon.py) | Structural gate for one editable JSON and its emitted pair; optional `--dir`. | Console findings only; does not mutate the icon. Checks the selected profile, exact canonical emitted parity, keyshape, spacing, and container protected region where applicable. Angle and fractional-grid authority remains in `check_svg_grid.py`. | `0` pass; `1` one or more validation failures or an input error; `2` usage error. | Full | Full | Full |
| [`core/check_svg_grid.py`](../core/check_svg_grid.py) | Grid/canvas/angle gate for SVG files or flat folders. Requires `--output-dir`; accepts `--expected`, `--icon-type`, `--exceptions`, and `--keyfit-results`. | `grid-results.json`, `grid-results.csv`, `grid-report.html`, and copied preview SVGs under `icons/`. | `0` no failing result; `1` any fail; `2` no usable input or option error. A documented fractional review may pass only through a matching hash-locked exception. | Full | Full | Full |
| [`core/render_overlap_audit.py`](../core/render_overlap_audit.py) | Render the two-instance relationships in editable JSON. Inputs: `input [output]`. | One profile-sized, expanded-stroke SVG panel per valid entry in `sourceAnalysis.spacingChecks`. This is review evidence, not an automatic visual verdict. | `0` at least one panel written; `1` no valid two-instance relationship; `2` usage error. A caller should skip it only when no relationship is declared. | Full | Full | Full |
| [`core/check_keyfit.py`](../core/check_keyfit.py) | Raster keyshape gate for ship SVGs or flat folders. Requires `--output-dir`; accepts `--expected-editable-dir`, `--icon-type`, raster sampling, and tolerance options. | Per-icon `.keyfit.json` and `_keyfit.png`; aggregate `keyfit-results.json`, CSV, and HTML. | `0` every processed icon passes; `1` any fail or processing error; `2` missing inputs, missing declared metadata, or option error. | Full | Full | Full |
| [`core/qa_overlays.py`](../core/qa_overlays.py) | Raster hole-and-pinch gate for ship SVGs or flat folders. Requires `--output-dir`; accepts `--icon-type`, `--error-dir`, sampling, radius, and fill-depth options. | Per-icon `.metrics.json` and `_holes.png`; aggregate `hole-diameters.json`, CSV, and HTML; copies failures into `hole_error/` by default. | **Report-driven:** currently exits `0` after a completed run even when a result is `fail`, and warns/skips per-file processing errors. Treat every expected row in `hole-diameters.json` as mandatory and inspect its `status`; `2` is an argument error. | Full | Full | Full |
| [`core/render_svg_contact_sheet.py`](../core/render_svg_contact_sheet.py) | Render a flat SVG folder. Inputs: `input output`; optional `--columns`, `--true-size`, `--preview-scale`. | One labeled PNG contact sheet; creates the output parent. | `0` rendered; `2` empty input or option error; nonzero on render/write failure. | Generic | Generic | Generic |
| [`core/bbox_zones.py`](../core/bbox_zones.py) | Measure painted or centerline bounds for SVG files/folders. Inputs: one or more paths; optional `--no-stroke`, `--json`. | Text or JSON on stdout; no files written. | `0` all collected files parsed, including an empty collection; `1` any per-file parse failure; `2` usage error. | Generic | Generic | Generic |

## Registry, compatibility, and migration commands

| Program | Inputs | Outputs or side effects | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`core/generate_assets.py`](../core/generate_assets.py) | Python shape registry; optional `--out-dir`. | Rewrites one standalone SVG per registered atom in `assets/shapes/` or the requested folder. | `0` generated; nonzero on registry/write error; `2` usage error. | Generic | Generic | Generic |
| [`core/generate_profile_assets.py`](../core/generate_profile_assets.py) | `core/icon_profiles.json`; optional `--frontend`, `--docs`, and read-only `--check`. | Generates the browser profile registry and Markdown profile table. Without `--check`, creates parent folders and rewrites stale mirrors. | `0` mirrors match or were generated; `1` at least one mirror is stale under `--check`; `2` usage error. | Full | Full | Full |
| [`core/compose_examples.py`](../core/compose_examples.py) | Every `assets/icons/*.json`. | Rewrites example design and ship SVGs through the compatibility renderer. | `0` all rendered; `1` no example JSON; propagates a failed child render as nonzero. | Full | No | No |
| [`core/render_icon.py`](../core/render_icon.py) | Legacy editable JSON and optional output filename; accepts compatibility-only `--distance-check`. | Requested 48u SVG plus a `-24.svg` companion. | `0` rendered; nonzero on invalid input/geometry/write error; `2` usage error. | Full | No | Outer only |
| [`core/repair_keyshape_targets.py`](../core/repair_keyshape_targets.py) | Dataset-specific editable-source folder, pre-repair `keyfit-results.json`, and a new output folder. | Reworked editable JSON, 48u and 24px sets, and a hash-locked exception manifest. It contains named overrides for one historical migration. | `0` completed; nonzero on missing/inconsistent data or geometry. It may write into an existing output tree, so use a new folder. | Full | No | No |
| [`core/restore_grid_outputs.py`](../core/restore_grid_outputs.py) | Historical flat SVG inventory; requires `--output-dir`; optional `--project-root`, `--overwrite`. | Re-emits a fixed historical normal-icon set from known editable-source locations; writes design, ship, editable, repair manifest, and grid exceptions. `--overwrite` removes the existing target first. | `0` completed; `2` existing target without `--overwrite`; nonzero on missing source or emission error. | Full | No | No |

Do not use the compatibility renderer or either migration command as a substitute
for the canonical emitter and validators.

## Shared modules and data

These are imported by commands; they are not standalone CLIs.

| Path | Input and output contract | Import/failure behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- |
| [`core/icon_profiles.json`](../core/icon_profiles.json) | Machine-readable source for canvas, stroke, center, keyshape, distinct-part distance, inheritance, and container-slot values. | No process exit. Malformed data makes `icon_profiles.py` fail at import. | Full | Full | Full |
| [`core/icon_profiles.py`](../core/icon_profiles.py) | Resolves profile inheritance and validates editable profile declarations, token lookup, and container-slot metadata. Returns detached profile/token structures. | No CLI. Raises `ValueError` for unknown/inconsistent profiles or invalid declarations. | Full | Full | Full |
| [`core/shape_registry.py`](../core/shape_registry.py) | Maps atom IDs and requested boxes to primitive/path geometry. | No CLI. Importers receive `SHAPES` and `BY_ID`; invalid requests raise. | Generic | Generic | Generic |
| [`core/icon_geometry.py`](../core/icon_geometry.py) | Parses and transforms paths, resolves editable instances, samples geometry, and serializes SVG. | No CLI. Parse, registry, or transform errors propagate to the calling command. | Generic | Generic | Generic |
| [`core/keyfit.py`](../core/keyfit.py) | Profile-aware token lookup, containment, assignment, nearest-token, and circle-overflow math. | No CLI. Unknown token/profile input returns no match or raises through the profile resolver, depending on the helper. | Full | Full | Full |

## Regression and repository checks

Run the complete suite with:

```bash
python3 -m unittest discover -s core -p 'test_*.py'
```

Standard `unittest` behavior applies: exit `0` when all runnable tests pass and
`1` on a failure. Raster tests skip when their optional rendering dependencies
are unavailable.

| Test module | Contract protected | Normal | Sub | Container |
| --- | --- | --- | --- | --- |
| [`core/test_detect_svg_shapes.py`](../core/test_detect_svg_shapes.py) | Reference parsing, classification, atom proposals, warnings, transforms, and plots. | Generic | Generic | Generic |
| [`core/test_shape_registry.py`](../core/test_shape_registry.py) | Registry IDs, browser/Python parity, atom geometry, parsing, transforms, and rendering invariants. | Generic | Generic | Generic |
| [`core/test_compose_container_preview.py`](../core/test_compose_container_preview.py) | Filled-preview manifest/source separation, relative references, accepted-sub compatibility, deterministic regeneration, and non-shipping CLI labeling. | No | Full | Full |
| [`core/test_icon_profiles.py`](../core/test_icon_profiles.py) | Profile inheritance and declarations, sub emission, container-slot translation/protection, and incomplete-analysis rejection. | Full | Full | Full |
| [`core/test_keyfit.py`](../core/test_keyfit.py) | Normal-profile token family, centered bounds, assignment, containment, and radial overflow. Cross-profile math is covered by `test_icon_profiles.py`. | Full | No | No |
| [`core/test_keyshape_raster.py`](../core/test_keyshape_raster.py) | Raster painted-boundary classification, sub/container profile normalization, and CLI failure propagation. | Full | Full | Full |
| [`core/test_svg_grid.py`](../core/test_svg_grid.py) | Canvas normalization for every profile, fractional placement, angle failures, and hash-locked exceptions. | Full | Full | Full |
| [`core/test_repository_docs.py`](../core/test_repository_docs.py) | Maintained local Markdown files/headings, exhaustive `core/*.py` coverage in this inventory, and required rework verify-gate wiring. | N/A | N/A | N/A |

## Top-level orchestration and support

| Program | Inputs and outputs | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`rework_opus.sh`](../rework_opus.sh) | Runs `stage → draft → detect → make → verify → upload` for a rework URL/category. Verify recreates its batch-scoped grid/keyshape/hole report directories, latches command failures, then requires structural validation, declared overlap evidence, and complete fresh reports before upload. | `0` selected stage range completed; nonzero on any active-stage failure. A failed verify prevents the following upload stage. `--from upload` is an explicit operator bypass of earlier stages. | Full | No | No |
| [`upload.py`](../upload.py) | Reads `manifest.json` beside itself and POSTs each referenced SVG; `--dry-run` only lists requests. | `0` no HTTP failures; `1` manifest/host error or any failed request; `2` usage error. Missing individual SVGs are counted as skipped, not failed. | Generic | Generic | Generic |
| [`open_app.sh`](../open_app.sh) | Opens `frontend/index.html` with macOS `open`. | Returns the launcher status. Icon-type behavior belongs to the editor, not this wrapper. | Generic | Generic | Generic |
