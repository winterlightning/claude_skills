# Pictographic Icon System — Implementation Plan

**Status:** Implementation-ready roadmap; the profile constants below are locked, while keyshape dimensions remain the first design decision to freeze.  
**Goal:** Build an original, Python- and AI-assisted browser UI icon library with Lucide/Font Awesome-class consistency, discovery, packaging, and scale, growing in gated stages toward approximately 20,000 icons.

## 1. Product outcome

The finished system will provide:

- A coherent visual language across small, normal, and composite icons.
- Deterministic SVG generation from structured, reviewable geometry rather than arbitrary final paths.
- Automated checks for profile, grid, stroke, bounds, negative space, keyshape, composition, and metadata.
- AI agents that plan and propose icons within frozen rules, with bounded repair loops and human approval.
- Exact, visual, and semantic duplicate detection.
- A fast browser catalog with search, filters, comparison, copy/download, and QA views.
- Reproducible raw SVG, metadata, sprite, and developer-package releases.

Quality is enforced by versioned profile data and deterministic validators. Prompts and visual judgment supplement those contracts; they do not replace them.

## 2. Locked Icon Profile

### 2.1 Profiles and coordinates

| Profile | Semantic use | Drawing zone | Padding per side | Export canvas / `viewBox` | Drawing-zone bounds | Center |
|---|---|---:|---:|---:|---|---:|
| `SUB32` | Verb, state, or modifier | 32×32 | 4 | 40×40 | x/y 4–36 | 20,20 |
| `MAIN48` | Primary noun or standalone subject | 48×48 | 6 | 60×60 | x/y 6–54 | 30,30 |
| `COMPOSITE64` | Multi-part combination or diagram | 64×64 | 8 | 80×80 | x/y 8–72 | 40,40 |

The nominal size (`32`, `48`, or `64`) always names the **drawing zone**, never the SVG canvas. For every profile:

```text
export canvas = drawing size + (2 × padding)
```

The SVG uses top-left origin and final canvas coordinates. The drawing zone is the maximum ordinary visible-ink envelope. Padding is transparent export space and must not be treated as additional drawing or composition room. Validators inspect the rendered stroke envelope, not only path centerlines; with a centered 4-unit stroke, an ordinary outer centerline sits at least 2 units inside the drawing-zone edge. Any future optical overshoot must be an explicit, versioned exception.

When composing, do not nest a component's 40×40 or 60×60 export canvas. Place its profile-specific geometry by declared anchors inside the COMPOSITE64 drawing zone, then apply only the composite's outer padding.

### 2.2 Global style and grid

```yaml
grid: 1
snap_to_grid: true
authored_coordinates: integer
stroke_width: 4
stroke: currentColor
fill: none
line_cap: round
line_join: round
```

Stroke width is always 4 units for all profiles. Profiles change geometry and negative-space budgets, never stroke weight. Primary v1 artwork is outline-only; filled styles require a later, separately versioned profile.

### 2.3 Minimum ink clearance

MIC is the shortest visible empty distance between otherwise distinct pieces of rendered ink.

| Profile | MIC | Minimum equal-stroke centerline spacing |
|---|---:|---:|
| `SUB32` | 3 | 7 |
| `MAIN48` | 4 | 8 |
| `COMPOSITE64` | 6 | 10 |

For two 4-unit strokes:

```text
minimum centerline spacing = MIC + stroke width
```

Thus the consistent centerline values are 7/8/10. They are a convenient equal-stroke check; the authoritative general test measures actual vector ink outlines, including curves, joins, and round endcaps. Intended connections, contacts, occlusions, or knockouts must be declared narrowly in relationship metadata rather than bypassing MIC globally.

### 2.4 Profile-specific optical rendering

One semantic concept may have separate `SUB32`, `MAIN48`, and `COMPOSITE64` siblings. Each is authored and reviewed for its target profile: simplify details, rebalance negative space, and reposition features as needed while keeping stroke width 4.

Published variants must not be produced by proportionally scaling another SVG. The DSL and emitted SVG reject scale transforms. Composition may use integer translation through named anchors, then flatten placements into final coordinates; a fit failure requests a new optical variant or a revised composition.

## 3. Keyshape and composition model

### 3.1 Keyshapes

The standard keyshape catalog is:

- `CIRCLE`
- `SQUARE`
- `HRECT_XS`, `HRECT_S`, `HRECT_M`, `HRECT_L`, `HRECT_XL`
- `VRECT_XS`, `VRECT_S`, `VRECT_M`, `VRECT_L`, `VRECT_XL`
- `FREE` — exceptional shape only

Exact dimensions are deliberately not invented in this plan. Milestone M1 freezes all 12 standard keyshapes for each profile (36 definitions), including width, height, centering, anchors, tolerance, and measurement basis. The recommended basis to evaluate during the golden-icon study is visible-ink bounds, because MIC and drawing-zone rules are also ink-based.

