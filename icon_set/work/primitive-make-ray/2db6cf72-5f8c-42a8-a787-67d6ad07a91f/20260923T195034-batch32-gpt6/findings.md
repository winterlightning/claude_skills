# performance tablet increase

A hand holding a tablet displaying a rising chart.

Keyshape: SQUARE. Balanced composition; target centerline box (6,6)-(42,42).

Plan: Open tablet boundary accommodates the gripping thumb; separate trend and bars inside.

Construction: monitor: clean display perimeter; pencil: coherent diagonal stroke for trend.

Omissions: Tiny chart divisions omitted.

Visual review: Tablet, trend arrow and hand are present. Bars crowd the lower frame, and thumb crowds the right bar. Hand contour is angular. Not visually approved.

Human construction: Shared human_ref/user.svg reviewed; this is a hand and does not have a head/body gap.

```text
status: invalid
  ERROR  mic [thumb]: parallel straight edges thumb-2 and bar-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [tablet]: parallel straight edges tablet-3 and arrow-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [tablet]: tablet and trend are 6 apart on centerlines nearest (26, 6)<->(26, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [tablet]: tablet and bar-0 are 4 apart on centerlines nearest (14, 42)<->(14, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [tablet]: tablet and bar-1 are 4 apart on centerlines nearest (22, 42)<->(22, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
