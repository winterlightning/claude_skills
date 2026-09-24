# card game heart

Three hearts on an upright playing card; reduce the central suit while preserving both opposing corner marks.

## Provenance

Source UUID: `2d678d4e-3c28-4171-9206-0e44c564a983`.
Input: `icon_set/work/todo-references/card game heart_2d678d4e-3c28-4171-9206-0e44c564a983.svg`.
Prior result: `icon_set/work/primitive-make-ray/2d678d4e-3c28-4171-9206-0e44c564a983/20260922T222359-37f3f9/result.json` (invalid).

## Keyshape

VRECT_L: Visible ink (6,2)–(42,46), centerline envelope (8,4)–(40,44), preserves the upright sheet/card and gives vertical content room.

## Construction references

heart: paired lobes and opposing suit orientation. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

No defining feature intentionally omitted.

## Visual review

Main heart and the opposing corner hearts remain. Reducing the main heart leaves the corner marks too close to the card walls; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [card]: card and upper are 5 apart on centerlines nearest (8, 13)<->(13, 13); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [card]: card and lower are 5 apart on centerlines nearest (40, 35)<->(35, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main]: main and upper are 5.06311 apart on centerlines nearest (19.4956, 21.4053)<->(17, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main]: main and lower are 4.94975 apart on centerlines nearest (24, 31)<->(27.5, 34.5); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
