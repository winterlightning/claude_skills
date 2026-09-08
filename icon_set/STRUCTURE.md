# `icon_set` — what lives where, and why

A map of every folder and script in `icon_set/`, grouped by the mission it
serves. Read this when you need to know *which file to open* for a task; read
[`README.md`](README.md) for the rules themselves and
[`skills/icon-design/SKILL.md`](skills/icon-design/SKILL.md) for how to design
an icon.

The geometry model and vector checks use stdlib Python. Build-time raster QA
loads CairoSVG, NumPy, OpenCV, and Pillow lazily; see `requirements-qa.txt`.

## The system in one picture

```
 contracts (JSON)  ──read at import──►  model  ──build()──►  Icon instance
       ▲                                  │                       │
       │ every number lives here          │ Sub32 / Solo48 /      │ draw()
       │                                  │ Container64 pick      ▼
       │                                  │ the profile        renderers ──► SVG / PNG
       │                                  ▼                       │
   tests hold                          registry                   ▼
   docs + code                      (discovers by folder)     validation (8 checks)
   to the contracts                       │                       │
                                          ▼                       ▼
                                   scripts/build.py ──────► dist/<family><canvas>/
                                   scripts/compose.py ────► dist/compositions/
                                   scripts/generate_skills.py ─► ../.claude/skills/icon-*/
```

There are six missions. Each folder below belongs to exactly one of them.

| Mission | Folders |
|---|---|
| 1. **Define the rules** | `model/contracts/`, `schemas/` |
| 2. **Model and author icons** | `model/`, `model/icons/` and its three family folders |
| 3. **Emit artifacts** | `renderers/`, `dist/`, `assets/` |
| 4. **Prove the rules were followed** | `validation/`, `tests/` |
| 5. **Operate: build, compose, review, prepare** | `scripts/`, `scripts_*.py` shims |
| 6. **Teach an agent to design** | `skills/`, `references/`, `../.claude/skills/` |

---

## 1. Define the rules

### `model/contracts/` — the single source of every number

Machine-readable, versioned, locked. Nothing in the Python restates a number
from here; `profiles.py` and `keyshapes.py` read these at import and assert
they agree with themselves.

| File | Holds | Who reads it |
|---|---|---|
| `icon-profile.v1.json` | The three **families** and their binding to a profile, folder, base class and dist folder. Per profile: canvas, interior guide inset, MIC, centerline minimum, rational keyshape scale. Global style (stroke 4, round caps and joins, grid 1) and the tolerances. | `model/profiles.py`, `model/contracts.py`, registry, validator, `build.py`, `generate_skills.py` |
| `keyshapes.v1.json` | The 10 base keyshape sizes and all 30 resolved definitions (10 per profile), plus the reserved `HRECT_XS` / `VRECT_XS` tokens. | `model/keyshapes.py`, validator check 5 |
| `exceptions.v1.json` | Every approved `FREE` keyshape use, keyed by `(icon_id, profile)`, with bounds, rationale, approval id and `status` (`proposed` / `approved`). | `model/icons/family.py` at construction, validator check 1 |
| `composition-templates.v1.json` | The four composition classes. `SOLO` and `CONTAINER_COMBINE` are frozen; the latter owns both child positions. Its protected slot was **withdrawn** on 2026-09-07 — the record and the reasoning stay in the file under `withdrawn_slot`. | `model/icons/combined.py`, `container/_base.py`, validator check 6, `compose.py` |
| `categories.json` | The category tree (`primitives/*`, `objects/*`, …). A *subject* taxonomy, orthogonal to family. | metadata only |

### `schemas/icon-record.schema.json`

JSON Schema for one published icon record: metadata plus the geometry AST,
never final path data. `family` and `profile` are both required. Every record in
every manifest conforms; `tests/test_schema.py` checks it.

---

## 2. Model and author icons

### `model/` — the runtime view of the contracts

