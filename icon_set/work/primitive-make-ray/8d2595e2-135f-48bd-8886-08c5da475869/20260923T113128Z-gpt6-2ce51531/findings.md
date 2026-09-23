# earthquake hiding proof table

A crouching person shelters beneath a table with earthquake marks above.

SQUARE: The broad composition needs equal overall width and height; visible extrema (4,4)-(44,44).

Construction: human_ref/full_body_ref.png: crouching pose and coherent limbs. No useful exact Lucide scene match.

Reduction: The original continuous head-and-back silhouette is retained; no detached head is introduced. Small folds reduced.

Both themes inspected at 48 and 192 px. Table, tremors and crouched continuous body remain recognizable, but the figure merges with the tabletop and has pinched limbs. Not visually approved. Shared human crouching reference inspected; source has continuous head/back, so no detached-head gap applies.

```text
status: invalid
  ERROR  mic [tabletop]: parallel straight edges tabletop-5 and crouched-body-4 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [crouched-body]: parallel straight edges crouched-body-4 and crouched-body-12 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [crouched-body]: parallel straight edges crouched-body-7 and crouched-body-9 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [tremor--1]: parallel straight edges tremor--1-1 and tremor--1-3 are 5.6 apart on centerlines (ink gap 1.6); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [tremor-1]: parallel straight edges tremor-1-1 and tremor-1-3 are 5.6 apart on centerlines (ink gap 1.6); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [tabletop]: tabletop and tremor--1 are 6 apart on centerlines nearest (13, 16)<->(13, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [tabletop]: tabletop and tremor-1 are 6 apart on centerlines nearest (35, 16)<->(35, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [tabletop]: tabletop and crouched-body are 3 apart on centerlines nearest (27, 24)<->(27, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [table-leg-8]: table-leg-8 and crouched-body are 4 apart on centerlines nearest (8, 40)<->(12, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [table-leg-40]: table-leg-40 and crouched-body are 6 apart on centerlines nearest (40, 39)<->(34, 39); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
