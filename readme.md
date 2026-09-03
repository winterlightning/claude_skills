# Unlimited Shapes

Build normal, sub, and container icons with exact editable geometry and
reference-informed construction. Author, export, and review at one native size
per configured profile. Built-in defaults are **48×48px normal/main**,
**32×32px sub**, and **64×64px container**, with 4px stroke. These values are
editable, and additional named profiles are supported. Keep 1u = 1px and do not
create half-size derivatives.

New sources use `schemaVersion: 2` and an
ordered `elements` array: lines, native shapes, and connected paths with arcs or
quadratic/cubic curves. A new contour does not require a named shape, registry
change, or generated shape asset.

The semantic brief and supplied prototype define what to draw. Relevant Lucide
original/debug pairs help explain how to construct it. Preserve useful contour
grouping, proportions, joints and gaps; do not treat debug segmentation or a
target part count as the style.

Start with the skill for the icon's role:

- [Normal icons](docs/icons/SKILL.md)
- [Sub icons](docs/sub-icons/SKILL.md)
- [Container icons](docs/container-icons/SKILL.md)

The [documentation index](docs/README.md) routes to shared rules and input lanes.
[Editable geometry and references](docs/shared/atomic-shapes.md) defines the
source schema. [The canonical pipeline](docs/shared/icon-pipeline.md) defines
emission, QA, repair and delivery. Exact canvas, stroke, keyshape and slot values
remain in [core/icon_profiles.json](core/icon_profiles.json).

## Manage profiles

```bash
python3 core/profile_manager.py
```

The local app edits the actual `core/icon_profiles.json`: canvas, stroke,
keyshapes, validation defaults/overrides, inheritance, and custom icon types.
Save validates the configuration, backs up the previous JSON/mirrors, and
regenerates the Markdown profile references. It does not migrate existing
icons. Changed profiles require deliberate re-emission, QA, and native review.
See [Profile configuration](docs/shared/profile-configuration.md) for the schema,
custom-profile workflow, and local save boundaries.

## Find a construction reference

```bash
python3 core/lucide_reference.py search 'cloud' --limit 6
python3 core/lucide_reference.py inspect cloud --json
```

The local bundle contains authoritative original SVGs, generated colored
segment views, an index, provenance and license information. Inspect only
relevant examples and record the selected names and principles in
`sourceAnalysis.lucideReferences`. Original SVGs remain authoritative reference
evidence; debug files are an inspection aid, not required production markup.
Their original 24px canvas stays unchanged as reference evidence; it does not
determine the configured output or acceptance-review size.

## Rework a local pack

For a user-selected pack containing `manifest.json` and prototypes:

```bash
python3 core/rework_pack.py inspect path/to/pack
python3 core/rework_pack.py prepare path/to/pack
```

Follow the [local pack lane](docs/icons/rework.md#local-manifest-pack-lane) to
author the exact selected symbols in `editable/`, emit and inspect the drafts,
and record a hash-locked true-size visual review. Then run:

```bash
python3 core/rework_pack.py build path/to/pack
```

Build emits the existing editable sources, verifies QA and prepares manifest
delivery files plus a local review gallery. It does not author the subjects or
upload them. Keep manifest/prototypes unchanged and inspect true-size results.
`--skip-qa` is diagnostic only, not a completed delivery.

Existing rework folders are historical artifacts, not automatically rebuilt by
this rule change. If migration is requested later, old half-size visual evidence
must be replaced by an actual native-size review and a fresh SVG hash; changing
the review size field alone is insufficient.

The separate URL/payload workflow remains available:

```bash
./rework_opus.sh "https://symlib.pictographic.ai/download-wrong-icons-json?cat=Building+Construction" --to verify
```

It stages, detects, makes and verifies normal icons. Uploading is a separate,
explicitly authorized action after dry-run and review; a rework request alone
does not authorize it.

## Detect supplied SVG evidence

```bash
python3 -m pip install -r requirements.txt
python3 core/detect_svg_shapes.py path/to/input.svg \
  --output path/to/input-shapes.json \
  --plot path/to/input-preflight.png
```

Inspect the source, report and plot together. Detector coordinates use a 48-unit
analysis grid; recompose on the chosen configured profile. Legacy atom
suggestions are optional hints, not an authoring restriction. Under `--strict`,
status `3` means manual review is required before making the icon.

## Author geometry and emit output

Author schema-version-2 editable JSON directly, using the selected skill and
[geometry guide](docs/shared/atomic-shapes.md). Edit element coordinates,
geometry attributes, semantic roles, and source-analysis evidence in that JSON.
The Profile Manager configures the system; it does not edit icon geometry.

```bash
python3 core/emit_icon.py work/<job>/editable/<name>.json --out-dir work/<job>/output
python3 core/validate_icon.py work/<job>/editable/<name>.json --dir work/<job>/output
```

Canonical paint is imposed centrally. Editable JSON remains the repair source;
the emitter writes native `<name>.svg` and a byte-equivalent `<name>-design.svg`
compatibility alias, not a second resolution. Complete the [shared QA
pipeline](docs/shared/icon-pipeline.md) and native-size visual review before
delivery. Legacy documents remain backend compatibility inputs.

## Layout

| Folder | Contents |
| --- | --- |
| `frontend/` | Profile Manager app |
| `references/lucide/` | Original/debug SVG pairs, searchable index, provenance and license |
| `core/` | JSON profile configuration/local manager, geometry, emission, validation, reference retrieval, rework and QA tools |
| `docs/icons/` | Normal-icon skill, rules, requests and rework adapters |
| `docs/sub-icons/` | Sub-icon skill, rules and requests |
| `docs/container-icons/` | Container skill, rules and requests |
| `docs/shared/` | Geometry schema, pipeline, input adapters and QA guides |

Legacy `instances` documents remain supported for compatibility. Do not extend
the old shape registry or regenerate its assets during ordinary icon authoring.
