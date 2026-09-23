# outdoors dog house

A standing dog underneath a sloping outdoor shelter.

Keyshape: SQUARE. Equal width and height fit the complete scene or enclosing frame.

One lean-to outline encloses a coherent dog silhouette with ear, muzzle, back, belly and legs. Ink extremes (4,4)-(44,44).

Construction references: dog: coherent animal contour and purposeful pointed ear; input owns the full-body pose.

Omissions/reductions: Rear far leg omitted; near hind leg and front leg retained.

Visual review: The dog and shelter remain identifiable, but paws merge toward the floor and the rear leg crowds the wall. Not visually approved; MIC failures are retained.

Human construction: Not applicable.

Validation: **invalid**

```text
status: invalid
  ERROR  mic [dog]: parallel straight edges dog-hind-leg-2 and shelter-2 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [dog]: parallel straight edges dog-hind-leg-1 and shelter-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [dog]: parallel straight edges dog-front-leg-2 and shelter-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [shelter]: shelter and dog are 4 apart on centerlines nearest (13, 42)<->(13, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `176149f5-709e-4aea-827c-9e372966aa1a`.
