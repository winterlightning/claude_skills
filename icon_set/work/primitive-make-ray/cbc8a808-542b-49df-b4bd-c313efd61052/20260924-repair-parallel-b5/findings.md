# valve logo — blocked

Source: `pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg`

Keyshape: HRECT_M. BLOCKED after six rounds: two-row candidate passes geometry but changes defining single-line logo. Retain single-line VALVE; letter-to-letter MIC and A counter remain blockers.

No letters omitted. A two-row candidate passed geometry but was rejected because it changed the single-line logo.

Blocked: single-line letters crowd each other; A counter undersized. Round6 reflow is not a faithful wordmark.

References: supplied SVG rendered as reference.png; Lucide original/trash-2.svg and atomic-debug/trash-2.svg: shared handle nodes and coherent rounded contours; Lucide original/tv.svg and atomic-debug/tv.svg: consistent rounded enclosure construction

```text
BUILD GATE FAIL (fail, 6 errors, 0 warnings)
  error: mic [v-first]: parallel straight edges v-first-2 and a-sides-1 are 5.9397 apart on centerlines (ink gap 1.9397); requires at least 8 centerline / 4 ink (midpoint-normal)
  error: mic [v-first]: v-first and a-sides are 5.9397 apart on centerlines nearest (12, 10)<->(17.88, 10.84); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [a-sides]: a-sides and l are 2 apart on centerlines nearest (22, 38)<->(24, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [l]: l and v-second are 5.9397 apart on centerlines nearest (28, 38)<->(33.88, 37.16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [v-second]: v-second and e are 2 apart on centerlines nearest (38, 10)<->(40, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 1 undersized holes; 1 pinches
```
