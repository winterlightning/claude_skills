# passport globe

A passport showing a globe in front of a larger world globe.

Keyshape: SQUARE. Equal width and height fit the complete scene or enclosing frame.

Large globe is occluded by the foreground passport; the cover carries a small gridded globe. Ink extremes (4,4)-(44,44).

Construction references: globe: circular outline, elliptical meridian and equator; book: foreground cover.

Omissions/reductions: Tiny continental bends reduced; both the world globe and passport-cover globe are retained.

Visual review: World globe and foreground passport remain recognizable as a composition, but the tiny cover globe loses its grid at 48px and reads as a solid disk. Not visually approved; retained as an unsuccessful fit.

Human construction: Not applicable.

Validation: **invalid**

```text
status: invalid
  ERROR  mic [passport]: parallel straight edges passport-6 and continent-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [continent]: parallel straight edges continent-1 and continent-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [world]: world and globe are 5.40184 apart on centerlines nearest (20, 34)<->(25.2173, 32.6003); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [continent]: continent and passport are 6 apart on centerlines nearest (14, 26)<->(20, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [passport]: passport and globe are 5 apart on centerlines nearest (31, 42)<->(31, 37); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `df632f40-c8e3-4ae9-9986-caca559c4210`.