| File | Mission |
|---|---|
| `contracts.py` | The one read path for the JSON: `icon_profile()`, `keyshapes()`, `exceptions()`, `composition_templates()`, `families()`, `family_for_profile()`, `approved_free_keyshapes()`. Cached. |
| `profiles.py` | `Profile` enum — `SUB32`, `SOLO48`, `CONTAINER64` — with `.spec` (canvas, MIC, guide, centre, scale), `.family`, and `Profile.for_family("solo")`. Also the style and tolerance constants. Asserts the contract's two tables agree. |
| `keyshapes.py` | `Keyshape` enum (CIRCLE, SQUARE, HRECT_*, VRECT_*, FREE) with exact 1× / 1.5× / 2× resolution per profile, `bounds_for(profile)`, radial helpers, `FreeKeyshapeSpec`, `approved_free_spec()`. Cross-checked against the contract at import. |
| `primitives.py` | The typed geometry AST: `Point`, `Line`, `Arc`, `Contour`, `Relationship`, `Position`, `ResolvedDrawing`, `translate()`, and dict (de)serialisation. The model's internal geometry and the interchange format are the same objects. |
| `position.py` | `PlacedIcon` — an icon bound to its integer translation inside a composition. |

### `model/icons/` — the authoring API and the three families

| File / folder | Mission |
|---|---|
| `base.py` | `Icon`: the authoring API. `add_line`, `add_arc`, `add_dot`, `add_polyline`, `add_contour`, `add_anchor`, `relate`; `draw()`, `to_svg()`, `export_icon_to()`, `validate_icon()`, `to_record()`. Carries `family`, `semantic_role`, `semantic_kind`, `category`, `aliases`, `keywords`. |
| `family.py` | `FamilyIcon`: the shared base of the three families. Resolves the **profile from the family name through the contract** — there is no profile attribute to override — looks up `FREE` records, places the `center` anchor, calls `build()`. |
| `sub/` | The **sub** family, `SUB32`, 32×32. `_base.py` defines `Sub32`. One module per icon (family modules `operators.py`, `shapes.py`, `arrows.py`, `chevrons.py`, `marks.py`, `free_glyphs.py` predate that rule and are read-only). 52 icons. |
| `solo/` | The **solo** family, `SOLO48`, 48×48. `_base.py` defines `Solo48`; 13 subjects live in one module per icon. |
| `container/` | The **container** family, `CONTAINER64`, 64×64. `_base.py` defines `Container64` and derives the content region from the contract, adding advisory `content-top-left` / `content-bottom-right` anchors. `shapes.py` (circle, square, rounded square, hexagon), `clipboard.py`, `browser_window.py`. |
| `combined.py` | `CombinedIcon`: a composition that owns placed children, flattens them with namespaced element ids (`<index>:<icon_id>:<element>`), and emits on `CONTAINER64` as family `container`. |
| `registry.py` | **Discovery by folder.** For each family in the contract, imports every public module in its folder and registers every `icon_id`-bearing subclass of that family's base. Refuses a class from another family (`TypeError` naming both). `all_icons()`, `icons_in(family)`, `create(icon_id)`, `icon_ids()`, `families()`. |

**To add an icon**: one new file in the right family folder, subclassing that
family's base. Nothing to register.

---

## 3. Emit artifacts

### `renderers/`

| File | Mission |
|---|---|
| `svg.py` | `build_paths()` groups primitives into `<path>` elements (a contour becomes one path with round joins; a loose primitive its own path with round caps) and refuses non-contiguous or unclosed contours. `render_svg()` emits the canonical document: exact viewBox, locked style, integer coordinates, no transforms. |
| `png.py` | `render_png()` rasterises the same scene at the native canvas (or an integer multiple) via `cairosvg`. |

### `dist/` — build output, one folder per family

| Folder | Contents |
|---|---|
| `dist/sub32/` | 52 SVGs + `manifest.json` (`family: sub`, `profile: SUB32`) |
| `dist/solo48/` | 13 SVGs + `manifest.json` (`family: solo`, `profile: SOLO48`) |
| `dist/container64/` | 5 SVGs + `manifest.json` (`family: container`, `profile: CONTAINER64`) |
| `dist/compositions/` | Output of `compose.py`: `<host>-<sub>.svg/.json/.png` |

