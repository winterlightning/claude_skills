# squeeze sides

Hand grips a phone while two arrows point inward; four repeated fingers and a curved thumb.

## Keyshape

SQUARE: The full composition uses a balanced 36 by 36 centerline envelope, visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg`.

Construction: smartphone and move-horizontal: rounded phone and arrow strokes. Local Lucide original and atomic-debug geometry were inspected where used; the human construction reference owns anatomy.

## Reduction

- Phone footer separator omitted to reduce crowding; thumb and wrist simplified.

## Visual review

Four finger loops, opposed arrows, thumb and wrist retained. Finger interiors and nearby marks crowd at native size; not visually approved. Reviewed at native 48px and enlarged size in both themes.

## Validation

```text
status: invalid
  ERROR  mic [finger-0]: parallel straight edges finger-0-0 and finger-0-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-0]: parallel straight edges finger-0-0 and finger-1-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-0]: parallel straight edges finger-0-4 and finger-1-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-0]: parallel straight edges finger-0-4 and finger-2-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-1]: parallel straight edges finger-1-0 and finger-1-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-1]: parallel straight edges finger-1-0 and finger-2-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-1]: parallel straight edges finger-1-4 and finger-2-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-1]: parallel straight edges finger-1-4 and finger-3-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-2]: parallel straight edges finger-2-0 and finger-2-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-2]: parallel straight edges finger-2-0 and finger-3-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-2]: parallel straight edges finger-2-4 and finger-3-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [finger-3]: parallel straight edges finger-3-0 and finger-3-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [phone]: phone and wrist are 0.472232 apart on centerlines nearest (33.5756, 39.7929)<->(34, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [finger-0]: finger-0 and left-arrow are 4.07107 apart on centerlines nearest (8.87868, 16.8787)<->(6, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [phone]: phone and right-arrow are 4 apart on centerlines nearest (34, 10)<->(38, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [thumb]: thumb and right-arrow are 7.51588 apart on centerlines nearest (36.2339, 18.863)<->(41.5485, 13.5485); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [phone]: phone and thumb are 0 apart on centerlines nearest (34, 18)<->(34, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
