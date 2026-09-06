# Negative-space repair examples

Use these patterns after `core/qa_overlays.py` identifies an undersized enclosed
region or pinched junction. A failing measurement locates the problem; it does
not choose the repair. Examples use the built-in normal 48px canvas, 4px stroke,
keyshapes, and 1px radius/fill-depth defaults. For a changed or custom profile,
use its resolved JSON values rather than copying these illustrative numbers.

The shared order is structural/grid and declared-overlap prerequisites, then
distance → holes/pinches → keyshape, followed by native-size review. After any
repair, regenerate from the authoritative editable JSON, recheck prerequisites,
and restart at distance. Do not edit diagnostic SVG copies or carry forward
earlier passing reports for changed geometry.

## Repair ladder

Work in this order and stop at the first option that preserves recognition:

1. **Enlarge the opening.** Recompose the geometry that bounds it so the region gains room.
2. **Rebalance the composition.** Reduce the dominant part and enlarge the crowded identity-bearing detail.
3. **Remove the part.** Delete a complete non-essential element or semantic group. Record the omission.

Never push parts together until a hole disappears. That changes topology and creates a pinch rather than repairing the opening.

## The keyshape still controls every repair

The keyshape is the painted padding boundary. Record the declared token before
editing and validate it after fresh distance and hole/pinch passes:

These worked examples use default exact keyfit mode. For an agent-approved
[keyshape exception](icon-pipeline.md#keyshape-exceptions) justified by the subject
or prototype, use documented optical bounds and retain token containment instead
of inventing cardinal contacts. Optical mode cannot hide a failed negative-space
repair; all three gates and native-size review remain required.

```bash
python3 core/validate_icon_keyshapes.py <ship.svg> \
  --editable <editable-source.json> \
  --output-dir <keyshape-qa-folder>
```

| Keyshape | Boundary that must remain unchanged |
| --- | --- |
| `circle-44` | Paint reaches the four radius-22 cardinals and no paint enters the corner regions |
| `square-40` | Paint reaches and stays inside `(4,4)…(44,44)` |
| `portrait-36x44` | Paint reaches and stays inside `(6,2)…(42,46)` |
| `landscape-44x36` | Paint reaches and stays inside `(2,6)…(46,42)` |

An opening can pass while disconnected spacing fails or the keyshape becomes
undersized, offset, or crossed. All three gates must pass independently on the
same final geometry and resolved profile.

## Example A — remove a clipped secondary detail

A repeated stripe terminates against the inside of a `square-40` shell and creates a tiny enclosed pocket.

- Do not shorten an arbitrary fragment or move the stripe into the wall.
- Remove the complete stripe instance if the remaining repetition still communicates the subject.
- Confirm the outer shell still establishes all four square edges, so the painted keyshape remains `(4,4)…(44,44)`.

This is the cleanest use of rung 3: deleting interior detail does not change the keyshape when the silhouette establishes it.

## Example B — rebalance a landscape composition

A large vehicle body leaves too little room for an identity-bearing wheel opening inside `landscape-44x36`.

- Keep the landscape boundary fixed at `(2,6)…(46,42)`.
- Reduce the body locally and enlarge the complete wheel geometry.
- Redistribute the saved space around the wheel rather than globally scaling the icon.
- Recheck ordinary spacing, the hole gate, and the landscape edge contacts.

This is rung 2: the dominant part yields space so the smaller feature can remain honest.

## Example C — enlarge inside a portrait boundary

A narrow triangular opening near the top of a portrait icon fails the diameter gate, while unused room remains below it.

- Keep the portrait boundary `(6,2)…(42,46)`.
- Move the assembly within that boundary or move the lower closing edge away from the apex.
- Preserve the natural silhouette, optical balance, and symmetry.
- Do not push the two sloped members together at the tip.

This is rung 1: use available internal room without changing the selected keyshape.

## Example D — repair a circle without entering its corners

A radial detail near 45° needs more clearance inside `circle-44`.

- The painted circle boundary is radius 22 around `(24,24)`; its 44×44 bounding box is not usable corner space.
- Move the detail inward along its radius, reduce a non-identity-bearing neighbour, or simplify the radial group.
- Keep the icon touching the four cardinals while every painted sample remains inside the circle.
- Do not extend the detail toward `(2,2)`, `(46,2)`, `(46,46)`, or `(2,46)`; those points lie outside the keyshape.

Circle containment is a separate verification from rectangular painted bounds.

## Useful sizing math

Values below are native pixels and geometry units for the default 4px stroke
and 1px minimum enclosed radius:
**1u = 1px**, with no doubling or halving. An enclosed region passes at an
inscribed radius of at least `1u = 1px` (diameter `2u = 2px`).

| Opening | Inscribed radius after 4px stroke | Minimum geometry (u = px) |
| --- | --- | --- |
| Slot between parallel centerlines distance `d` | `(d - 4) / 2` | `d ≥ 6` |
| Centerline polygon with inradius `R` | `R - 2` | `R ≥ 3` |
| Right triangle with legs `a`,`b`, hypotenuse `c` | `(a + b - c)/2 - 2` | `a + b - c ≥ 6` |
| 45° right isosceles triangle with legs `a` | `a(2 - √2)/2 - 2` | `a ≥ 6/(2 - √2) ≈ 10.243` |
| Equilateral triangle side `s` | `s√3/6 - 2` | `s ≥ 6√3 ≈ 10.392` |
| Square side `s` | `s/2 - 2` | `s ≥ 6` |

For another profile, let `S = strokeWidth` and `r = minimumEnclosedRadius`.
A polygon's centerline inradius must be at least `r + S/2`; a parallel slot needs
`d ≥ S + 2r`. Apply the configured solid-fill-depth check independently.

These are the enclosed-hole floor, not the disconnected-line spacing rule or a
visual-opening target. For built-in normal icons, distinct components still
require 8px between centerlines (4px between 4px-wide ink); a hole-only `d ≥ 6`
example cannot waive that separate gate. A declared
identity-bearing opening still needs R5's 3px painted clearance: 7px between
Regular-stroke centerlines. Keep margin above rounded numerical thresholds.

A stroked V does not open at its centerline tip. Its painted inner apex sits farther inward, so sharp openings need more height than their centerline diagram suggests.

## Before calling the repair complete

- The distance gate has a fresh passing result on the repaired output.
- `core/qa_overlays.py` has a complete fresh passing result, zero undersized
  holes, zero pinches, and no processing/native-size errors.
- `validate_icon_keyshapes.py` passes the same declared keyshape on those bytes
  and the unchanged resolved profile; same-size output aliases also pass.
- Circle paint remains inside radius 22; rectangle paint remains inside its exact boundary.
- The icon still reaches all required cardinals or edges and stays centered.
- Grid, overlap, connection, and native-size reviews still pass (48×48 for these normal-icon examples).
- The repair can be named as enlarge, rebalance, or remove.

Missing, stale, failed, or unresolved-review evidence blocks completion. Resolve
checker errors and ambiguous intended joins instead of widening real connections
or weakening profile thresholds to obtain a pass.
