# arduino plus minus

Status: **blocked**. Keyshape: `HRECT_M`.

Blocked: full plus mark remains readable in both themes, but the gate cannot certify the exact 8-unit right-wall gap. Earlier numeric-pass candidates reduced plus to a stub and were rejected visually. Exact HRECT_M ink bounds retained.

Omissions: Lobes rebalanced; minus shortened.

Construction references: lucide/infinity original and atomic-debug: coherent lobe flow.

Final gate:

```text
BUILD GATE FAIL (review, 0 errors, 1 warnings)
  warning: mic [infinity]: infinity and plus-h are 8 apart on centerlines nearest (44, 24)<->(36, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Attempts are preserved in `attempts/`; 8 revisions after initial authoring.
