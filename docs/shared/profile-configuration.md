# Profile configuration and manager

[`core/icon_profiles.json`](../../core/icon_profiles.json) is the numerical
authority for icon types. The built-in `normal`, `sub`, and `container` profiles
start at 48px, 32px, and 64px with 4px stroke, but those are editable defaults.
Custom safe names are supported without adding Python branches or another skill.
The three skills describe drawing roles; the [shared pipeline](icon-pipeline.md)
works with any configured profile.

One invariant remains: authoring geometry, canonical SVG, and acceptance review
use the same native canvas and stroke, with 1u = 1px. Configuration is not a
mechanism for silently scaling finished icons or bypassing their review.

## Use the local app

From the repository root:

```bash
python3 core/profile_manager.py
```

This starts the manager at loopback `127.0.0.1:8765` and opens its session URL in
the browser. Use `--port <number>` if needed (`--port 0` chooses a free port), or `--no-open` to open the printed
URL yourself. The manager is served at `/`.
Stop the server with Ctrl-C when finished. Opening `frontend/profiles.html`
directly is not a replacement for the local save service.

This app manages profiles only. Author icon geometry as editable JSON and use
the [CLI pipeline](icon-pipeline.md) for emission, QA, and native-size review.

Edit profiles, keyshapes, validation defaults/overrides, or the raw configuration
in the manager. Inspect the resolved settings before saving. Save validates the
whole registry, rejects a stale revision, and updates the actual JSON plus its
generated Markdown profile references. Reload after a conflict rather than
overwriting another editor's changes.

The service binds only to loopback. Its API requires the launch session token,
checks request host/origin, and limits writes to configuration/mirror targets.
Keep the token-bearing launch URL local. It is not a hosted multi-user service.

Before changed files are replaced, their previous contents are backed up under
`work/profile-config-backups/<timestamp-id>/`, with a manifest. Saves use atomic
file replacement and attempt rollback if any write fails; inspect a reported
rollback failure before restoring a named backup. Saving never modifies icon
JSON, original references, rework manifests, emitted icon artifacts, or uploads.

## JSON fields and inheritance

The profile registry's `schemaVersion: 2` is distinct from an editable icon's
own version-2 geometry schema.

| Location | Meaning |
| --- | --- |
| `defaultIconType` | Existing profile used by compatibility inputs that omit `iconType`; new icons declare their type explicitly |
| `validationDefaults` | Complete shared validation settings listed below |
| `profiles.<name>.label` | Required nonempty display label on every raw profile |
| `canvas` | Positive integer native square canvas in pixels/units |
| `strokeWidth` | Positive finite native stroke, no larger than the canvas |
| `keyshapes` | Nonempty array of centered painted-boundary tokens |
| `extends` | Optional existing parent profile; cycles are rejected |
| `validation` | Optional partial override of effective validation settings |
| `containerSlot` | Optional accepted-profile slot; omit to inherit, use `null` to clear, or supply the complete replacement object |

Profile and keyshape names use safe kebab form: lowercase letters/digits joined
by single hyphens, excluding the reserved names `constructor` and `prototype`.
Unknown fields and invalid references are rejected. A profile
without a parent supplies canvas, stroke, and keyshapes itself; a child inherits
omitted fields. An explicit keyshape array replaces the entire inherited array,
not individual entries. Validation merges global defaults → parent → child.

Changing canvas or stroke does not scale inherited keyshapes, slot coordinates,
or icon geometry. Update any dependent dimensions intentionally. The resolver
derives the center from `canvas / 2` and exposes legacy `design*`/`ship*` names
with equal values. Do not author those derived fields in the raw JSON.

### Keyshapes

Each token has `name`, `orientation`, `shape`, `width`, and `height`. Names are
unique within the profile. `shape` is `rect` or `circle`; orientation is `square`,
`portrait`, `landscape`, or `circle`, consistent with the dimensions. Circles
also require `diameter` equal to width and height; rectangles omit it. Tokens
must fit inside the canvas and cannot be narrower than the configured stroke.
There is no requirement to define all four orientations.

### Validation settings

All seven keys are required in `validationDefaults`; profile overrides may
specify only the keys they change. Values use native units (1u = 1px).

| Key | Built-in default | Controls |
| --- | --- | --- |
| `gridStep` | 1 | Ordinary placement grid |
| `majorGridStep` | 4 | Major guide interval; a positive integer multiple of `gridStep` |
| `geometryTolerance` | 0.001 | Numeric geometry agreement/tolerance checks |
| `keyshapeTolerance` | 0.03125 | Painted-keyshape measurement tolerance |
| `minimumDistinctCenterlineDistance` | 4; sub overrides to 3 | Minimum distance between distinct geometry centerlines |
| `minimumEnclosedRadius` | 1 | Enclosed negative-space radius floor |
| `minimumSolidFillDepth` | 1 | Solid junction depth/pinch gate; 0 explicitly disables this gate |

