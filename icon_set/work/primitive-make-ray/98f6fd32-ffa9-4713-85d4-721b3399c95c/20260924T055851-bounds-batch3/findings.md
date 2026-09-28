# sign language thank you

Status: blocked.

Keyshape: SQUARE. Full hand and downward motion use the square field.

Reduction: Minor palm crease omitted.

Construction references: Lucide hand original and atomic-debug: rounded fingertips and coherent palm. Shared human references inspected; no detached head.

Visual review: Four fingers, thumb and downward arrow retained; unresolved crowding where arrow begins next to palm.

Blocker: MIC: hand and motion at (26,30) and approximately (26.0491,26.0006) are 3.9997 centerline units apart; requires 8.

Final validation:

```text
status: invalid
  ERROR  mic [hand]: hand and motion are 3.9997 apart on centerlines nearest (26, 30)<->(26.0491, 26.0006); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Final build gate:

```text
BUILD GATE FAIL (fail, 1 errors, 0 warnings)
  error: mic [hand]: hand and motion are 3.9997 apart on centerlines nearest (26, 30)<->(26.0491, 26.0006); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

```
