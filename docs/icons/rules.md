# Normal icon rules

Use `normal` for a complete standalone icon. This page owns normal-specific
composition and badge policy. Apply the [shared visual rules](../shared/icon-rules.md)
for geometry, paint, spacing, connections, naming, and negative space; use
[profile.md](profile.md) for the generated canvas, stroke, center, and keyshape
values.

## Composition

- Declare `"iconType": "normal"` in every new editable source. Omission is
  supported only for backward compatibility.
- Author directly on the normal design canvas and emit its exact design/ship
  pair through the shared pipeline.
- Prefer a few large, legible forms. Preserve
  the silhouette and one to three identity-bearing features; remove texture
  and incidental repetition. Feature guidance is not an element-count quota.
- Choose a normal keyshape from the dominant whole-icon silhouette. Declare
  `keyfitCheck.targetToken` and preserve its painted extent and containment.
  Intrinsically thin/sparse subjects may use shared R1's documented optical mode;
  do not stretch them to all four edges merely to satisfy exact mode.
- Review recognition, optical balance, and negative space at the exact ship
  size in the generated profile.

## Composite corner badges

A badge is a semantic modifier within a normal icon. It is distinct from a
standalone `sub` icon placed inside a container.

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

Use a kebab-case name and deliver schema-version-2 editable JSON, both canonical SVG
sizes, and the evidence required by the [shared pipeline](../shared/icon-pipeline.md).
For symbol-library work, also apply [rework.md](rework.md); its brief review and
upload contract belong only to that input lane.
