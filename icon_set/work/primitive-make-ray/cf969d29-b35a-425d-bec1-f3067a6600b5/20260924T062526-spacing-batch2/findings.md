# face spiral eyes

Status: blocked

Keyshape: CIRCLE; bounds_for(Profile.SOLO48) = (2, 2, 46, 46). Radial CIRCLE preserves round face.

Reduction: Retained both fully wound spiral eyes and neutral mouth in selected blocked candidate.

Construction references: Human references inspected; no useful exact local Lucide match for spiral faces.

Visual review at 48px and enlarged in both themes: Neutral mouth and spiral concept retained; inner windings merge at native size and remain blocked.

Final validation:

```text
status: invalid
  ERROR  mic [head]: head and spiral-0 are 4.96731 apart on centerlines nearest (6.31966, 14.6517)<->(10.7147, 16.9663); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head]: head and spiral-1 are 4.96731 apart on centerlines nearest (41.6803, 14.6517)<->(37.2853, 16.9663); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [spiral-0]: spiral-0 and spiral-1 are 4 apart on centerlines nearest (22, 20)<->(26, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Final build gate:

```text
BUILD GATE FAIL (fail, 4 errors, 2 warnings)
  error: mic [head]: head and spiral-0 are 4.96731 apart on centerlines nearest (6.31966, 14.6517)<->(10.7147, 16.9663); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [head]: head and spiral-1 are 4.96731 apart on centerlines nearest (41.6803, 14.6517)<->(37.2853, 16.9663); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [spiral-0]: spiral-0 and spiral-1 are 4 apart on centerlines nearest (22, 20)<->(26, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 2 undersized holes; 0 pinches
  warning: internal-spacing [spiral-0]: spiral-0 and spiral-0 have -1.0942 units of ink clearance over 17.2043 units; requires 4; review required
  warning: internal-spacing [spiral-1]: spiral-1 and spiral-1 have -1.0942 units of ink clearance over 17.2043 units; requires 4; review required

```
