# browser with 18+ text

Retain bindings, header and horizontal 18+; rebalance digit and operator spacing without dropping characters.

## Provenance

Source UUID: `fc5ffdff-80e9-4119-bf62-fb7c515c5aad`.
Input: `icon_set/work/todo-references/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg`.
Prior result: `icon_set/work/primitive-make-ray/fc5ffdff-80e9-4119-bf62-fb7c515c5aad/20260923-b06-a3379238/result.json` (invalid).

## Keyshape

SQUARE: Visible ink (4,4)–(44,44), centerline envelope (6,6)–(42,42), balances the complete composition.

## Construction references

calendar: repeated binding posts, quarter-round frame and header rule. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

No defining feature intentionally omitted.

## Visual review

All three characters and the two-binding enclosure remain. The 8 and plus still crowd neighboring characters and the frame; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [calendar-body]: parallel straight edges calendar-body-0 and plus-vertical-1, plus-vertical-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [calendar-body]: calendar-body and one are 6 apart on centerlines nearest (6, 26)<->(12, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [header]: header and eight-top are 5 apart on centerlines nearest (23, 18)<->(23, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [calendar-body]: calendar-body and eight-bottom are 7 apart on centerlines nearest (23, 42)<->(23, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [calendar-body]: calendar-body and plus-horizontal are 3 apart on centerlines nearest (42, 30)<->(39, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [one]: one and eight-top are 6 apart on centerlines nearest (14, 26)<->(20, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [one]: one and eight-bottom are 6 apart on centerlines nearest (14, 32)<->(20, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eight-top]: eight-top and plus-horizontal are 7.77064 apart on centerlines nearest (25.7716, 27.1481)<->(33, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eight-bottom]: eight-bottom and plus-horizontal are 7.19804 apart on centerlines nearest (25.9424, 31.4147)<->(33, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
