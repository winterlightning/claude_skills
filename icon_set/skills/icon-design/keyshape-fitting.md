# Hitting the keyshape exactly

The rectangle-family fit runs at **tolerance zero**. Painted bounds must equal
the keyshape's bounds. This is achievable rather than harsh, and here is why.

## The envelope is exact

Every cap and every join is round, so the painted region is exactly the
centerline plus a disc of radius 2. Therefore:

```
visible bounds = centerline bounds grown by exactly 2 on all four sides
```

So to reach a visible edge at `x = 0`, put a centerline point at `x = 2`. No
estimation is involved.

## Two different fit tests

**Rectangle family** (`SQUARE`, `HRECT_*`, `VRECT_*`) — the visible bounding box
must **equal** the keyshape bounds. Reach all four.

**`CIRCLE`** — a radial test, not a bounding box. All ink within radius `R` of
the canvas centre, and maximum radial extent at least `R - 0.5` so the artwork
touches. This is why a five-point star can use `CIRCLE`: it has no ink at the
bounding box's corners, and its bbox is not square.

SOLO48 has centered visible-ink envelopes: circle 44×44, square 40×40,
landscape 44×36 and portrait 36×44 — four keyshapes: `CIRCLE`, `SQUARE`,
`HRECT_L` and `VRECT_L` (the contract's `keyshape_choices`). The other
rectangle size tokens exist only so older modules still resolve; on SOLO48 they
give the same bounds as `HRECT_L`/`VRECT_L`. Never choose one for new work.
SUB32 and CONTAINER64 retain their own tables.

SOLO48 spacing is **4 units between ink edges, or 8 between centerlines**
for 4-unit strokes. The validator enforces this for parallel straight edges
inside a single contour as well as for separate paths. The internal straight
check measures exact perpendicular distance where non-adjacent segments have
positive overlap; shared endpoints and ordinary joins are excluded. Curved or
near-parallel internal edges retain the sampled review advisory.

## The numbers, ready to use

For a subject that cannot fit upright, try diagonal construction when it keeps
the subject recognizable. Recompute integer points and shared joins; rotation
does not waive the envelope or clearance rules. If no fit works, record the
reason and attempted layouts and use **Exception — manual review** in the
gallery's Flag selector (`exception`). Retain all validation findings and do
not describe the icon as valid or approved. A custom envelope still uses the
existing FREE proposal/approval process; a flag grants no rule exemption and
does not allow ink outside the canvas.

The centerline box is the one you author to. SOLO48 uses explicit profile
sizes; CONTAINER64 uses twice the SUB32 base dimensions. Drawings are separately
authored, never scaled, because the stroke stays 4 and the grid stays 1.

### `sub` — `SUB32`, canvas 32, MIC 3, centerline minimum 7

| Keyshape | Visible | Centerline box |
|---|---|---|
| `CIRCLE` | radius 16 about (16,16) | radius 14 |
| `SQUARE` | (0,0)-(32,32) | (2,2)-(30,30) |
| `HRECT_XL` | (0,2)-(32,30) | (2,4)-(30,28) |
| `HRECT_L` | (0,4)-(32,28) | (2,6)-(30,26) |
| `HRECT_M` | (0,6)-(32,26) | (2,8)-(30,24) |
| `HRECT_S` | (0,8)-(32,24) | (2,10)-(30,22) |
| `VRECT_XL` | (2,0)-(30,32) | (4,2)-(28,30) |
| `VRECT_L` | (4,0)-(28,32) | (6,2)-(26,30) |
| `VRECT_M` | (6,0)-(26,32) | (8,2)-(24,30) |
| `VRECT_S` | (8,0)-(24,32) | (10,2)-(22,30) |

### `solo` — `SOLO48`, canvas 48, MIC 4, centerline minimum 8

| Keyshape | Visible | Centerline box |
|---|---|---|
| `CIRCLE` | radius 22 about (24,24) | radius 20 |
| `SQUARE` | (4,4)-(44,44) | (6,6)-(42,42) |
| `HRECT_L` | (2,6)-(46,42) | (4,8)-(44,40) |
| `VRECT_L` | (6,2)-(42,46) | (8,4)-(40,44) |

### `container` — `CONTAINER64`, canvas 64, MIC 4, centerline minimum 8

| Keyshape | Visible | Centerline box |
|---|---|---|
| `CIRCLE` | radius 32 about (32,32) | radius 30 |
| `SQUARE` | (0,0)-(64,64) | (2,2)-(62,62) |
| `HRECT_XL` | (0,4)-(64,60) | (2,6)-(62,58) |
| `HRECT_L` | (0,8)-(64,56) | (2,10)-(62,54) |
| `HRECT_M` | (0,12)-(64,52) | (2,14)-(62,50) |
| `HRECT_S` | (0,16)-(64,48) | (2,18)-(62,46) |
| `VRECT_XL` | (4,0)-(60,64) | (6,2)-(58,62) |
| `VRECT_L` | (8,0)-(56,64) | (10,2)-(54,62) |
| `VRECT_M` | (12,0)-(52,64) | (14,2)-(50,62) |
| `VRECT_S` | (16,0)-(48,64) | (18,2)-(46,62) |

Ask the model rather than doing the arithmetic by hand:

```python
Keyshape.HRECT_L.bounds_for(Profile.SOLO48)   # (2, 6, 46, 42)
Profile.for_family("solo").spec.center        # (24, 24)
```

`HRECT_XS` and `VRECT_XS` are reserved identifiers. Requesting one raises.

## Traps that cost a cycle each

**Regular polygons have no integer vertices.** A regular pentagon or five-point
star at any useful radius lands on fractions. Place vertices on the nearest grid
point to the true radius — the `CIRCLE` touch rule accepts it, since only one
vertex has to reach `R`. Where an exact alternative exists, prefer it: the
`octagon` is authored as a chamfered square, so every vertex is exact.

**Curved parts need real clearance margin.** See
[authoring.md](authoring.md#spacing). A curve exactly on the minimum returns
`review`, not `pass`. This bites at 48 in particular: a 4-unit mark between two
walls needs 16 between the wall centerlines, 17 when a wall is curved, and the
SOLO48 centerline boxes are only 36×36 (`SQUARE`) or 40×32 (`HRECT_L`/`VRECT_L`).
A band that is short cannot be fixed by squeezing; change the keyshape or drop
the mark.

**Reaching a bound mid-arc works, but only if the centre is exact.** An arc's
axis extremum is measured exactly, so a semicircle whose centre is an integer
point reaches its extreme exactly. An arc whose endpoints do not sit on the
intended ellipse gives a centre with a fractional part and misses. Pick the
integer radius whose apex *is* the endpoint that sits on the centerline box, so
the arc lands on the bound instead of overshooting it.

## When nothing fits: `FREE`

Some subjects fit no keyshape at all. Six do in this set — `minus`, `bar`,
`dot`, `exclamation`, `ellipsis`, `dots-vertical` — because their short axis is
entirely stroke-defined at 4 units and the smallest standard minor dimension is
16. Nothing is wrong with them; there is simply no token for a 4-unit axis.

`FREE` is the recorded escape hatch, not a way around a failure.

**Approve it when** exact fitting would distort the subject or weaken
recognition, and the natural form reads well at native size.

**Reject it when** the mismatch is accidental undersizing, poor centring,
unfinished geometry, or an attempt to avoid a repair. Fix the icon instead.

To use it, add a record to `icon_set/model/contracts/exceptions.v1.json`. The
record is keyed by `(icon_id, profile)`, and the profile is the family's:

```json
{
  "icon_id": "minus",
  "profile": "SUB32",
  "bounds": [0, 14, 32, 18],
  "rationale": "1-D bar glyph. The short axis is entirely stroke-defined at 4 units; no standard keyshape has a 4-unit axis, and the smallest standard minor dimension is 16.",
  "approval_id": "FREE-2026-09-07-001",
  "status": "proposed"
}
```

Write `status: "proposed"`. You can author and validate against a proposed
record in a draft run, but the release path — which the build script uses —
requires `approved`, and only a human sets that. The rationale must be specific
to this subject; "does not fit" is not a rationale.

`FREE` waives the keyshape fit and nothing else. Canvas, grid, stroke, clearance
and native-size review all still apply.
