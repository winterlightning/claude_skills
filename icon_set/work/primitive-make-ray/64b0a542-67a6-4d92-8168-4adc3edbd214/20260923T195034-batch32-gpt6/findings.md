# patentee

A patent certificate with a folded corner and ribbon seal.

Keyshape: VRECT_L. Upright subject; target centerline box (8,4)-(40,44).

Plan: Fold and page share corner nodes; circular seal interrupts the page lower boundary.

Construction: ticket: coherent document boundary; circular seal and ribbon from the source.

Omissions: Three writing rules reduced to one to reserve seal space.

Visual review: Certificate, folded corner and ribbon seal remain recognizable. Writing crowds the fold, and ribbon junctions do not meet certified attachment geometry. Not approved.

```text
status: invalid
  ERROR  mic [fold]: fold and writing are 5.09902 apart on centerlines nearest (30, 14)<->(25, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [seal]: seal and ribbon are 0.485281 apart on centerlines nearest (37.6569, 37.6569)<->(38, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
