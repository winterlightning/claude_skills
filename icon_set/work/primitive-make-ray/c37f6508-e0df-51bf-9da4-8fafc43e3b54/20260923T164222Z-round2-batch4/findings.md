# death rip

An arched gravestone marked RIP on a rectangular plinth.

**VRECT_L**: The upright composition uses the 32 by40 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: No useful exact tombstone original; coherent arch and hand-authored RIP letter contours.

Reduction: None; all three letters retained.

Validation: **invalid**, 8 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. RIP lettering, arched stone and base remain recognizable. The R and P counters are weak, and letters crowd one another and the stone walls. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [stone]: parallel straight edges stone-right and p-stem-2, p-stem-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [p-stem]: parallel straight edges p-stem-2, p-stem-1 and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [r-stem]: parallel straight edges r-stem-2, r-stem-1 and stone-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [stone]: stone and r-stem are 6 apart on centerlines nearest (10, 29)<->(16, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [stone]: stone and p-bowl are 3 apart on centerlines nearest (38, 22)<->(35, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [plinth]: plinth and i are 7 apart on centerlines nearest (25, 36)<->(25, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [r-leg]: r-leg and i are 4 apart on centerlines nearest (21, 29)<->(25, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [p-stem]: p-stem and i are 6 apart on centerlines nearest (31, 29)<->(25, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](death-rip.svg) · [Python](death_rip_c37f6508_e0df_51bf_9da4_8fafc43e3b54.py) · [Light](light-240.png) · [Dark](dark-240.png)