Every folder is regenerated by `scripts/build.py`, which validates before it
writes and prunes outputs for icons that no longer exist. Rebuilding produces a
byte-identical tree. A consumer of one family never sees another's records.

### `assets/` — QA previews, not deliverables

| Folder | Contents |
|---|---|
| `assets/previews-png/<family><canvas>/` | Native-size PNG of every icon, written by `build.py` |
| `assets/previews-svg/contact-sheet*.svg` | Light and dark contact sheets from `contact_sheet.py` |

---

## 4. Prove the rules were followed

### `validation/` — the eight-check chain

| File | Mission |
|---|---|
| `library_qa.py`, `hole_geometry.py` | Library-wide spacing evidence, vendored rendered hole/pinch measurements, SVG/rule hashes, optional debug PNG/SVGs, JSON metrics, and searchable HTML. Rules come from `model/contracts/negative-space.v1.json`; source details are in `validation/PROVENANCE.md`. |
| `internal_spacing.py` | Non-blocking, sampled opposing-edge checks within a contour; reports sustained tight stretches and creates an annotated SVG overlay. |
| `structure.py` | Checks metadata constraints from the record schema and input geometry types before rendering or measurement; malformed inputs produce validation findings. |
| `validator.py` | `IconValidator.validate(icon)` runs the eight checks in locked order and returns a `ValidationReport`. 1 `schema/profile` (fields, enums, **family owns the profile**, FREE approval) · 2 `style/grid` · 3 `canvas/keyshape bounds` · 4 `mic` · 5 `keyshape` · 6 `composition` (roles, template, child profiles and positions) · 7 `svg round-trip` · 8 `reproducibility`. Never repairs or relaxes. |
| `envelope.py` | Exact painted-ink bounds: centerline extrema (arc axis extrema solved in closed form) grown by the stroke radius. Rectangle fit at tolerance 0 depends on this. |
| `stroke_distance.py` | The **MIC engine**, vendored. Exact rational predicates for straight pairs, bounded curve subdivision for arcs. Returns `pass` / `fail` / `review`; `review` is never a pass. |
| `slots.py` | Distance from centerline geometry to a *filled* rectangle; `intrusions()` lists ink that enters one. A measuring tool since the protected slot was withdrawn — used to report a container's headroom, no longer to reject it. |
| `path_commands.py` | Converts the geometry AST into the normalised path commands the MIC engine consumes, so the engine has no dependency outside this package. |
| `svg_reader.py` | Deliberately minimal strict parser for the documents we emit, used by the round-trip check to confirm viewBox, style, path data, and the absence of transforms. Not a general SVG parser. |
| `report.py` | `Finding`, `ValidationReport`, `CHECK_ORDER`. Every finding names its check and, where geometry is involved, the element id and coordinates. |

### `tests/` — 175 tests, stdlib `unittest`

```bash
python3 -m unittest discover -s icon_set/tests -t .
```

| File | Proves |
|---|---|
| `test_profiles_keyshapes.py` | Profile constants, the 30 keyshape resolutions, 1.5× / 2× exactness, reserved tokens, the one-to-one family binding, profile names = family + canvas. |
| `test_families.py` | Each family base authors on its own profile and cannot be overridden; the registry refuses a module in the wrong folder; the validator rejects a family/profile mismatch; unfamilied drafts never ship. |
| `test_corpus.py` | Every registered icon validates with no warnings, lives in its family's folder, ships its family's profile; each `dist/<family>/manifest.json` matches the registry and lists one profile; no legacy mixed folder remains. |
| `test_validator.py` | Each of the eight checks in isolation, including that a `connect` declaration excuses only its own pair and that `numeric_epsilon` is not a design tolerance. |
| `test_composition.py` | The frozen `CONTAINER_COMBINE` template: slot geometry, container intrusion, content overflow, positions, participant count, a noun may be content, a child's own spacing is not re-judged at the parent scale. |
| `test_model_and_renderers.py` | Authoring API, contour topology errors, AST round-trip, `CombinedIcon` parity and namespacing, canonical SVG, deterministic export, rejection of scale transforms. |
| `test_traced.py` | The `smartwatch` reconstruction: solo on `SOLO48`, fills `SQUARE`, one connected drawing, strap tips converge. |
| `test_schema.py` | Every record conforms to the schema (`jsonschema` if installed, structural fallback otherwise); `family` is required and bound to `profile`. |
| `test_references.py` | The Lucide bundle is intact — both views present, indexed and hash-matched, segment counts agreeing with `atomic-debug/` — and its inspector answers in this system's terms. |
| `test_skill_docs.py` | The shared skill docs: links resolve, quoted paths exist, quoted numbers match the contracts for all three profiles, the family table names every binding, no retired names. |
| `test_generated_skills.py` | The three `/icon-*` skills exist, are current with the generator, are pinned to one family each, and quote correct numbers. |

