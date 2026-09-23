# office desk 1

An office desk with a monitor, clock, and cup.

Keyshape: HRECT_L. Horizontal scene; target centerline extremes (4,8)-(44,40).

Plan: Desk spans the keyshape; monitor left and clock right deliberately balance different shapes.

References: laptop: simple screen enclosure and supporting base.

Omissions: Desk apron and monitor lower bezel omitted; cup and clock retained.

Visual review: Desk, monitor and clock remain recognizable; cup and clock hands are crowded. Not approved under clearance rules.

```text
status: invalid
  ERROR  mic [cup]: parallel straight edges cup-3 and cup-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cup]: parallel straight edges cup-2 and desk-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [monitor]: monitor and clock are 6 apart on centerlines nearest (26, 14)<->(32, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [clock]: clock and hands are 1.99985 apart on centerlines nearest (37.9755, 8.0003)<->(38, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
