# couple polaroid image

A Polaroid photograph of a couple beneath a heart.

**VRECT_L**: The upright composition uses the 32 by40 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: image: coherent photo frame; human_ref/user.svg: paired circular heads and smooth shoulders.

Reduction: None; both people and the heart retained.

Validation: **invalid**, 5 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Both heads, shoulders, heart and Polaroid frame remain. The heart and heads lack clearance, and the body shapes are shallow. Not approved.

Human construction evidence:

```json
{
  "reference": "icon_set/references/human_ref/user.svg",
  "figures": 2,
  "head_centers": [
    [
      17,
      22
    ],
    [
      31,
      22
    ]
  ],
  "radius": 3,
  "head_bottom": 25,
  "shoulder_apex_y": 33,
  "centerline_gap": 8,
  "ink_gap": 4,
  "construction": "Outlined busts, not stick figures. Actual head/body spacing retained; surrounding composition fails."
}
```

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [frame]: frame and head-0 are 6 apart on centerlines nearest (8, 22)<->(14, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [frame]: frame and head-1 are 6 apart on centerlines nearest (40, 22)<->(34, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [frame]: frame and heart are 5.11909 apart on centerlines nearest (20.6076, 4)<->(20.6076, 9.11909); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head-0]: head-0 and heart are 5.15605 apart on centerlines nearest (18.9032, 19.681)<->(22.1755, 15.6964); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head-1]: head-1 and heart are 5.15605 apart on centerlines nearest (29.0968, 19.681)<->(25.8245, 15.6964); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](couple-polaroid-image.svg) · [Python](couple_polaroid_image_e2c5bf0f_5995_5267_b0b2_06ba6ad56a64.py) · [Light](light-240.png) · [Dark](dark-240.png)