---

## 5. Operate

### `scripts/` — runnable entry points

| Script | Mission | Typical call |
|---|---|---|
| `validate_library.py` | Run spacing and hole/pinch QA over the current Python library without publishing; write `dist/qa/index.html`, metrics, and optional debug images. | `python3 icon_set/scripts/validate_library.py --debug` |
| `build.py` | Validate every icon of every family, then export SVG, PNG preview and a per-family manifest to `dist/<family><canvas>/`. Fails the whole build on one invalid icon, naming the element. Prunes stale outputs. Always runs hole/pinch QA; `debug=False`, `report=True` control evidence. | `python3 icon_set/scripts/build.py` · `--family solo` · `--no-png` |
| `compose.py` | Compose a container (64) with a sub (32) at the frozen template's positions into one validated `CONTAINER_COMBINE`, written to `dist/compositions/`. | `python3 icon_set/scripts/compose.py --host container-circle --sub heart --png` · `--list` |
| `contact_sheet.py` | Render a QA sheet: each icon enlarged over its keyshape and canvas guides, plus an unscaled native render, in light or dark. Filter by family. | `python3 icon_set/scripts/contact_sheet.py --family sub --theme dark --png /tmp/sub.png` |
| `generate_skills.py` | Render `/icon-sub`, `/icon-solo`, `/icon-container` from the contracts into `../.claude/skills/`. `--check` reports drift. | `python3 icon_set/scripts/generate_skills.py` |
| `lucide_reference.py` | Search the vendored Lucide bundle and read a reference in this system's terms: painted bounds, aspect ratio, suggested keyshape for a named profile, and the segment inventory from `atomic-debug/`. `atoms` lists one reference's segments; `search --kind` finds references built out of a given construction. | `python3 icon_set/scripts/lucide_reference.py inspect heart --profile SOLO48` · `atoms heart` · `search ring --kind arc/quarter-circle` |
| `profile_lab.py` | Measure a proposed profile number against every icon before committing to it: which stop validating and why, which gain or lose edge padding, whose interior detail crosses a moved guide, and how each icon's tightest clearance compares to a proposed MIC. Applies the proposal through `ICON_CONTRACT_OVERLAY` in a subprocess, so no locked contract is touched until `--write`. | `python3 icon_set/scripts/profile_lab.py show` · `try SOLO48.interior_guide_inset=8 --render` · `try CONTAINER64.mic=6 --write` |
| `prepare_references.py` | Rasterise a folder of reference SVGs (large and native-size), write a brief per icon from its manifest, contact sheets and an `index.html` worklist, so a batch can be triaged before authoring. | `python3 icon_set/scripts/prepare_references.py container_icons/svg --out container_icons/work --native 64` |
| `reconstruct.py` | The batch loop. `trace` measures each source **from its render** — bounds, aspect and the keyshape it points at, full-width and full-height rules, detached marks, corner rounding — and writes an authoring brief in the target canvas's units. `compare` scores each finished icon against its source (`fidelity`, tolerant of 2 units of stroke movement; `iou`, raw) and writes a worst-first ledger plus a source/authored/overlay panel per icon. `status` is the one-line progress count. | `python3 icon_set/scripts/reconstruct.py trace container_icons/svg` · `compare --family container` |

### `scripts_compose.py`, `scripts_lucide.py` — import shims

