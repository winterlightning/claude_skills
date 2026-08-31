# Negative-space repair examples

Use these patterns after `core/qa_overlays.py` identifies an undersized enclosed region or pinched junction. A failing measurement tells you where the problem is; it does not choose the repair.

## Repair ladder

Work in this order and stop at the first option that preserves recognition:

1. **Enlarge the opening.** Move or resize the atoms that bound it so the region gains room.
2. **Rebalance the composition.** Reduce the dominant part and enlarge the crowded identity-bearing detail.
3. **Remove the part.** Delete a complete non-essential element, semantic group, or atom instance. Record the omission.

Never push parts together until a hole disappears. That changes topology and creates a pinch rather than repairing the opening.

## The keyshape still controls every repair

The keyshape is the painted padding boundary. Record the declared token before editing and validate the same token afterward:

```bash
python3 core/check_keyfit.py <ship.svg> \
  --expected-editable-dir <editable-json-folder> \
  --output-dir <keyshape-qa-folder>
```

| Keyshape | Boundary that must remain unchanged |
| --- | --- |
| `circle-44` | Paint reaches the four radius-22 cardinals and no paint enters the corner regions |
| `square-40` | Paint reaches and stays inside `(4,4)…(44,44)` |
| `portrait-36x44` | Paint reaches and stays inside `(6,2)…(42,46)` |
| `landscape-44x36` | Paint reaches and stays inside `(2,6)…(46,42)` |

An opening can pass while the keyshape becomes undersized, offset, or crossed. Both gates must pass independently.

## Example A — remove a clipped secondary detail

A repeated stripe terminates against the inside of a `square-40` shell and creates a tiny enclosed pocket.

- Do not shorten an arbitrary fragment or move the stripe into the wall.
- Remove the complete stripe instance if the remaining repetition still communicates the subject.
- Confirm the outer shell still establishes all four square edges, so the painted keyshape remains `(4,4)…(44,44)`.

This is the cleanest use of rung 3: deleting interior detail does not change the keyshape when the silhouette establishes it.

## Example B — rebalance a landscape composition

A large vehicle body leaves too little room for an identity-bearing wheel opening inside `landscape-44x36`.

- Keep the landscape boundary fixed at `(2,6)…(46,42)`.
- Reduce the body locally and enlarge the complete wheel atom.
- Redistribute the saved space around the wheel rather than globally scaling the icon.
- Recheck ordinary spacing, the hole gate, and the landscape edge contacts.

This is rung 2: the dominant part yields space so the smaller feature can remain honest.

## Example C — enlarge inside a portrait boundary

A narrow triangular opening near the top of a portrait icon fails the diameter gate, while unused room remains below it.

- Keep the portrait boundary `(6,2)…(42,46)`.
- Move the assembly within that boundary or move the lower closing edge away from the apex.
- Preserve the allowed line angles and symmetry.
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

Values below are ship pixels at the Regular 2px stroke; double them for design units. An enclosed region passes at an inscribed radius of at least `0.5px = 1u design`.

| Opening | Inscribed radius after 2px stroke | Minimum geometry |
| --- | --- | --- |
| Slot between parallel centerlines distance `d` | `(d - 2) / 2` | `d ≥ 3px` (6u design centerline distance) |
| Centerline polygon with inradius `R` | `R - 1` | `R ≥ 1.5px` |
| Right triangle with legs `a`,`b`, hypotenuse `c` | `(a + b - c)/2 - 1` | `a + b - c ≥ 3px` |
| 45° right isosceles triangle with legs `a` | `0.293a - 1` | `a ≥ 5.12px` |
| Equilateral triangle side `s` | `0.289s - 1` | `s ≥ 5.20px` |
| Square side `s` | `s/2 - 1` | `s ≥ 3px` |

A stroked V does not open at its centerline tip. Its painted inner apex sits farther inward, so sharp openings need more height than their centerline diagram suggests.

## Before calling the repair complete

- `core/qa_overlays.py` reports zero undersized holes and zero pinches.
- `check_keyfit.py` passes the same declared keyshape.
- Circle paint remains inside radius 22; rectangle paint remains inside its exact boundary.
- The icon still reaches all required cardinals or edges and stays centered.
- Grid, angle, overlap, connection, and true-size 24px reviews still pass.
- The repair can be named as enlarge, rebalance, or remove.
