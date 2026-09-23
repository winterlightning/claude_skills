# real estate favorite house rating

A house beneath a large central rating star and two smaller stars.

Keyshape: SQUARE. Equal width and height preserve the full scene or enclosing composition.

Three five-point stars sit above a symmetric pitched-roof house. Ink extremes (4,4)-(44,44).

Construction reference: star: five-point outline; house: mirrored roof and doorway.

Omissions/reductions: None; all three stars and the doorway are retained.

Visual review: House and three-star arrangement remain visible, but small side-star counters close and the doorway and roof gaps crowd. Not visually approved.

Human construction: Not applicable.

Validation: **invalid**; outcome: **failed-validation**

```text
status: invalid
  ERROR  mic [house]: parallel straight edges walls-right-3 and walls-right-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [house]: parallel straight edges walls-right-1 and walls-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [house]: parallel straight edges walls-3 and walls-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [main-star]: main-star and star-0 are 4.43877 apart on centerlines nearest (18.3784, 19.7297)<->(14, 19); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main-star]: main-star and star-1 are 4.43877 apart on centerlines nearest (29.6216, 19.7297)<->(34, 19); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main-star]: main-star and roof are 4.47214 apart on centerlines nearest (22, 20)<->(24, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [star-0]: star-0 and roof are 5.26965 apart on centerlines nearest (13, 25)<->(15.9231, 29.3846); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [star-1]: star-1 and roof are 5.26965 apart on centerlines nearest (35, 25)<->(32.0769, 29.3846); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [roof]: roof and house are 2.7735 apart on centerlines nearest (12.4615, 31.6923)<->(14, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `f53e79c7-b34f-44d2-9af3-49b5684cc631`.
