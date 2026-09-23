# tv circle check

Television on a central stand with a circled check inside.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg`.

monitor and circle: rounded screen, central stand and circular status mark. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

No defining feature intentionally omitted.

## Visual review

Screen, stand, status ring and check retained. Ring-to-screen and ring-to-check gaps fail; not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [screen]: screen and status-ring are 6 apart on centerlines nearest (24, 6)<->(24, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [status-ring]: status-ring and check are 2.99952 apart on centerlines nearest (30.3871, 15.1838)<->(28, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
