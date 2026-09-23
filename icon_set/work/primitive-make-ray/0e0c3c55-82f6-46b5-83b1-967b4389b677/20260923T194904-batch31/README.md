# parkig aid system

A parking P with sensor waves facing a triangular obstacle.

Keyshape: SQUARE. Equal width and height fit the complete scene or enclosing frame.

P sits upper-left, two expanding wave curves occupy the middle, and an obstacle sits lower-right. Ink extremes (4,4)-(44,44).

Construction references: square-parking: P construction; radio-tower: expanding signal arcs, adapted to the supplied right-facing arrangement.

Omissions/reductions: None.

Visual review: P, two sensor waves and triangular obstacle remain visible, but the outer wave merges toward the triangle. Not visually approved; both the blocking error and the remaining warning are recorded.

Human construction: Not applicable.

Validation: **invalid**

```text
status: invalid
  ERROR  mic [wave-outer]: wave-outer and obstacle are 2.49388 apart on centerlines nearest (31.3853, 25.6528)<->(33.6159, 26.7681); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [p-loop]: p-loop and wave-inner are 7.99989 apart on centerlines nearest (18, 12)<->(25.9998, 12.0418); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `0e0c3c55-82f6-46b5-83b1-967b4389b677`.
