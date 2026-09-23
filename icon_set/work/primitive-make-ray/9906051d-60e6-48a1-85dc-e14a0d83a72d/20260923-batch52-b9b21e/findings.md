# turn 1

Diamond traffic sign with opposing branches on an outlined vertical route.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/turn 1_9906051d-60e6-48a1-85dc-e14a0d83a72d.svg`.

signpost: coherent outlined arrow corners; intentional opposing branches. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

No defining feature intentionally omitted.

## Visual review

Diamond and opposed route branches retained. Narrow outlined route closes under the fixed stroke; not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [route]: parallel straight edges route-5 and route-7 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [route]: parallel straight edges route-11 and route-8 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [diamond]: parallel straight edges diamond-1 and route-3 are 6.36396 apart on centerlines (ink gap 2.36396); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [route]: parallel straight edges route-9 and diamond-3 are 4.94975 apart on centerlines (ink gap 0.949747); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [diamond]: diamond and route are 3.53553 apart on centerlines nearest (29.5, 36.5)<->(27, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
