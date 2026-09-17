# Pictographic color rules

These rules capture the user's color-experiment decisions. They apply to color
variants across the existing icon families. The default theme is **Real-world
illustration**, defined in [color-theme.json](color-theme.json). Keep its exact
24 named swatches; black outlines and transparent negative space are separate
from those swatches.

## Choose color by subject and part

Identify the depicted part before choosing its token. Use recognizable material
and object colors: green foliage, blue water, brown wood, near-white paper,
dark lenses, metallic hardware. Abstract or unknown components may use
`ACCENT_GRAY`; genuinely gray materials may also use a suitable gray swatch.

Use one token for repeated regions of the same logical part. Different materials
or inherently different colors may receive different tokens. Do not alternate
shades simply because a surface was split into multiple polygons. Use flat,
solid colors; do not invent extra shades, gradients, lighting, or opacity-based
tints to extend the palette. Transparency is for actual openings.

For variable colors, use the theme's documented defaults unless context or the
user supplies a better choice. Blue clothing/vehicles, medium skin, brown hair,
and red gift wrap with a gold ribbon are illustration defaults, not universal
facts about the subject. Keep choices consistent for equivalent parts.

## Preserve outlines and junctions

- Outer outline strokes are pure black `#000000`, at the original width.
- Inner lines and elements may use theme colors or remain black. Do not force
  every stroke to black, and do not recolor a boundary merely because part of
  the same path runs through the interior.
- Paint surface fills first, then colored details, then the structural lines
  that must remain continuous at their contacts, and finally black outlines.
  Determine structural ownership from the drawing; one fixed source order is
  not reliable for every icon.
- Colored line caps must not cover the black border at shared endpoints. Put
  the outer contour above the colored stroke; if a detail still protrudes,
  clip or trim it to its region rather than widening or moving the outline.
- Keep inner supports and continuous bands unbroken. A book spine ends behind
  its shelf; a vertical corner seam does not interrupt a continuous gold band.
  Real crossings may have another ownership order when the subject calls for it.

## Distinguish a surface from an opening

An enclosed polygon is not automatically a solid part. Keep handle apertures,
frame openings, gaps, and other negative space transparent. Never paint them
white to imitate a hole. A baggage handle must read as a handle around open
space, not a solid rectangular extension of the case.

In metadata, represent an opening separately from a palette assignment
(`token: null`, paint/color `none` is acceptable). Do not add a fake
"transparent" swatch to the 24-color palette.

## Close a silhouette when color needs a boundary

When an open line-art silhouette represents a solid filled subject, add the
smallest sensible black closing line between its natural endpoints. Match the
source width, caps, joins, and native grid. Give the new fill a complete boundary
and keep the original outline paths intact.

Examples: close the wrist on the hand holding a torch before filling the skin;
close the bottom of the howling wolf's neck so its gray fill has a black base.

Do not close every open path automatically. Preserve intentional gaps, mouths
of vessels, holes, and open decorative marks. Closing a silhouette is a semantic
decision, not a blanket distance threshold between nearby endpoints.

## Allow meaningful creative regions

The color variant may add a small region that helps explain the object even if
the original has no separate path for it. For example, add blue liquid inside
the lower flask around a seedling. Follow the flask walls, keep the mouth open,
and paint the liquid behind the stem and outline. A liquid surface may be a flat
color boundary without an extra black divider.

Use the existing palette, preserve the subject's identity, and keep additions
inside their intended region. Prefer simple, readable shapes over decoration.
Record additions separately so they can be regenerated, reviewed, or removed.

## Reusable verification examples

| Example | Failure to avoid | Required visible result |
|---|---|---|
| Protective vest | Pocket endpoints covering the side border | Continuous black sides |
| Earth | Green continent strokes painting across the circular border | Unbroken black globe outline |
| Man at checkout counter | Tie covering shoulder or counter edges | Tie inside the black structure |
| Death Star equatorial trench | Colored trench caps cutting through the circle | Black circumference above the trench |
| Hand holding torch | Skin fill without a closed wrist | Minimal black wrist closure |
| Howling wolf profile | Filled neck ending on an unoutlined edge | Black base joining the neck endpoints |
| Seedling in laboratory flask | No region for liquid | Contained blue liquid with visible stem and open mouth |
| Baggage | Solid fill across the handle aperture | Transparent handle opening |
| Kaaba | Corner seam cutting the gold band | Continuous gold band |
| Bookcase | Book endpoints painted over the shelf | Continuous shelf in front of the book ends |

These are regression examples, not mandatory shapes or colors for unrelated
icons. Review native-size readability and enlarged intersections. Verify the
final exported SVG/PNG, not only a contact sheet or an intermediate drawing.
