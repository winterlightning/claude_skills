# spellbook

Open spellbook with a star on its left page and a lower cover edge.

SQUARE: Square overall composition; target visible envelope (4,4)-(44,44).

book-open: mirrored page contours with a central gutter.

No defining parts omitted.

Open book and star retained; star crowds left page boundary, and upper curve misses exact keyshape. Not approved.

```text
status: invalid
  ERROR  canvas/keyshape bounds: visible ink (4, 4.5, 44, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.5, 0.0, 0.0], tolerance 0.0)
  ERROR  mic [outer]: outer and star are 2 apart on centerlines nearest (6, 22)<->(8, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
