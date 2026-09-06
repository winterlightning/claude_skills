# Script and Module Inventory

This is the command contract for the icon pipeline. Use
[icon-pipeline.md](icon-pipeline.md) for execution order, [icon-rules.md](icon-rules.md)
for shared design rules, and the selected [type guide](icon-types.md) for its
specific rules and generated profile.
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

Canvas, stroke, keyshapes and validation resolve from the JSON registry. Built-in
defaults are normal/main 48px, sub 32px, container 64px, with 4px stroke; custom
safe names work through the generic profile-aware tools. The role columns below
describe built-in workflow coverage, not an enum of allowed profiles.
`design`/`ship` names are same-size compatibility aliases; 1u = 1px.

Configured `defaultIconType` (initially `normal`) is used when legacy editable
JSON omits `iconType`. Commands with
an `--icon-type` option must be given the profile of standalone SVG input; when
editable JSON is supplied, its declaration is authoritative.
The mandatory `validate_icon_keyshapes.py` gate does not apply that legacy
fallback: it requires an explicit schema-version-2 editable profile and token.

All intake modes share the same acceptance order after structural/grid/overlap
prerequisites: **`check_svg_spacing.py` → `qa_overlays.py` →
`validate_icon_keyshapes.py`**, then native-size review. Every repair regenerates
the SVG aliases and restarts this sequence. Require complete fresh passing
evidence on the same SVG/profile; a later pass cannot waive an earlier failure.
SVG detection is only for supplied SVG references, never a fabricated reference
requirement for a name-and-description brief or a PNG input.
Distance, hole, and keyshape reports include SVG/profile hashes. Production
wrappers verify persisted evidence before accepting a delivery; profile-default
hole thresholds must match the selected JSON settings, not a relaxed diagnostic
override. The local pack also rejects profile-file changes during its build.

## Pipeline commands

