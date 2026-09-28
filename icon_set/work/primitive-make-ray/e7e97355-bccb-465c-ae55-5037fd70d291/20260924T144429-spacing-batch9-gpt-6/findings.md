# heart user

Status: **blocked**. Keyshape: `VRECT_L`. 32 by 40 centerline envelope supports upright page, heart or phone.

Smooth mirrored heart lobes and person retained; head and shoulders still crowd enclosure.

Omissions/reductions: None in final candidate.

Inspected construction references:

- icon_set/references/lucide/original/heart.svg
- icon_set/references/lucide/atomic-debug/heart.svg
- icon_set/skills/icon-design/human-reference.md
- icon_set/references/human_ref/user.svg

Lucide construction principles: coherent outlines, paired curves and real shared attachment nodes, re-authored on SOLO48. Directional Bluetooth/play marks, page corner, capsule handle and mail flap preserve intentional asymmetry; other pairs share axes and dimensions.

Native 48px and enlarged light/dark previews visually inspected. Not approved: retain identifiable composition and record the unresolved gate.

Saved candidates: 7. Earlier candidates and logs remain in this run folder.

```text
status: invalid
  ERROR  mic [heart]: heart and head are 7 apart on centerlines nearest (24, 8)<->(24, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [heart]: heart and shoulders are 6.9175 apart on centerlines nearest (17.2075, 41.3288)<->(20, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
BUILD GATE FAIL (fail, 2 errors, 0 warnings)
  error: mic [heart]: heart and head are 7 apart on centerlines nearest (24, 8)<->(24, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [heart]: heart and shoulders are 6.9175 apart on centerlines nearest (17.2075, 41.3288)<->(20, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Human geometry: head center (24,19), radius 4; bottom y23. Shoulder apex y31. Centerline gap 8, ink gap 4; enclosure clearance remains blocked.
