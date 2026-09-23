# performance increase mail

An envelope holding an increasing chart.

Keyshape: SQUARE. Balanced composition; target centerline box (6,6)-(42,42).

Plan: Envelope boundary, three chart bars, and a rising trend arrow above.

Construction: trending-down: continuous trend stroke, reversed for increase; source owns envelope/chart layout.

Omissions: Three outlined bars reduced to vertical strokes.

Visual review: Envelope, three rising bars and trend arrow survive, but bars and arrow are too close. Small overlaps at envelope attachments remain unresolved. Not approved.

```text
status: invalid
  ERROR  mic [envelope]: parallel straight edges envelope-3 and bar-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [bar-0]: parallel straight edges bar-0 and envelope-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [envelope]: envelope and bar-0 are 0.291386 apart on centerlines nearest (11.8585, 29.2547)<->(12, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [envelope]: envelope and bar-2 are 0.291386 apart on centerlines nearest (36.1415, 29.2547)<->(36, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [bar-1]: bar-1 and trend are 4.12311 apart on centerlines nearest (24, 18)<->(23, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [bar-0]: bar-0 and trend are 5.65685 apart on centerlines nearest (12, 22)<->(8, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [bar-2]: bar-2 and arrow are 6 apart on centerlines nearest (36, 14)<->(42, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
