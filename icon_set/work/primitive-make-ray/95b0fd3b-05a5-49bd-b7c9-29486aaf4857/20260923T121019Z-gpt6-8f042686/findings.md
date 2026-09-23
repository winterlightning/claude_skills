# ipod play

An iPod player with play triangle, screen division, and circular control.

Keyshape: VRECT_L — Upright player enclosure. Centerline extremes: [8, 4, 40, 44].

Construction: Tangent rounded device body with independently authored play and control. 

Visual review: Reviewed in both themes at 48px and enlarged. Device, triangle and screen division read clearly; circular control is too close to the bottom and reads as a dot. Not approved under SOLO48 clearance.

Omissions: None.

References:
- icon_set/work/todo-references/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg
- icon_set/references/lucide/original/smartphone.svg
- icon_set/references/lucide/atomic-debug/smartphone.svg

```text
status: invalid
  ERROR  mic [screen-divider]: screen-divider and play are 5 apart on centerlines nearest (18, 32)<->(18, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [body]: body and control are 4 apart on centerlines nearest (24, 44)<->(24, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
