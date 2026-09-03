# Unlimited Shapes

Build normal, sub, and container icons with exact editable geometry and
reference-informed construction. New sources use `schemaVersion: 2` and an
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
analysis grid; recompose on the chosen normal/sub/container profile. Legacy atom
suggestions are optional hints, not an authoring restriction. Under `--strict`,
status `3` means manual review is required before making the icon.

## Editor and output

Open `frontend/index.html` directly in a browser; no build step is required.
Start a path, line, circle, ellipse, rectangle, polyline or polygon. Edit exact
geometry attributes and semantic roles, or import/edit/export the whole version-2
document. Dragging and nudging bake coordinates rather than saving transforms.
Undo, duplication, ordering, profile guides and actual ship-size previews support
review. Geometry edits mark source analysis incomplete until it is reviewed again.

Canonical paint is imposed centrally. Exported editable JSON remains the repair
source; final design/ship SVGs come from `core/emit_icon.py` and the shared QA
pipeline. Browser previews do not replace validation. The editor requires
version-2 sources; legacy documents remain backend compatibility inputs and
must be converted before editor import.

## Layout

| Folder | Contents |
| --- | --- |
| `frontend/` | Profile-aware editable geometry editor |
| `references/lucide/` | Original/debug SVG pairs, searchable index, provenance and license |
| `core/` | Geometry, emission, validation, reference retrieval, rework and QA tools |
| `docs/icons/` | Normal-icon skill, rules, requests and rework adapters |
| `docs/sub-icons/` | Sub-icon skill, rules and requests |
| `docs/container-icons/` | Container skill, rules and requests |
| `docs/shared/` | Geometry schema, pipeline, input adapters and QA guides |

Legacy `instances` documents remain supported for compatibility. Do not extend
the old shape registry or regenerate its assets during ordinary icon authoring.
