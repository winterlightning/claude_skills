# office sign document

A document with a diagonal signing pen.

Keyshape: VRECT_L. Upright page or profile; target centerline extremes (8,4)-(40,44).

Plan: Open page outline around the diagonal pen; coherent pointed pen contour.

References: file-pen: diagonal writing tool with an open page boundary.

Omissions: Short baseline flourish omitted.

Visual review: Diagonal pen and open document read clearly, but the pen band and upper page edge are too close. Not approved under clearance rules.

```text
status: invalid
  ERROR  mic [pen]: parallel straight edges pen-3 and pen-band are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [page]: page and pen are 4.24264 apart on centerlines nearest (40, 12)<->(37, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
