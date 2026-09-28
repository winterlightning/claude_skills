# face awesome

Status: blocked

Keyshape: CIRCLE; bounds_for(Profile.SOLO48) = (2, 2, 46, 46). Radial CIRCLE preserves round face.

Reduction: No defining star eye omitted. Final blocked candidate retains the smile.

Construction references: Lucide star original/atomic-debug: mirrored tips/valleys and common eye definition. Human facial vocabulary inspected.

Visual review at 48px and enlarged in both themes: Recognizable star-eyed expression; tiny star interiors and crowded gaps remain unacceptable.

Final validation:

```text
status: invalid
  ERROR  mic [head]: head and star-0 are 7.46969 apart on centerlines nearest (6.43405, 14.4385)<->(13, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head]: head and star-1 are 7.46969 apart on centerlines nearest (41.566, 14.4385)<->(35, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [star-0]: star-0 and star-1 are 6 apart on centerlines nearest (21, 18)<->(27, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [star-0]: star-0 and smile are 6 apart on centerlines nearest (20, 24)<->(20, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [star-1]: star-1 and smile are 6 apart on centerlines nearest (28, 24)<->(28, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Final build gate:

```text
BUILD GATE FAIL (fail, 6 errors, 0 warnings)
  error: mic [head]: head and star-0 are 7.46969 apart on centerlines nearest (6.43405, 14.4385)<->(13, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [head]: head and star-1 are 7.46969 apart on centerlines nearest (41.566, 14.4385)<->(35, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [star-0]: star-0 and star-1 are 6 apart on centerlines nearest (21, 18)<->(27, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [star-0]: star-0 and smile are 6 apart on centerlines nearest (20, 24)<->(20, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [star-1]: star-1 and smile are 6 apart on centerlines nearest (28, 24)<->(28, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 2 undersized holes; 0 pinches

```
