# business card hand 3

Hand holding a portrait business card; flatten the upper hand clearance and shorten the shoulder bowl while retaining the portrait.

## Provenance

Source UUID: `bcaaf2a2-b7c9-450b-836e-e0c294ab0564`.
Input: `icon_set/work/todo-references/business card hand 3_bcaaf2a2-b7c9-450b-836e-e0c294ab0564.svg`.
Prior result: `icon_set/work/primitive-make-ray/bcaaf2a2-b7c9-450b-836e-e0c294ab0564/20260922T221840-dd88b8/result.json` (invalid).

## Keyshape

SQUARE: Visible ink (4,4)–(44,44), centerline envelope (6,6)–(42,42), balances the complete composition.

## Construction references

hand and human_ref/user.svg: rounded hand contours, circular portrait head and curved shoulders. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

- Upper hand/back contour straightened to increase clearance above the card.

## Visual review

Portrait head and shoulders, card, gripping thumb and upper hand outline remain. Thumb-to-head and shoulder-to-card clearances still fail; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

{"path": "icon_set/references/human_ref/user.svg", "gap_evidence": "Head center (16,23), radius 3, lowest centerline y=26. Shoulder ellipse upper apex (16,34). 34-26-4 = 4 visible ink units. The separate thumb and card clearance failures remain."}

## Validation

```text
status: invalid
  ERROR  mic [thumb]: thumb and head are 5.86607 apart on centerlines nearest (24.3507, 25.9787)<->(18.8246, 24.0107); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [card]: card and shoulders are 5 apart on centerlines nearest (12, 42)<->(12, 37); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