`scripts/` is a folder of entry points, not a package. These two files re-export
`compose.py` and `lucide_reference.py` as importable modules so the tests and
any library caller can use them.

---

## 6. Teach an agent to design

### `skills/icon-design/` — the shared technique library

The family-agnostic reference an agent reads while authoring. It never states a
family-specific number without naming the family.

| File | Mission |
|---|---|
| `SKILL.md` | Entry point: the three families and how to choose, the five steps, what may never be done, where things live, definition of done. |
| `intake.md` | Brief-only vs brief-plus-references; what a reference is and is not; preparing a folder; Lucide. |
| `naming.md` | Concept ids, aliases and keywords, supplied `sym-` ids, family suffixes, reserved variants, element ids. |
| `keyshape-fitting.md` | The exact envelope, the two fit tests, ready-to-use keyshape tables for all three profiles, traps, `FREE`. |
| `geometry.md` | The authoring API, contours and joins, arcs, and *the folder is the registry*. |
| `authoring.md` | Reduce, design backwards, tangent continuity, spacing, the repair ladder, optical judgement, native-size review. |
| `validation.md` | The eight checks, `review` is not `pass`, the repair loop, the never-list, commands. |
| `request-templates.md` | Copy-paste request forms. |

### `../.claude/skills/icon-{sub,solo,container}/SKILL.md` — the slash commands

Generated, one per family, pinned to one profile each. Invoke as `/icon-sub`,
`/icon-solo`, `/icon-container` with the brief as arguments. Each carries the
family's numbers and keyshape table, its folder, base class and dist, its
family-specific checks, and a hand-off line naming the other two skills for a
brief that belongs elsewhere. Regenerate after any contract change:

```bash
python3 icon_set/scripts/generate_skills.py
```

### `references/lucide/` — construction references

1,798 Lucide icons in two views, with `index.json`, `LICENSE` and
`PROVENANCE.md`. A construction reference for how a contour flows or a corner
turns, never a source to copy: Lucide is 2/24, this system is 4/32, and its
coordinates are fractional where ours are integers.

| | |
|---|---|
| `original/` | The drawing as Lucide ships it. |
| `atomic-debug/` | **The geometry reference.** The same icon split into one `<path>` per segment, tagged `data-atom` (`element.segment`), `data-src` (originating element) and `data-kind` (`line/horizontal`, `line/vertical`, `line/diagonal`, `arc/quarter-circle`, `arc/circular`, `arc/elliptical`, `cubic`, `quad`), coloured on a hue ramp. Says how an icon is built, where the outline only shows what it looks like. Analyser output — an inventory of the construction, not a part count to reproduce; it cuts a native circle into four quarter-arcs. `index.json`'s `segmentCount` / `segmentKinds` are counted from it and `test_references.py` asserts they still agree. |

Read both through `scripts/lucide_reference.py`: `inspect` for proportions and
the atom tally, `atoms` for the segment list, `search --kind` to find references
built out of a given construction.

---

## Where a task starts

| I want to… | Start at |
|---|---|
| Change a rule or a number | `model/contracts/*.json`, then run tests; docs and skills that quote it will fail until updated, and `generate_skills.py` regenerates the slash skills |
| Add a sub / solo / container icon | `/icon-sub`, `/icon-solo`, `/icon-container`, or a new file in `model/icons/<family>/` |
| Understand why an icon failed | `validation/validator.py` for the check, `report.describe()` for the element and coordinates |
| Ship | `scripts/build.py` → `dist/<family><canvas>/` |
| Compose a container with content | `scripts/compose.py` |
| Look at the set | `scripts/contact_sheet.py --family <family>` |
| Test a profile change (padding, MIC, keyshape size) | `scripts/profile_lab.py try <TARGET>.<field>=<value>`, then `--write` when the report is acceptable |
| Reconstruct a batch of reference drawings | `scripts/prepare_references.py` to look, `scripts/reconstruct.py trace` to measure, the family skill to author, `scripts/reconstruct.py compare` to check the result is the same picture |
| Check the skills teach what the contracts say | `tests/test_skill_docs.py`, `tests/test_generated_skills.py` |