Horizontal rectangles must be wider than tall, vertical rectangles taller than wide, and the long dimension must increase strictly from XS through XL. `FREE` has no standard dimensions and always requires a specific rationale plus human approval. It never waives the grid, 4-unit stroke, MIC, or drawing-zone rules.

### 3.2 Composition classes and semantic roles

| Class | Contract |
|---|---|
| `SOLO` | One independently readable concept in an explicitly authored profile. |
| `SIDE_COMBINE` | A MAIN noun and a SUB verb/state/modifier placed beside one another. |
| `CONTAINER_COMBINE` | A MAIN noun or container encloses, hosts, or carries a SUB element. |
| `DIAGRAM_COMBINE` | Multiple elements and connectors express flow, hierarchy, structure, or another relationship. |

`MAIN` means **noun**. `SUB` means **verb, state, or modifier**. `COMPOSITE64` is a composition space, not a third semantic role. Every composition declares its class, participants and roles, keyshapes, anchors, intended contacts, occlusion order, and component optical-variant versions. Combined classes normally emit COMPOSITE64; any exception must be defined by a frozen template rather than inferred by an agent.

## 4. Technical architecture

Canonical profile, taxonomy, and geometry records are source; SVGs and previews are build artifacts.

```text
taxonomy backlog → concept/spec agent → profile-specific geometry DSL
                 → deterministic Python compiler → validators
                 → visual critic + bounded repair → dedupe + human review
                 → packages, search index, and browser catalog
```

Recommended repository layout, using the existing `icon_set` area:

```text
icon_set/
  model/
    profiles/icon-profile.v1.yaml
    keyshapes/keyshapes.v1.yaml
    compositions/composition-templates.v1.yaml
    taxonomy/categories.yaml
    concepts/
    icons/
  schemas/
    icon-source.schema.json
  pictographic/
    dsl/
    compiler/
    validation/
    composition/
    agents/
    dedupe/
  assets/
    figma/
    fixtures/
    previews/
  web/
  dist/
```

Use typed Python models (for example, Pydantic) as runtime contracts and publish JSON Schema for interchange. Keep arithmetic and geometry invariants in semantic validators rather than duplicating derived numbers by hand.

A minimal profile source should encode the locked values directly:

```yaml
schema_version: 1.0.0
units: design-unit
coordinates: {origin: top-left, grid: 1, snap: true}
style:
  stroke: {width: 4, color: currentColor, cap: round, join: round}
  fill: none
profiles:
  SUB32:       {drawing_size: 32, padding: 4, export_size: 40, mic: 3, equal_stroke_centerline_min: 7}
  MAIN48:      {drawing_size: 48, padding: 6, export_size: 60, mic: 4, equal_stroke_centerline_min: 8}
  COMPOSITE64: {drawing_size: 64, padding: 8, export_size: 80, mic: 6, equal_stroke_centerline_min: 10}
```

Each icon record needs a stable ID, canonical kebab-case name, aliases, taxonomy, semantic roles, composition class, supported profiles, keyshape, separate per-profile DSL geometry, declared relationships/exceptions, validation and review state, and profile/keyshape/compiler/prompt/model provenance.

The geometry DSL should be a structured AST, not an opaque SVG path string. V1 primitives should cover line, polyline, circle, ellipse, rectangle, rounded rectangle, arcs, and explicit path commands. Elements receive stable IDs, semantic groups, layers, anchors, and relationships. Global style is inherited and per-element stroke overrides are rejected.

## 5. Validation and composition contracts

Run validation in a fixed order with element IDs and actionable coordinates in every failure:

1. **Schema/profile:** required fields, enums, compatible versions, and exact constants.
2. **Style/grid:** integer authored coordinates, grid 1, stroke 4, round cap/join, `currentColor`, and no fill.
3. **Stroke-aware bounds:** full visible ink stays inside the drawing zone; padding stays clear.
4. **MIC:** vector-outline distance meets 3/4/6 after only declared connections are grouped.
5. **Keyshape:** frozen token exists, dimensions and tolerance match, or an approved `FREE` record exists.
6. **Composition:** roles, slot cardinality, anchors, contacts, occlusions, and output profile follow a frozen template.
7. **SVG round-trip:** exact `viewBox`, canonical style, no scale/matrix transform, no clipping, and identical results after reparse.
8. **Reproducibility:** identical source and tool versions produce byte-identical normalized SVGs and manifests.

The composition engine is constraint-driven: resolve a template and output profile; fetch the required optical variants; align named anchors with integer translations; solve bounds, MIC, and relationship constraints; flatten placements; then run the entire validator chain. If no solution exists, return a structured conflict. Never fix a layout by scaling, thinning the stroke, moving off-grid, or lowering MIC.

