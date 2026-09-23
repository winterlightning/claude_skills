# square user

Rounded square with a circular user head and a smooth closed shoulder dome.

SQUARE preserves the square enclosure and composition; visible extremes (4,4)-(44,44), centerline extremes (6,6)-(42,42).

human_ref/user.svg and full_body_ref.png: circular head, symmetric shoulders and exact detached gap.

No parts omitted.

Circular head and shoulder dome retained, with exact 28-(17+3)=8 centerline / 4 ink head-body gap. Dome is compressed and border clearance remains uncertified; not approved as a complete pass.

```text
status: review
  WARN   mic [frame]: frame and head are 8 apart on centerlines nearest (24, 6)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and body are 8 apart on centerlines nearest (15, 42)<->(15, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
