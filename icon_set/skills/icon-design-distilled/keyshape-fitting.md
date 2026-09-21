# Keyshape fitting

Rectangle keyshapes fit at **tolerance zero**. Round caps and joins mean the painted region is the centerline grown by exactly 2 on every side, so **author to the centerline box** and the visible bounds follow.

- Rectangle family (`SQUARE`, `HRECT_*`, `VRECT_*`): visible bounding box must equal the keyshape bounds. Reach all four.
- `CIRCLE`: radial test. All ink within R of centre, max extent at least R - 0.5. A star can use it.

Ask the model: `Keyshape.HRECT_L.bounds_for(Profile.SOLO48)`, `Profile.for_family("solo").spec.center`.

**SUB32** (canvas 32, ink clearance 3, centerline min 7). Centerline boxes: CIRCLE r14 about (16,16); SQUARE (2,2)-(30,30); HRECT_XL (2,4)-(30,28); HRECT_L (2,6)-(30,26); HRECT_M (2,8)-(30,24); HRECT_S (2,10)-(30,22); VRECT_XL (4,2)-(28,30); VRECT_L (6,2)-(26,30); VRECT_M (8,2)-(24,30); VRECT_S (10,2)-(22,30).

**SOLO48** (canvas 48, ink clearance 4, centerline min 8). CIRCLE r20 about (24,24); SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40); HRECT_M (4,10)-(44,38); VRECT_L (8,4)-(40,44); VRECT_M (10,4)-(38,44). `_XL`/`_S` resolve to `_L` here; never choose them for new work.

**CONTAINER64** (canvas 64, ink clearance 4, centerline min 8). CIRCLE r30 about (32,32); SQUARE (2,2)-(62,62); HRECT_XL (2,6)-(62,58); HRECT_L (2,10)-(62,54); HRECT_M (2,14)-(62,50); HRECT_S (2,18)-(62,46); VRECT_XL (6,2)-(58,62); VRECT_L (10,2)-(54,62); VRECT_M (14,2)-(50,62); VRECT_S (18,2)-(46,62).

`HRECT_XS`/`VRECT_XS` raise.

**Traps:**
- Regular polygons have no integer vertices. Snap to nearest grid point; CIRCLE only needs one vertex to reach R. Prefer exact constructions (octagon as chamfered square).
- Curves need margin. A curve exactly on the minimum returns `review`. A 4-wide mark between two walls needs 16 between wall centerlines, 17 if a wall is curved. If the band is short, change keyshape or drop the mark.
- Reaching a bound mid-arc works only if the centre is exact. Pick the integer radius whose apex is the endpoint on the box.
- Cannot fit upright: try a diagonal construction on integer points. Still no fit: keep the findings, flag **Exception, manual review** in the gallery, record attempted layouts. The flag waives nothing.

**FREE** is for subjects with no possible keyshape (e.g. `minus`, `dot`: a 4-unit axis has no token). Add a record keyed by `(icon_id, profile)` to `icon_set/model/contracts/exceptions.v1.json` with `bounds`, a subject-specific `rationale`, `approval_id`, `status: "proposed"`. Only a human sets `approved`, which release requires. Reject it for undersizing, poor centring or dodging a repair. FREE waives the keyshape fit only.