Values are finite and positive, except solid-fill depth may be zero. Treat a
threshold change as a visible policy decision, not an icon-specific waiver.
Ordinary QA commands use resolved settings when no explicit diagnostic override
is supplied. Visual construction guidance, such as corner treatment and declared
opening clearance, still belongs in [shared rules](icon-rules.md); it is not an
undocumented extra manager setting.

### Container slots

A full slot has `x`, `y`, `w`, `h`, `acceptedProfile`, and `minimumClearSquare`.
The accepted profile must exist and differ from the outer profile. The slot is
centered and square, with dimensions equal to the accepted profile's native
canvas; the protected clear square covers that accepted canvas. An editable
container additionally chooses `acceptedKeyshape` from the accepted profile.
Changing an inserted profile's canvas therefore requires updating every slot
that accepts it. Inserts remain separately authored and are translated, not
scaled, into the slot.

## Add a custom type

Add a profile in the manager, or add an entry under `profiles`. For example,
this independent toolbar family inherits shared normal settings but replaces
its geometry dimensions and keyshape list:

```json
"toolbar": {
  "label": "Toolbar icon",
  "extends": "normal",
  "canvas": 40,
  "strokeWidth": 3,
  "validation": {"gridStep": 0.5, "majorGridStep": 2},
  "keyshapes": [
    {"name": "circle-36", "orientation": "circle", "shape": "circle", "width": 36, "height": 36, "diameter": 36},
    {"name": "square-32", "orientation": "square", "shape": "rect", "width": 32, "height": 32}
  ]
}
```

This is an example entry, not a request to change the current registry. Validate
the complete registry before saving. The manager and generated aggregate
reference include custom types; dedicated type `profile.md` pages are generated
only for the existing built-in skill folders.

For an icon request, say:

```text
Use the shared icon pipeline with iconType "toolbar" from core/icon_profiles.json
to create <subject>. Resolve its current canvas, stroke, keyshapes, and validation
settings. Deliver editable version-2 geometry, the canonical native SVG, and fresh
QA/native-size review. Process only this subject; do not change profiles or upload.
```

An unknown name needs an explicit configuration decision; do not silently choose
`normal`. Special-purpose URL/upload or legacy migration scripts may still have
their own role/input restrictions—use the generic pipeline for custom profiles.

## Try a profile adaptation

When a user explicitly requests a mechanical adaptation experiment, create a
separate draft trial:

```bash
python3 core/adapt_icon.py INPUT_FILE_OR_FOLDER \
  --from-profile normal --to-profile sub \
  --metadata-dir EXISTING_EDITABLE_DIR \
  --out-dir NEW_NONEXISTENT_DIR
```

A folder input selects only its immediate `*-design.svg` files, not canonical
aliases or subdirectories. The actual SVG supplies geometry; a verified matching
companion JSON supplies declared keyshape/optical intent and relationship labels.
When no companion metadata is available, use `--source-keyshape TOKEN` instead
of `--metadata-dir`; the two options are mutually exclusive. The target token is
matched by orientation unless `--target-keyshape TOKEN` is supplied. Profiles
with a `containerSlot` are rejected on either side of this experiment.
The experiment uses a uniform stroke-aware fit and symmetry-aware grid placement.
It does not change profile configuration, edit the originals in place, or upload.

The new directory holds source copies, draft editable JSON, native canonical SVGs
and same-size `-design.svg` aliases, QA evidence, `summary.json`, and `review.html`.
Every draft retains `sourceAnalysis.incomplete: true`; old visual acceptance and
grid exceptions are not carried over. Exact-fit failures remain failures, not
automatic optical waivers; optical intent can only come from verified source
metadata. Inspect numeric findings and the actual target-native
rendering before deciding what needs recomposition or simplification.

Exit `0` means the selected inputs were emitted and QA ran, **not that the icons
are approved**. Numeric failures remain disclosed in the draft results. Exit `1`
indicates a file-processing error; `2` indicates invalid input or command usage.
The ordinary [authoring pipeline](icon-pipeline.md) and target type's composition,
spacing, keyfit, and visual-review rules remain the delivery requirements.

## Validate and refresh after edits

For a candidate configuration, validation is read-only:

```bash
python3 core/profile_manager.py --validate path/to/candidate.json
```

If you deliberately edit `core/icon_profiles.json` directly, regenerate mirrors:

```bash
python3 core/generate_profile_assets.py
python3 core/generate_profile_assets.py --check
```

The next CLI process reads current JSON. Reload the manager to see changes made
outside the app. Generated Markdown is a reference, not a separate configuration
source. A successful configuration save does not prove any existing icon still
conforms.

Re-emit affected sources under the changed profile, rerun all relevant QA, and
review the actual native SVG before delivery. Update recorded bounds, spacing,
review size/hash, and reference rationale where they changed. A profile or
validation change invalidates prior acceptance evidence even if the SVG bytes
did not change. Never fix that by editing review metadata alone. Do not migrate
historical work/rework folders unless that migration was explicitly requested.
