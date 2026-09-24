# Heart-shaped smiling face with heart eyes.

Status: **blocked**. Model: invalid. Build gate: fail.

HRECT_L gives the paired heart eyes the broadest available heart envelope.

Heart holes are open, but eyes, outer heart and smile remain too close; not visually approved.

Omissions: Smile simplified to one arc; both heart eyes retained.

References: Original reference supplies shared mirrored heart lobes; no useful exact Lucide match used.

## Build gate

```text
BUILD GATE FAIL (fail, 6 errors, 0 warnings)
  error: mic [heart]: heart and eye-0 are 5.51754 apart on centerlines nearest (8.41456, 28.5361)<->(12.6294, 24.9755); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [heart]: heart and eye-1 are 5.51754 apart on centerlines nearest (39.5854, 28.5361)<->(35.3706, 24.9755); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [heart]: heart and smile are 6.02577 apart on centerlines nearest (18.8513, 37.1377)<->(22, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-0]: eye-0 and eye-1 are 4.45303 apart on centerlines nearest (21.7735, 19.3492)<->(26.2265, 19.3492); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-0]: eye-0 and smile are 6.84369 apart on centerlines nearest (17.5221, 26.8246)<->(22, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-1]: eye-1 and smile are 6.84369 apart on centerlines nearest (30.4779, 26.8246)<->(26, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

```
