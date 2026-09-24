# book person

A book carrying a circular head over curved arms and a torso.

**VRECT_L**: Upright envelope supplies 40 centerline units of height for stacked or nested parts. Exact visible bounds are recorded by `ink_extremes` in the module.

Construction references: book-user: book cover and pages; human_ref/user.svg and full_body_ref.png: circular head and coherent human strokes.

Reduction: None; book, head, raised arms and torso retained.

Validation: **review**, 0 errors, 2 warnings.

Visual review: **needs review**, inspected at 48px and enlarged in light and dark. Book, circular head and curved arms remain recognizable. Torso is much shorter than the source and the head-to-arms equality remains a numeric warning. Exact detached gap is retained, but not approved.

Human construction evidence:

{
  "reference": "icon_set/references/human_ref/user.svg; icon_set/references/human_ref/full_body_ref.png",
  "head_center": [
    24,
    16
  ],
  "radius": 3,
  "head_bottom": 19,
  "torso_start": [
    24,
    27
  ],
  "centerline_gap": 8,
  "visible_ink_gap": 4,
  "flags": "person/head/torso-1/start",
  "limitation": "Head/arms sampled equality remains a warning; short torso is a visual compromise."
}

Validation findings:

```text
status: review
  WARN   mic [book]: book and arms are 8 apart on centerlines nearest (8, 24)<->(16, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [head]: head and arms are 7.99992 apart on centerlines nearest (24, 19)<->(24.0368, 26.9998); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](book-person.svg) · [Python](book_person_8ed961c5_a996_4c78_a7d6_d1d6baa41755.py) · [Light](light-240.png) · [Dark](dark-240.png)
