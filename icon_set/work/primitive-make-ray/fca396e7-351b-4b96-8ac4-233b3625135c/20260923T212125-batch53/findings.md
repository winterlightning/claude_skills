# user cash scale

A person and a dollar coin balanced on a seesaw.

Keyshape: **SQUARE**. The complete composition is distributed across a square envelope. The module records the exact profile bounds in `ink_extremes`.

Construction reference: scale: horizontal balance and fulcrum; human_ref/user.svg: circular head and shoulder apex.

Omissions/reduction: Small arm/leg outline steps simplified; coin, dollar and fulcrum retained.

Validation: **invalid**, 4 errors, 1 warnings.

Visual review at 48px and enlarged, light and dark: **needs-review**. The dollar overlaps the coin and the person nearly merges with the beam. The complete composition is retained, but the native negative space is inadequate.

Human reference: `icon_set/skills/icon-design/human-reference.md; icon_set/references/human_ref/user.svg`. Detached head bottom y=14, torso top y=22: 8 centerline units / 4 ink units.

status: invalid
  ERROR  mic [person-body]: parallel straight edges person-bottom-left, person-bottom-right and beam-1, beam-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [person-body]: person-body and beam are 2 apart on centerlines nearest (6, 30)<->(6, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [beam]: beam and coin are 4 apart on centerlines nearest (34, 32)<->(34, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [beam]: beam and dollar-stem are 3 apart on centerlines nearest (34, 32)<->(34, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [coin]: coin and dollar-stem are 0 apart on centerlines nearest (34, 12)<->(34, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

[SVG](user-cash-scale.svg) · [Python](user_cash_scale_fca396e7_351b_4b96_8ac4_233b3625135c.py) · [Light preview](light-240.png) · [Dark preview](dark-240.png)
