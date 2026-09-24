# circle skull xmark

Status: **blocked**. Keyshape: `CIRCLE`. Circular badge requires radial envelope of radius 22 visible ink.

Simplified candidate lost crossbone silhouette; complete four-ray skull retained with spacing blockers.

Omissions/reductions: Microscopic tooth detail simplified to central stroke.

Inspected construction references:

- icon_set/references/lucide/original/skull.svg
- icon_set/references/lucide/atomic-debug/skull.svg

Lucide construction principles: coherent outlines, paired curves and real shared attachment nodes, re-authored on SOLO48. Directional Bluetooth/play marks, page corner, capsule handle and mail flap preserve intentional asymmetry; other pairs share axes and dimensions.

Native 48px and enlarged light/dark previews visually inspected. Not approved: retain identifiable composition and record the unresolved gate.

Saved candidates: 7. Earlier candidates and logs remain in this run folder.

```text
status: invalid
  ERROR  mic [ring]: ring and bone-tr are 2.97033 apart on centerlines nearest (36.9263, 8.73897)<->(35, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-left are 5.8767 apart on centerlines nearest (14.2904, 21.6084)<->(20, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-right are 5.8767 apart on centerlines nearest (33.7096, 21.6084)<->(28, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [skull]: skull and tooth are 8 apart on centerlines nearest (16, 32)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
BUILD GATE FAIL (fail, 3 errors, 1 warnings)
  error: mic [ring]: ring and bone-tr are 2.97033 apart on centerlines nearest (36.9263, 8.73897)<->(35, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [skull]: skull and eye-left are 5.8767 apart on centerlines nearest (14.2904, 21.6084)<->(20, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [skull]: skull and eye-right are 5.8767 apart on centerlines nearest (33.7096, 21.6084)<->(28, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  warning: mic [skull]: skull and tooth are 8 apart on centerlines nearest (16, 32)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
