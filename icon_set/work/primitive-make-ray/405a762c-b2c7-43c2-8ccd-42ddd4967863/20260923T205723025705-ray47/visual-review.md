# square person confined

Square enclosure containing a frontal person with a closed torso and two arm seams.

SQUARE preserves the square enclosure and composition; visible extremes (4,4)-(44,44), centerline extremes (6,6)-(42,42).

human_ref/user.svg and full_body_ref.png: circular head, broad smooth shoulders and exact detached gap.

No defining parts omitted.

Head, closed torso and arm seams retained. Own head-to-body gap is 28-(17+3)=8 centerline units / 4 ink units. Body is compressed and arm seams crowd sides; not approved.

```text
status: invalid
  ERROR  mic [body-base]: parallel straight edges body-base-3 and right-arm are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [left-arm]: parallel straight edges left-arm and body-base-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [body-base]: parallel straight edges body-base-2 and frame-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [frame]: frame and body-base are 7 apart on centerlines nearest (15, 42)<->(15, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and head are 8 apart on centerlines nearest (24, 6)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