| Program | Stage and inputs | Outputs or side effects | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`core/detect_svg_shapes.py`](../../core/detect_svg_shapes.py) | Detect one reference SVG. Input: `input`; optional `--output`, `--plot`, `--strict`, `--compact`, `--show`. | JSON to stdout or `--output`; optional plot image or interactive window. Does not compose an icon. | `0` analyzed; `3` manual review under `--strict`; `1` analysis/I/O error; `2` usage error. | Generic | Generic | Generic |
| [`core/batch_detect_svg_shapes.py`](../../core/batch_detect_svg_shapes.py) | Detect `*.svg` recursively. Inputs: `input_dir output_dir`; optional `--overwrite`, `--progress-every`. | Per-source `-shapes.json` and `-preflight.png`; `batch-summary.json`. Existing results are reused unless overwritten. | `0` with no per-file failures; `1` invalid/empty input or any failed source; `2` usage error. Review-required results alone do not make the command fail. | Generic | Generic | Generic |
| [`core/fetch_rework_batch.py`](../../core/fetch_rework_batch.py) | Stage a symbol-library rework payload from exactly one of `--cat`, `--url`, or `--json`; optional `--base`, `--out`, `--overwrite`, `--uploader`. | Fetches/copies one source per symbol; writes `manifest.json`, `batch.json`, `briefs.md`, subfolders, and a batch-local `upload.py`; prunes stale staged source names. | `0` staged; `1` malformed input, fetch/copy error, missing uploader, or name collision; `2` usage error. | Full | No | No |
| [`core/lucide_reference.py`](../../core/lucide_reference.py) | Read-only retrieval: `search QUERY [--limit N --kind KIND --json]`, `inspect ICON [--json]`. Maintenance: `index`. | Search/inspect print metadata and exact geometry; `index` rebuilds `references/lucide/index.json` without changing SVGs. | `0` success, including a search with no matches; `1` input/data error; `2` usage error. | Generic | Generic | Generic |
| [`core/rework_pack.py`](../../core/rework_pack.py) | Local SVG-prototype manifest pack: `{inspect,prepare,build} PACK`; `--skip-qa` is diagnostic only. Delivery names are `<sid>_rework.svg` or `<sid>_<api.label>.svg` (for example `_generated`). | Prepare writes prototype detection evidence/sheet. Build emits version-2 sources, runs prerequisites then profile-selected distance → holes → canvas/keyshape (both aliases), checks fresh hash-bound distance/keyshape evidence and visual review, and copies passing native SVGs to manifest destinations. Reuses the gate's raster keyfit evidence; failed icons do not replace prior deliveries. Writes fresh timestamped QA, `rework-results.json`, gallery and contact sheet. Never POSTs. | `0` inspect/prepare success or all-symbol build pass; `1` error, failing build or diagnostic-only build; `2` usage error. A failed run may contain passing local deliveries; inspect every result. | Full | Full | No |
| [`core/emit_icon.py`](../../core/emit_icon.py) | Emit an editable icon JSON; optional `--out-dir`. The document selects the icon profile. | Canonical native `<name>.svg` and byte-equivalent `<name>-design.svg` compatibility alias. Creates the output folder; no scaled derivative. | `0` emitted; nonzero on invalid JSON, name, profile, geometry, or write error; `2` usage error. | Full | Full | Full |
| [`core/compose_container_preview.py`](../../core/compose_container_preview.py) | Compose a non-shipping filled-preview manifest that references one container JSON and one accepted sub-icon JSON; requires `--out-dir`. | Validates both profiles, slot/keyshape compatibility, and 1:1 placement; writes a container-native preview SVG and same-size compatibility alias without creating a flattened editable source. | `0` native preview emitted; nonzero on manifest, profile, keyshape, geometry, or write error; `2` usage error. | No | Full | Full |
| [`core/validate_icon.py`](../../core/validate_icon.py) | Structural gate for one editable JSON and its native canonical/compatibility outputs; optional `--dir`. | Console findings only; does not mutate the icon. Checks the selected profile, exact canonical emitted parity, keyshape, spacing, and container protected region where applicable. Fractional-grid authority remains in `check_svg_grid.py`. | `0` pass; `1` one or more validation failures or an input error; `2` usage error. | Full | Full | Full |
| [`core/check_svg_grid.py`](../../core/check_svg_grid.py) | Grid/canvas gate for SVG files or flat folders. Requires `--output-dir`; accepts `--expected`, `--icon-type`, `--exceptions`, and `--keyfit-results`. | `grid-results.json`, `grid-results.csv`, `grid-report.html`, and copied preview SVGs under `icons/`. | `0` no failing result; `1` any fail; `2` no usable input or option error. A documented fractional review may pass only through a matching hash-locked exception. | Full | Full | Full |
| [`core/check_svg_spacing.py`](../../core/check_svg_spacing.py) | Disconnected-stroke spacing on actual native SVG files or flat folders. Default `--icon-type normal`; optional `--output-dir`, `--json`, `--quiet`. Requires strict flat round-stroked SVG at the profile's native dimensions/stroke; no editable metadata or threshold overrides. | Identifies separate subpaths and connected components, then reports every component pair's nearest centerline distance and ink clearance. Normal48 uses configured 8u centerline / 4u ink gap. Optional fresh per-file JSON and colored native SVG, plus `spacing-results.json` and `spacing-report.html`. Does not edit inputs. Also called by normal structural validation. | `0` every input passes; `1` violation, unresolved curve measurement/contact, input/dependency/report error; `2` CLI misuse. One connected shape has no separate pairs, not proof of valid internal spacing. | Full | Full | Outer only |
| [`core/render_overlap_audit.py`](../../core/render_overlap_audit.py) | Render two-element relationships in version-2 editable JSON, or legacy instance pairs. Inputs: `input [output]`. | One profile-sized, expanded-stroke SVG panel per valid entry in `sourceAnalysis.spacingChecks`. This is review evidence, not an automatic visual verdict. | `0` at least one panel written; `1` no valid pair relationship; `2` usage error. A caller should skip it only when no relationship is declared. | Full | Full | Full |
| [`core/validate_icon_keyshapes.py`](../../core/validate_icon_keyshapes.py) | Mandatory native canvas/painted-keyshape gate: `SVG [SVG ...]` or flat folder; requires `--editable ONE_JSON` for one SVG or `--expected-editable-dir DIR`. Optional `--icon-type NAME`, `--output-dir`, `--json`, `--quiet`; no threshold overrides. Declared schema-v2 metadata is authoritative and design aliases share the canonical JSON. | Checks explicit native width/height/viewBox, configured stroke, strict flat geometry, declared exact/optical fit, stroke overflow and protected slots through current profiles. Optional QA writes: fresh `canvas-keyshape-results.json` with `ok`, `checked`, `failed`, `rows`; per-input reports and keyfit overlay under unique `files/<stem>-<pathhash>-<runid>/`. Does not edit inputs or profiles. | `0` all selected inputs pass; `1` validation/read/dependency failure; `2` CLI misuse. Any missing, stale, or failing expected result blocks completion; passing is not full production approval. | Full | Full | Full |
| [`core/check_keyfit.py`](../../core/check_keyfit.py) | Raster implementation used internally by `validate_icon_keyshapes.py`; standalone native SVG/folder diagnostics require `--output-dir` and accept `--expected-editable-dir`, `--icon-type`, raster sampling, and tolerance options. | Per-icon `.keyfit.json` and `_keyfit.png`; standalone aggregate `keyfit-results.json`, CSV, and HTML. Do not duplicate its work after the mandatory gate or use diagnostic tolerances for delivery acceptance. | `0` every processed icon passes; `1` any fail or processing error; `2` missing inputs, missing declared metadata, or option error. A standalone pass does not replace `validate_icon_keyshapes.py`. | Full | Full | Full |
| [`core/qa_overlays.py`](../../core/qa_overlays.py) | Raster hole-and-pinch gate for native SVGs or flat folders. Requires `--output-dir`; accepts `--icon-type`, `--error-dir`, sampling, radius, and fill-depth options. Use profile defaults for acceptance. | Per-icon `.metrics.json` and `_holes.png`; aggregate `hole-diameters.json`, CSV, and HTML with explicit failed processing-error rows. Failure copies go in fresh per-run folders under `hole_error/`; prior evidence and input files are preserved. Rejects input/output collisions. Repair authoritative editable JSON, not QA copies. | `0` every selected input passes; `1` any hole/pinch violation, invalid/missing input, processing or report error; `2` argument error or only empty folders. Require both exit success and complete fresh passing rows. | Full | Full | Full |
| [`core/render_svg_contact_sheet.py`](../../core/render_svg_contact_sheet.py) | Render a flat native SVG folder. Inputs: `input output`; optional `--columns`, `--icon-type`, `--true-size`, `--preview-scale`. | One labeled native-size PNG contact sheet; type selects its configured canvas, optional `--true-size` must match, and the default preview scale is 1. Validates viewport/intrinsic dimensions and omits byte-identical `-design.svg` aliases. Creates the output parent. | `0` rendered; `2` empty input, non-native dimensions, divergent aliases, or option error; nonzero on parse/render/write failure. | Full | Full | Full |
| [`core/classify_icon_type.py`](../../core/classify_icon_type.py) | Size-based skill picker for generation packs. Inputs: pack roots, batch folders, `sym_*` folders, or prototype SVGs; optional `--sub-max` (default 12u), `--no-stroke`, `--overwrite`, `--dry-run`, `--json`. | Writes one-word `icon_type.txt` (`sub` or `normal`) beside each `sym_*/<sid>_prototype.svg`; preserves an existing `container` verdict unless overwritten. Never touches prototypes or manifests. | `0` all prototypes measured; `1` any measurement failure; `2` no prototype found or usage error. | Full | Full | Input only |
| [`core/bbox_zones.py`](../../core/bbox_zones.py) | Measure painted or centerline bounds for SVG files/folders. Inputs: one or more paths; optional `--no-stroke`, `--json`. | Text or JSON on stdout; no files written. | `0` all collected files parsed, including an empty collection; `1` any per-file parse failure; `2` usage error. | Generic | Generic | Generic |

