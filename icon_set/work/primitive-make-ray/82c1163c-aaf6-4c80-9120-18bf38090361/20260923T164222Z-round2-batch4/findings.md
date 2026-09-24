# cog double 1

Two equal toothed gears on a rising diagonal.

**SQUARE**: The overall composition uses the 36 by36 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: cog: repeated radial teeth and circular hubs, generated from shared quarter geometry.

Reduction: None; the eight teeth and center hole of each gear are retained.

Validation: **invalid**, 12 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Eight teeth and both gear hubs are restored after the four-tooth trial looked insufficiently gear-like. Tooth valleys and hub clearances remain too tight; not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [gear-1]: parallel straight edges gear-1-2 and gear-1-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-1]: parallel straight edges gear-1-16 and gear-1-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-0]: parallel straight edges gear-0-2 and gear-0-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-0]: parallel straight edges gear-0-16 and gear-0-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-1]: parallel straight edges gear-1-26 and gear-1-24 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-1]: parallel straight edges gear-1-8 and gear-1-10 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-0]: parallel straight edges gear-0-26 and gear-0-24 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-0]: parallel straight edges gear-0-8 and gear-0-10 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-1]: parallel straight edges gear-1-21 and gear-0-5 are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [gear-0]: gear-0 and hub-0 are 4.15613 apart on centerlines nearest (11.8587, 26.5707)<->(13.7173, 30.288); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [gear-0]: gear-0 and gear-1 are 7.07107 apart on centerlines nearest (21, 26)<->(26, 21); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [gear-1]: gear-1 and hub-1 are 4.15613 apart on centerlines nearest (36.1413, 8.57067)<->(34.2827, 12.288); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](cog-double-1.svg) · [Python](cog_double_1_82c1163c_aaf6_4c80_9120_18bf38090361.py) · [Light](light-240.png) · [Dark](dark-240.png)