Minimum acceptance fixtures include:

- Reject canvas 41, stroke 3 or 6, half-grid coordinates, butt caps, miter joins, and ink in padding.
- In SUB32, a horizontal centerline from `(6,20)` to `(34,20)` with round stroke 4 paints to x=4–36 and passes; extending it to x=5 paints to x=3 and fails.
- Equal-width stroke centerline separations of 7/8/10 pass for SUB32/MAIN48/COMPOSITE64; 6/7/9 fail. Cover parallel shafts and round endcaps.
- An undeclared contact fails; the same intentional contact with a narrowly scoped `connect` relationship passes.
- MAIN+modifier and SUB+noun fail semantic validation; MAIN+noun plus SUB+state in a valid template passes.
- Missing keyshape definitions, invalid H/V orientation, broken XS–XL ordering, and unreviewed `FREE` usage fail release validation.
- A scaled group fails even if its final stroke is reset to 4; flattened integer translation passes.
- An unsatisfiable composition returns a deterministic diagnostic without mutating any locked rule.

## 6. Phased milestones

| Milestone | Primary deliverables | Exit gate |
|---|---|---|
| **M0 — Baseline and golden set** | Decision log; repository/test skeleton; 50–75 diverse reference icons and invalid fixtures covering profiles, roles, keyshapes, and compositions. | Locked rules exist once in machine-readable form; open decisions are marked; CI runs tests and snapshots. |
| **M1 — Freeze keyshape dimensions** | 36 standard profile/keyshape definitions; measurement basis; tolerances; anchors; attachment/overshoot rules; examples and counterexamples. | No unresolved standard-keyshape dimension; golden sheet is approved at native and common browser sizes. |
| **M2 — Figma templates** | Exact 40/60/80 frames; drawing-zone, padding, center, grid, keyshape, MIC, and composition guides; export presets. | Generated fixture round-trips through Figma without canvas, stroke, or alignment drift. |
| **M3 — Icon Profile schema** | Versioned profile, keyshape, icon-source, exception, and composition schemas; migration policy; generated docs. | Invalid constants and roles are rejected; 40/60/80 and 7/8/10 invariants are computed and verified. |
| **M4 — Geometry DSL/compiler** | Structured DSL; deterministic Python renderer; normalized SVG serializer; canonical hashes and preview sheets. | Clean rebuild is byte-stable; outputs have exact style/canvas; no profile variant uses scaling. |
| **M5 — Validators** | Schema, grid/style, stroke-aware bounds, MIC, keyshape, composition, metadata, and round-trip validators with positive/negative fixtures. | Every locked rule has a passing and failing test; no invalid fixture reaches packaging. |
| **M6 — Composition engine** | Frozen templates and slots for all four classes; anchor placement, collision/MIC solving, occlusion/knockout handling, and golden compositions. | All class examples pass; MAIN/SUB roles are enforced; failures are diagnostic rather than silently altered. |
| **M7 — Category/taxonomy plan** | Category tree; canonical naming/alias rules; search keywords; coverage matrix; concept-brief schema; prioritized backlog. This can start alongside M1–M3. | Every planned icon has one canonical concept ID; synonyms become aliases, not duplicate jobs; bulk generation backlog is approved. |
| **M8 — AI-agent pilot** | Spec planner, DSL generator, critic/repair, naming, dedupe, and catalog agents; versioned prompts; reproducible job manifests; bounded retries. | Three consecutive 100-icon batches reach at least 95% acceptance after one repair cycle, with zero profile-rule violations. |
| **M9 — Dedupe and visual QA** | Normalized geometry hashes; raster/perceptual and semantic similarity; review UI; overlays and contact sheets; resolution states. | Exact duplicates are zero; every near-duplicate is resolved as `merge`, `alias`, `distinct`, or `profile-sibling`; unexplained snapshot diffs are zero. |
| **M10 — Packaging and browser catalog** | Raw SVGs, metadata, sprite, tree-shakeable typed ESM package, React adapter, search index, catalog UI, docs, versioning/deprecation policy. | One-icon import includes only that icon; builds are reproducible; users obtain explicit unscaled profile assets; fixed-query top-five search recall is at least 90%. |
| **M11 — Scale to ~20k** | Gated catalog expansion, virtualized browser, lazy search data, release automation, category gap reporting, and support policy. | Complete validation/provenance, no unresolved duplicates, acceptable batch quality, and reproducible release from a clean checkout. |

Bulk generation must wait for M1–M5 and the golden fixtures. Taxonomy work may proceed in parallel, but its naming and concept model must freeze before the agent pilot.

## 7. AI production, dedupe, and visual QA