## Registry, compatibility, and migration commands

Manage numerical profiles with [profile configuration](profile-configuration.md).
The browser manager edits the actual JSON; it is separate from icon authoring.

Shape registries and their generated assets are legacy compatibility tools.
Ordinary version-2 authoring neither changes the registry nor runs asset generation.
Profile generation remains current because it maintains numeric profile mirrors.

| Program | Inputs | Outputs or side effects | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`core/profile_manager.py`](../../core/profile_manager.py) | Local configuration app; optional `--port`, `--no-open`; read-only `--validate PATH`. | Serves Profile Manager on loopback. Validated revision-guarded saves back up and atomically replace profile JSON/generated Markdown references; no icon geometry, artifacts or uploads are changed. | `0` valid candidate or clean server shutdown; `1` invalid candidate/startup error; `2` usage error. API save failures return an HTTP error without ending the server. | Full | Full | Full |
| [`core/generate_profile_assets.py`](../../core/generate_profile_assets.py) | `core/icon_profiles.json`; optional `--docs`, `--type-docs-root`, and read-only `--check`. | Generates all configured types in `docs/shared/icon-profiles.md`, plus `profile.md` for the existing built-in skill folders. `--docs` changes the combined reference; `--type-docs-root` changes the root for the type pages. Without `--check`, creates parents and rewrites stale Markdown references. | `0` all generated references match or were generated; `1` at least one is missing or stale under `--check`; `2` usage error. Check mode writes nothing. | Full | Full | Full |
| [`core/adapt_icon.py`](../../core/adapt_icon.py) | Experimental draft trial: `INPUT_FILE_OR_FOLDER --from-profile NAME --to-profile NAME --metadata-dir EXISTING_EDITABLE_DIR --out-dir NEW_NONEXISTENT_DIR`. Use `--source-keyshape TOKEN` instead of metadata when unavailable; optional `--target-keyshape TOKEN`. Folders select immediate `*-design.svg` only; profiles with slots are rejected. | Copies selected sources into a new trial directory; writes draft editable JSON, native SVG aliases, prerequisites and distance → holes → canvas/keyshape QA (both aliases), `summary.json`, and `review.html`. Fresh SVG/editable/profile hashes bind results; verified companion metadata supplies intent, never old approval. No original/configuration edits or uploads. See [profile adaptation](profile-configuration.md#try-a-profile-adaptation). | `0` all selected inputs emitted and QA executed, **not approval**; numeric failures remain draft findings. `1` file-processing error; `2` invalid input or usage. | Full | Full | No |
| [`core/compose_examples.py`](../../core/compose_examples.py) | Every `assets/icons/*.json`. | Rewrites one native `<name>.svg` per example through the compatibility renderer; no companion or alias. | `0` all rendered; `1` no example JSON; propagates a failed child render as nonzero. | Full | No | No |
| [`core/render_icon.py`](../../core/render_icon.py) | Compatibility editable JSON and optional output filename; accepts compatibility-only `--distance-check`. | Only the requested native SVG, default `<name>.svg`; no suffixed companion. | `0` rendered; nonzero on invalid input/geometry/write error; `2` usage error. Does not replace canonical validation. | Full | Full | Outer only |
| [`core/repair_keyshape_targets.py`](../../core/repair_keyshape_targets.py) | Dataset-specific editable-source folder, pre-repair `keyfit-results.json`, and a new output folder. | Reworked editable JSON, a native 48px `final/` set, and a hash-locked exception manifest; no `final_24/` derivative. It contains named overrides for one historical migration. | `0` completed; nonzero on missing/inconsistent data or geometry. It may write into an existing output tree, so use a new folder. | Full | No | No |
| [`core/restore_grid_outputs.py`](../../core/restore_grid_outputs.py) | Historical flat SVG inventory; requires `--output-dir`; optional `--project-root`, `--overwrite`. | Re-emits a fixed historical normal-icon set from known editable-source locations; writes native `final/`, `editable/`, a repair manifest, and grid exceptions, without SVG aliases or reduced derivatives. `--overwrite` removes the existing target first. | `0` completed; `2` existing target without `--overwrite`; nonzero on missing source or emission error. | Full | No | No |

Do not use the compatibility renderer or either migration command as a substitute
for the canonical emitter and validators.

## Shared modules and data

These are imported by commands; they are not standalone CLIs.

| Path | Input and output contract | Import/failure behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- |
| [`core/icon_profiles.json`](../../core/icon_profiles.json) | Schema-v2 numerical source: default type, canvas, stroke, keyshapes, validation defaults/overrides, inheritance and slots; centers/compatibility aliases are derived. | No process exit. Malformed data makes `icon_profiles.py` fail at import. | Full | Full | Full |
| [`core/icon_profiles.py`](../../core/icon_profiles.py) | Validates raw configuration, resolves arbitrary named profiles/inheritance/effective validation, and validates editable profile declarations, native SVG viewport/intrinsic dimensions, token lookup, and container-slot metadata. Returns detached profile/token structures or native-size findings. | No CLI. Raises `ValueError` for unknown/inconsistent profiles or invalid declarations. | Full | Full | Full |
| [`core/shape_registry.py`](../../core/shape_registry.py) | Legacy compatibility: resolves historical shape IDs and requested boxes. Not the vocabulary for new icons. | No CLI. Importers receive `SHAPES` and `BY_ID`; invalid requests raise. | Generic | Generic | Generic |
| [`core/icon_geometry.py`](../../core/icon_geometry.py) | Validates version-2 geometry elements, normalizes paths, bakes legacy placements, samples geometry, and serializes SVG with central paint. | No CLI. Invalid IDs, attributes, paths or legacy geometry raise through the calling command. | Generic | Generic | Generic |
| [`core/stroke_distance.py`](../../core/stroke_distance.py) | Splits normalized paths into drawable subpaths, bounds curve approximation, proves centerline connections, and measures continuous nearest segment distances between disconnected components. Returns contour IDs, grouping, nearest pairs and measurement bounds. | No CLI or file writes. Invalid inputs return failure; exhausted numerical/work bounds, ambiguous curved contact and unresolved threshold cases return non-passing review results. | Generic | Generic | Generic |
| [`core/profile_adaptation.py`](../../core/profile_adaptation.py) | Strict SVG ingestion and pure geometry adaptation: uniform stroke-aware profile fit and symmetry-aware grid placement; returns draft geometry and findings, not acceptance. Companion-metadata verification belongs to the trial runner. | No CLI or filesystem writes. Invalid input/profile/geometry raises through the calling trial runner. | Full | Full | No |
| [`core/keyfit.py`](../../core/keyfit.py) | Profile-aware token lookup, containment, assignment, nearest-token, and circle-overflow math. | No CLI. Unknown token/profile input returns no match or raises through the profile resolver, depending on the helper. | Full | Full | Full |

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
| [`core/test_detect_svg_shapes.py`](../../core/test_detect_svg_shapes.py) | Reference parsing, classification, atom proposals, warnings, transforms, and plots. | Generic | Generic | Generic |
| [`core/test_shape_registry.py`](../../core/test_shape_registry.py) | Legacy registry IDs, atom geometry, parsing, transforms, and rendering invariants. | Generic | Generic | Generic |
| [`core/test_icon_geometry.py`](../../core/test_icon_geometry.py) | Version-2 element/schema validation, path parsing, exact emission, legacy conversion and relationship contracts. | Full | Full | Full |
| [`core/test_lucide_reference.py`](../../core/test_lucide_reference.py) | Local reference lookup, exact inspection and corpus metadata behavior. | Generic | Generic | Generic |
| [`core/test_profile_manager.py`](../../core/test_profile_manager.py) | Local manager validation, revision conflicts, bounded backups/mirror saves, rollback, and HTTP access boundaries. | Full | Full | Full |
| [`core/test_adapt_icon.py`](../../core/test_adapt_icon.py) | Draft adaptation selection, verified metadata, evidence invalidation, new-directory output scope, original preservation, QA/report execution, and non-approval exit semantics. | Full | Full | No |
| [`core/test_profile_adaptation.py`](../../core/test_profile_adaptation.py) | Strict SVG ingestion, bounded geometry processing, stroke-aware fit, symmetry/grid handling, coherent ellipses, and collapse/curve/overflow findings. | Full | Full | No |
| [`core/test_classify_icon_type.py`](../../core/test_classify_icon_type.py) | Size classifier threshold boundary, preserved `container` verdicts, dry-run safety, and prototype collection scope. | Full | Full | Generic |
| [`core/test_rework_pack.py`](../../core/test_rework_pack.py) | Manifest pack scope, safe local paths, normal publication safety, stale-review rejection, and native gallery/contact-sheet dimensions for all three profiles. | Full | Generic | Generic |
| [`core/test_optical_keyfit.py`](../../core/test_optical_keyfit.py) | Exact/optical fit mode, required rationale/measured bounds and containment. | Full | Full | Full |
| [`core/test_compose_container_preview.py`](../../core/test_compose_container_preview.py) | Filled-preview manifest/source separation, relative references, accepted-sub compatibility, deterministic regeneration, and non-shipping CLI labeling. | No | Full | Full |
| [`core/test_icon_profiles.py`](../../core/test_icon_profiles.py) | Profile inheritance and declarations, sub emission, container-slot translation/protection, and incomplete-analysis rejection. | Full | Full | Full |
| [`core/test_keyfit.py`](../../core/test_keyfit.py) | Normal-profile token family, centered bounds, assignment, containment, and radial overflow. Cross-profile math is covered by `test_icon_profiles.py`. | Full | No | No |
| [`core/test_keyshape_raster.py`](../../core/test_keyshape_raster.py) | Raster painted-boundary classification, sub/container profile normalization, and CLI failure propagation. | Full | Full | Full |
| [`core/test_validate_icon_keyshapes.py`](../../core/test_validate_icon_keyshapes.py) | Mandatory canvas/keyshape gate: explicit native dimensions and metadata, configured profiles/strokes/tokens, strict SVG parsing, painted curve/overflow measurements, exact/optical fit, slot protection, CLI failure propagation and complete report evidence. | Full | Full | Full |
| [`core/test_svg_grid.py`](../../core/test_svg_grid.py) | Canvas normalization for every profile, fractional placement, arbitrary line directions, and hash-locked exceptions. | Full | Full | Full |
| [`core/test_check_svg_spacing.py`](../../core/test_check_svg_spacing.py) | Separate lines/subpaths, exact spacing thresholds, ink contact versus centerline connections, curved/diagonal distances, profile selection, unsafe input rejection, CLI reports and input preservation. | Full | Full | Outer only |
| [`core/test_qa_overlays.py`](../../core/test_qa_overlays.py) | Hole/pinch CLI failure exits, complete input/error coverage, report failures, fresh diagnostic copies and input/output collision protection. | Full | Full | Full |
| [`core/test_upload.py`](../../core/test_upload.py) | Offline normal/forced upload request headers, raw SVG body, manifest destination, and dry-run no-network behavior. | Generic | Generic | Generic |
| [`core/test_repository_docs.py`](../../core/test_repository_docs.py) | Maintained Markdown links/headings, exhaustive script inventory, rework verify-gate wiring, and isolated version-2 source-preflight behavior without running wrapper stages. | N/A | N/A | N/A |

## Profile Manager interface

- [`frontend/profiles.html`](../../frontend/profiles.html) and [`frontend/css/profiles.css`](../../frontend/css/profiles.css): local profile-manager interface.
- [`frontend/js/profile-manager.js`](../../frontend/js/profile-manager.js): manager edits, preview and save coordination.
- [`frontend/js/profile-config.js`](../../frontend/js/profile-config.js): browser configuration resolution/validation.
- [`frontend/js/profile-api.js`](../../frontend/js/profile-api.js): session-aware local API access.
- [`frontend/browser-smoke.cjs`](../../frontend/browser-smoke.cjs): read-only browser regression for the shipped defaults and an unsaved custom profile. Requires Playwright/Chromium and `PROFILE_MANAGER_URL`; blocks configuration writes and saves screenshots only to a temporary directory.

## Top-level orchestration and support

| Program | Inputs and outputs | Exit behavior | Normal | Sub | Container |
| --- | --- | --- | --- | --- | --- | --- |
| [`rework_opus.sh`](../../rework_opus.sh) | Runs `stage → draft → detect → make → verify → upload` for a rework URL/category. `draft` is a compatibility intake checkpoint; brief-only rows fabricate no SVG and skip detection, while actual SVG references get individual reports. Verify recreates batch-scoped QA directories, runs prerequisites then distance → holes → canvas/keyshape (both aliases), latches failures and requires complete fresh reports before upload. | `0` selected stage range completed; nonzero on any active-stage failure. A failed verify prevents upload; `--from upload` still runs verification. Passing checks does not replace separate upload approval. | Full | No | No |
| [`upload.py`](../../upload.py) | Reads `manifest.json` beside itself and POSTs each referenced SVG to `--base` or `api.base`, with `User-Agent: symlib-rework-upload/1.0`; `--dry-run` only lists requests. The [upload guide](../icons/rework.md#dry-run-and-approve-the-upload) covers production and existing batch-local copies. | `0` no HTTP failures; `1` manifest/host error or any failed request; `2` usage error. Missing individual SVGs are counted as skipped, not failed. | Generic | Generic | Generic |
| [`open_app.sh`](../../open_app.sh) | Launches the local Profile Manager; forwards options such as `--port` and `--no-open` to `core/profile_manager.py`. | Returns the manager's exit status. It does not edit icon geometry. | Full | Full | Full |
