# stack unstack column

A descending staircase of stacked column cells with two downward curved arrows.

## Keyshape

SQUARE: The full composition uses a balanced 36 by 36 centerline envelope, visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/stack unstack column_ff75519b-afd0-4da5-b995-1999fe2b031a.svg`.

Construction: No useful Lucide subject match; shared cell widths and repeated arrow construction. Local Lucide original and atomic-debug geometry were inspected where used; the human construction reference owns anatomy.

## Reduction

No defining feature intentionally omitted.

## Visual review

Five cells and both curved arrows retained. Middle cells and arrow clearances are too tight; not visually approved. Reviewed at native 48px and enlarged size in both themes.

## Validation

```text
status: invalid
  ERROR  mic [column-middle]: parallel straight edges column-middle-1 and divider-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [divider-middle]: parallel straight edges divider-middle and column-middle-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [column-middle]: column-middle and first-curve are 6 apart on centerlines nearest (22, 22)<->(28, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [column-bottom]: column-bottom and second-curve are 6 apart on centerlines nearest (30, 38)<->(36, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [first-tip]: first-tip and second-curve are 4 apart on centerlines nearest (32, 26)<->(36, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
