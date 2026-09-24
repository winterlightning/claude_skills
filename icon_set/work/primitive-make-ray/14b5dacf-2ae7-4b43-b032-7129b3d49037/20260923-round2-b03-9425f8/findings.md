# calendar math

Three-binding calendar with 2+1; redistribute the three glyphs across a wide keyshape.

## Provenance

Source UUID: `14b5dacf-2ae7-4b43-b032-7129b3d49037`.
Input: `icon_set/work/todo-references/calendar math_14b5dacf-2ae7-4b43-b032-7129b3d49037.svg`.
Prior result: `icon_set/work/primitive-make-ray/14b5dacf-2ae7-4b43-b032-7129b3d49037/20260923-b06-3c258fc8/result.json` (invalid).

## Keyshape

HRECT_L: Visible ink (2,6)–(46,42), centerline envelope (4,8)–(44,40), gives the horizontal composition more width.

## Construction references

calendar: repeated bindings and shared enclosure corners. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

No defining feature intentionally omitted.

## Visual review

All three calendar bindings and horizontal 2+1 remain. Wider frame improves overall spacing but the right digit and operator still crowd adjacent geometry; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [calendar-body]: parallel straight edges calendar-body-0 and one-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [calendar-body]: calendar-body and one are 5 apart on centerlines nearest (44, 20)<->(39, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [two]: two and plus-horizontal are 7.36983 apart on centerlines nearest (19.8526, 24.203)<->(27, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [plus-horizontal]: plus-horizontal and one are 7.2111 apart on centerlines nearest (31, 26)<->(37, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
