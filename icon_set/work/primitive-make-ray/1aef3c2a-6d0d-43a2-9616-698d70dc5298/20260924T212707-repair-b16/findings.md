# monitor-small-squares

Tall monitor with two equal squares stacked vertically.

Keyshape: VRECT_L; ink bounds (6, 2, 42, 46).

Reductions: Horizontal stand foot omitted in last attempt.

Construction references: Lucide monitor: enclosure and central support; repeated square definition.

Native and enlarged review, both themes: Not approved: lower square remains too close to screen bottom. Both squares retained.

status: invalid
  ERROR  mic [square-1]: parallel straight edges square-1-3 and screen-4, screen-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [screen]: screen and square-1 are 4 apart on centerlines nearest (25, 40)<->(25, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

BUILD GATE FAIL (fail, 2 errors, 0 warnings)
  error: mic [square-1]: parallel straight edges square-1-3 and screen-4, screen-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  error: mic [screen]: screen and square-1 are 4 apart on centerlines nearest (25, 40)<->(25, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
