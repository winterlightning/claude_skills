# stepdaughter

Girl with long hair and circular lower-right relationship badge.

## Keyshape

SQUARE: The full composition uses a balanced 36 by 36 centerline envelope, visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/stepdaughter_7bead6c0-72f2-44e3-81e8-617544d2ab4d.svg`.

Construction: human_ref/user.svg: circular jaw and broad shoulder construction. Local Lucide original and atomic-debug geometry were inspected where used; the human construction reference owns anatomy.

## Reduction

- Continuous neck replaced by the required detached head/shoulder layout.

## Visual review

Long hair, circular jaw and badge retained. Hair-to-face and hair-to-shoulder gaps fail; not visually approved. Reviewed at native 48px and enlarged size in both themes.

Circular head/jaw bottom centerline y=22; own upper shoulder centerline y=30; 30-22-4 = 4 units visible ink gap. Hair clearance is a separate failure for the two long-haired portraits.

## Validation

```text
status: invalid
  ERROR  mic [shoulders]: shoulders and hair-left are 1.31371 apart on centerlines nearest (8.92893, 32.9289)<->(8, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [face]: face and hair-top are 3.05524 apart on centerlines nearest (14, 14)<->(11.2543, 12.6599); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
