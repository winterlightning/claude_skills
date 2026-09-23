# square this way up

Rounded square with two upward arrows above a shared horizontal baseline.

SQUARE preserves the square enclosure and composition; visible extremes (4,4)-(44,44), centerline extremes (6,6)-(42,42).

square-arrow-up: joined shaft/head; arrows share size and baseline.

No parts omitted.

Two upward arrows and baseline remain readable, but adjacent arrowheads and bottom border spacing fail MIC. Not approved.

```text
status: invalid
  ERROR  mic [baseline]: parallel straight edges baseline and frame-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [frame]: frame and baseline are 7 apart on centerlines nearest (15, 42)<->(15, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [left-head]: left-head and right-head are 4 apart on centerlines nearest (22, 20)<->(26, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and left-head are 8 apart on centerlines nearest (6, 20)<->(14, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and right-head are 8 apart on centerlines nearest (42, 20)<->(34, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
