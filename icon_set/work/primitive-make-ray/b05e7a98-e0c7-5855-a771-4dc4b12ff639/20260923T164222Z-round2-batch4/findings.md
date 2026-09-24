# crop rotate

Crossing crop corners with opposing rotation arrows.

**SQUARE**: The overall composition uses the 36 by36 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: crop: shared crossing nodes; rotate-ccw: quarter arcs with compact corner arrowheads.

Reduction: Chevron arrowheads changed to right-angle arrowheads; both rotation arrows retained.

Validation: **valid**, 0 errors, 0 warnings.

Visual review at48px and240px in light and dark: **approved**. Both crop corners and rotation arrows remain distinct. Shared crossing nodes and mirrored quarter arcs are clean in both themes; compact right-angle arrowheads preserve the opposing directions.

Exact unresolved checks, elements and coordinates:

```text
status: valid
```

[SVG](crop-rotate.svg) · [Python](crop_rotate_b05e7a98_e0c7_5855_a771_4dc4b12ff639.py) · [Light](light-240.png) · [Dark](dark-240.png)
