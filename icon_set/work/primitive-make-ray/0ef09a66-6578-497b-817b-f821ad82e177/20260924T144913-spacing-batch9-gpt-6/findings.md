# mobile phone fingerprint

Status: **blocked**. Keyshape: `SQUARE`. 36 by 36 centerline envelope provides width for nested composition.

Single-arch reduction rejected as doorbell-like; restored ridges still violate spacing.

Omissions/reductions: Extra fingerprint branch strokes omitted; multiple identifying ridges retained.

Inspected construction references:

- icon_set/references/lucide/original/smartphone.svg
- icon_set/references/lucide/atomic-debug/smartphone.svg
- icon_set/references/lucide/original/fingerprint-pattern.svg
- icon_set/references/lucide/atomic-debug/fingerprint-pattern.svg

Lucide construction principles: coherent outlines, paired curves and real shared attachment nodes, re-authored on SOLO48. Directional Bluetooth/play marks, page corner, capsule handle and mail flap preserve intentional asymmetry; other pairs share axes and dimensions.

Native 48px and enlarged light/dark previews visually inspected. Not approved: retain identifiable composition and record the unresolved gate.

Saved candidates: 6. Earlier candidates and logs remain in this run folder.

```text
status: invalid
  ERROR  mic [separator]: separator and inner-left are 6 apart on centerlines nearest (18, 34)<->(18, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [separator]: separator and center-ridge are 5 apart on centerlines nearest (24, 34)<->(24, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [outer-ridge]: outer-ridge and inner-arch are 5.48686 apart on centerlines nearest (33, 23)<->(27.7981, 24.7453); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [inner-left]: inner-left and center-ridge are 4.37152 apart on centerlines nearest (19.9306, 26.4031)<->(24, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [phone]: phone and outer-ridge are 8 apart on centerlines nearest (24, 6)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
BUILD GATE FAIL (fail, 4 errors, 1 warnings)
  error: mic [separator]: separator and inner-left are 6 apart on centerlines nearest (18, 34)<->(18, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [separator]: separator and center-ridge are 5 apart on centerlines nearest (24, 34)<->(24, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [outer-ridge]: outer-ridge and inner-arch are 5.48686 apart on centerlines nearest (33, 23)<->(27.7981, 24.7453); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [inner-left]: inner-left and center-ridge are 4.37152 apart on centerlines nearest (19.9306, 26.4031)<->(24, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  warning: mic [phone]: phone and outer-ridge are 8 apart on centerlines nearest (24, 6)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