Agents may propose concepts and DSL geometry but cannot modify frozen profile/keyshape rules. Every job records its inputs, source/model/prompt versions, candidate geometry, validation output, repair history, review decision, and final artifact hashes. Limit automated repair attempts; persistent failures return to specification instead of accumulating ad hoc exceptions.

Use three duplicate layers:

1. **Exact geometry:** normalize coordinates, transforms, ordering, and attributes, then hash.
2. **Visual similarity:** compare standard monochrome renders using perceptual hashes, contours, and image similarity.
3. **Semantic similarity:** compare canonical names, aliases, categories, briefs, and embeddings.

Profile-specific optical siblings are intentional variants, not duplicates. Reviewers store `merge`, `alias`, `distinct`, or `profile-sibling` with a rationale; candidates are never silently discarded.

Every icon receives automated QA plus light/dark renders, true 40/60/80 export-size previews, common browser-size previews, category contact sheets, and profile-family comparisons. Detailed human review is mandatory for all icons through the initial 2,000-icon alpha and always for compositions, `FREE`, validator warnings, and dedupe candidates. Sampling of remaining straightforward icons may decrease only after three clean batches; all still receive contact-sheet triage.

## 8. Packaging and browser delivery

Initial outputs:

- `@pictographic/icons`: direct per-icon imports and tree-shakeable typed ESM modules.
- `@pictographic/metadata`: canonical names, aliases, categories, roles, profiles, and search data.
- Versioned raw SVG archive organized by concept ID and explicit profile.
- SVG sprite and manifest with hashes, provenance, replacements, and deprecations.
- React adapter first; add Vue, Svelte, or web components only when demand justifies them.
- Static browser catalog with search, filters, profile comparison, icon detail, copy/download, code snippets, and QA overlays.

The runtime API must accept explicit profile selection. A documented `auto` policy may choose among existing profile-specific drawings, but it must never present scaled geometry as a native profile.

## 9. Scale-up gates and quality metrics

Expand by quality gate, not generation speed:

| Stage | Catalog target | Required focus before advancing |
|---|---:|---|
| Pilot | ~100 | All standard keyshapes and composition classes represented; validators and repair loop calibrated. |
| Alpha | ~1,000 | Representative categories; complete human review; taxonomy and dedupe thresholds stabilized. |
| Internal release | ~2,000 | Search/browser usable; packaging/API stable enough for internal consumers. |
| Beta | ~5,000 | Core browser UI coverage; release automation; no unresolved QA or duplicate backlog. |
| Breadth | ~10,000 | Long-tail categories and aliases; three clean production batches. |
| Target | ~20,000 | Complete corpus checks; virtualized catalog; migration, deprecation, and support workflows. |

Increase batch size from 100 to 250, 500, and then 1,000 only after three consecutive batches meet the current gates. A failure pauses the affected category or generator version while unaffected work can continue.

Release gates:

- Machine validation and required metadata/provenance completeness: **100%**.
- Exact duplicates, unresolved near-duplicate decisions, undocumented `FREE` uses, and unexplained golden-image diffs: **0**.
- Normalized SVG/manifest reproducibility from identical inputs: **100%**.
- AI pilot acceptance after one repair cycle: **at least 95%** across three consecutive batches.
- Fixed-query search benchmark: **at least 90% top-five recall**.
- Browser search: target **under 100 ms p95** on an agreed reference device at catalog scale.
- Breaking profile or public API changes: major versions only, with migration metadata.

Track acceptance, repairs, exceptions, duplicates, and regressions by category, keyshape, profile, composition class, and generator version; catalog-wide averages can hide weak segments.

## 10. Definition of done for one icon

An icon is publishable only when:

- Its canonical concept ID, name, category, aliases, and semantic roles are approved.
- Every claimed profile has separately authored and optically reviewed geometry.
- DSL and metadata match the current versioned schemas.
- Stroke, grid, ink bounds, padding, MIC, keyshape, composition, and SVG round-trip checks pass.
- Every intended contact, occlusion, or exception is explicit and justified.
- Exact, visual, and semantic duplicate decisions are resolved.
- Native and browser-size renders pass visual QA.
- SVG, manifest, search entry, and packages rebuild reproducibly.
- No profile is derived through naive SVG scaling.

## 11. Immediate execution order

1. Commit the locked profile source, schema skeleton, arithmetic tests, and decision log.
2. Produce the 50–75 golden-icon set and use it to freeze the 36 standard keyshape definitions.
3. Generate matching Figma templates directly from the frozen profile/keyshape data.
4. Implement the smallest DSL/compiler slice and all hard validators before expanding primitive coverage.
5. Prove all four composition classes with golden fixtures.
6. Freeze taxonomy/naming, run the 100-icon agent pilot, calibrate QA/dedupe, then advance only through the scale gates.
