# vaisakhi harvest

A Vaisakhi drum with two beaters and a wheat sprig.

Keyshape: **SQUARE**. The complete composition is distributed across a square envelope. The module records the exact profile bounds in `ink_extremes`.

Construction reference: drum: barrel silhouette and hoops; wheat: repeated diagonal stalk branches.

Omissions/reduction: None; drum, both beaters and stalk retained.

Validation: **invalid**, 7 errors, 0 warnings.

Visual review at 48px and enlarged, light and dark: **needs-review**. Drum, beaters and wheat are recognizable. Hoop endpoints are not joined cleanly to the curved wall; hoop and grain spacing remain insufficient.

status: invalid
  ERROR  mic [grain-high]: parallel straight edges grain-high and grain-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [drum]: parallel straight edges drum-top and hoop-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [hoop-1]: parallel straight edges hoop-1 and drum-bottom are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [beater-left]: beater-left and drum are 6 apart on centerlines nearest (16, 12)<->(16, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [beater-right]: beater-right and drum are 6 apart on centerlines nearest (26, 12)<->(26, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [drum]: drum and hoop-0 are 0.573174 apart on centerlines nearest (10.4371, 23.8919)<->(11, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [drum]: drum and hoop-1 are 0.780911 apart on centerlines nearest (10.2315, 36.1384)<->(11, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

[SVG](vaisakhi-harvest.svg) · [Python](vaisakhi_harvest_a0865ae5_c028_46f5_ade5_f26da83b22c2.py) · [Light preview](light-240.png) · [Dark preview](dark-240.png)
