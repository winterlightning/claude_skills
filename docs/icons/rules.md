# Normal icon rules

Use `normal` for a complete standalone icon. This page owns normal-specific
composition and badge policy. Apply the [shared visual rules](../shared/icon-rules.md)
for geometry, paint, spacing, connections, naming, and negative space; use
[profile.md](profile.md) for the generated canvas, stroke, center, and keyshape
values.

## Composition

- Declare `"iconType": "normal"` in every new editable source. Omission is
  supported only for backward compatibility.
- Author, export, and review at the configured `normal` canvas and stroke
  (built-in defaults 48×48px and 4px). Emit canonical `<name>.svg` at 1:1;
  do not create a half-size derivative.
- Prefer a few large, legible forms. Preserve
  the silhouette and one to three identity-bearing features; remove texture
  and incidental repetition. Feature guidance is not an element-count quota.
- Choose a normal keyshape from the dominant whole-icon silhouette. Declare
  `keyfitCheck.targetToken` and preserve its painted extent and containment.
  The agent may approve a subject- or prototype-justified
  [keyshape exception](../shared/icon-pipeline.md#keyshape-exceptions) using
  optical mode; do not distort the form merely to satisfy exact edge contacts.
- Review recognition, optical balance, and negative space at the exact native
  size in the resolved profile.

## Composite corner badges

A badge is a semantic modifier within a normal icon. It is distinct from a
standalone `sub` icon placed inside a container. The dimensions below are
composition guidance for the built-in 48px normal profile, not registry
constraints. If its canvas/keyshapes change, recompose the badge within the
configured keyshape and recheck spacing instead of blindly scaling final paths.

- Keep 4u canvas-edge padding.
- Fit the main symbol to a 32×32u box and use a 16u-diameter or nominal-box
  badge, approximately half the main symbol's size.
- The standard bottom-right badge center is `(32,32)`. A 16u circular badge at
  that center occupies `x=24…40`, `y=24…40`.
- Reposition the main symbol optically within the live area so both symbols
  remain legible. Apply shared R4/R5 to distinct-part spacing and overlap
  cutouts.

| Corner | Meaning |
| --- | --- |
| Bottom-right | Additive action |
| Top-right | Status |
| Bottom-left | Modifier |
| Top-left | Security |

Preserve the modifier's corner semantics. If the composition is crowded,
simplify or reposition the main symbol before changing a badge's corner.

## Delivery

Use a kebab-case name and deliver schema-version-2 editable JSON, the configured native SVG, and the evidence required by the [shared pipeline](../shared/icon-pipeline.md).
For symbol-library work, also apply [rework.md](rework.md); its brief review and
upload contract belong only to that input lane.
