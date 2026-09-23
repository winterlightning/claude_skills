# tv retro

Retro television with rabbit-ear antenna, inset screen, two buttons and two feet.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/tv retro_f213d74b-e15b-42ab-953a-a7a36392d15b.svg`.

tv: antenna junction and rounded cabinet. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

No defining feature intentionally omitted.

## Visual review

Antenna, cabinet, inset screen, two buttons and both feet retained. Nested gaps and button spacing fail; not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [display]: parallel straight edges display-6 and cabinet-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cabinet]: parallel straight edges cabinet-0 and display-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [display]: parallel straight edges display-4 and cabinet-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cabinet]: cabinet and display are 6 apart on centerlines nearest (15, 14)<->(15, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [cabinet]: cabinet and button-0 are 4 apart on centerlines nearest (42, 22)<->(38, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [cabinet]: cabinet and button-1 are 4 apart on centerlines nearest (42, 30)<->(38, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [display]: display and button-0 are 4.05623 apart on centerlines nearest (29.9856, 22.7059)<->(34.0113, 22.2094); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [display]: display and button-1 are 4.05623 apart on centerlines nearest (29.9856, 29.2941)<->(34.0113, 29.7906); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [button-0]: button-0 and button-1 are 4 apart on centerlines nearest (36, 24)<->(36, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
