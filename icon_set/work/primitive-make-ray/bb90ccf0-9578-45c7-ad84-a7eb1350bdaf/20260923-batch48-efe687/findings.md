# squeeze sides

Phone with paired inward-bowing squeeze marks and a bottom separator.

## Keyshape

VRECT_M: The upright phone uses centerlines (10,4)–(38,44), visible ink (8,2)–(40,46).

## References

Input: `icon_set/work/todo-references/squeeze sides_bb90ccf0-9578-45c7-ad84-a7eb1350bdaf.svg`.

Construction: smartphone: rounded vertical enclosure. Local Lucide original and atomic-debug geometry were inspected where used; the human construction reference owns anatomy.

## Reduction

No defining feature intentionally omitted.

## Visual review

Four bowed squeeze strokes and footer retained. Outer echoes merge toward the phone walls; not visually approved. Reviewed at native 48px and enlarged size in both themes.

## Validation

```text
status: invalid
  ERROR  mic [phone]: phone and pressure--1 are 6 apart on centerlines nearest (10, 13)<->(16, 13); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [phone]: phone and echo--1 are 2 apart on centerlines nearest (10, 17)<->(12, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [phone]: phone and pressure-1 are 6 apart on centerlines nearest (38, 13)<->(32, 13); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [phone]: phone and echo-1 are 2 apart on centerlines nearest (38, 17)<->(36, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [pressure--1]: pressure--1 and echo--1 are 5.65685 apart on centerlines nearest (16, 13)<->(12, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [pressure--1]: pressure--1 and pressure-1 are 5.5 apart on centerlines nearest (21.25, 21)<->(26.75, 21); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [pressure-1]: pressure-1 and echo-1 are 5.65685 apart on centerlines nearest (32, 13)<->(36, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
