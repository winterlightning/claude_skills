# truck moving

Moving truck carrying a house above its cargo box.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/truck moving_1bdf40bf-9d96-43bd-a767-f5237c9e61eb.svg`.

truck and house: wheel pair, peaked roof and doorway. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

No defining feature intentionally omitted.

## Visual review

House, doorway, cargo body and both wheels retained. Door and lower chassis clearances close at native size; not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [house-walls]: parallel straight edges house-walls-3 and door-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [door]: parallel straight edges door-1 and house-walls-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [door]: parallel straight edges door-2 and house-walls-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cargo]: parallel straight edges cargo-2 and chassis are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [house-roof]: house-roof and house-walls are 0.312348 apart on centerlines nearest (10.8049, 11.7561)<->(11, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
