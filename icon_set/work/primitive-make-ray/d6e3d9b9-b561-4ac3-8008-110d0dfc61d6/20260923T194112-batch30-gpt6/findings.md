# note dollar sign

A clipboard displaying a dollar sign.

Keyshape: VRECT_L. Upright page or profile; target centerline extremes (8,4)-(40,44).

Plan: U-shaped board with a centered capsule clip; dollar construction belongs to the board interior.

References: notebook: coherent rounded enclosure; clip is reconstructed from the input.

Omissions: Small currency terminals simplified.

Visual review: Dollar S is now coherent and legible, but its terminals are too close to the clip and board bottom. Not approved under clearance rules.

```text
status: invalid
  ERROR  mic [dollar-s]: parallel straight edges s-bottom and board-3 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [board]: board and dollar-bottom are 4 apart on centerlines nearest (24, 44)<->(24, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [clip]: clip and dollar-top are 5 apart on centerlines nearest (24, 12)<->(24, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
