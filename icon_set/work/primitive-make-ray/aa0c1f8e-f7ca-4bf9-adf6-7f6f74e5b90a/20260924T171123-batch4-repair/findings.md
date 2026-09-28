# Dizzy face with spiral eyes and an open mouth.

Status: **blocked**. Model: invalid. Build gate: fail.

CIRCLE retains the round face.

Eye turns, inter-eye gap and mouth crowding remain unresolved; not visually approved.

Omissions: Mouth simplified to a circular opening; defining spiral windings retained.

References: Original reference supplies mirrored windings; human facial vocabulary, no useful exact Lucide match used.

## Build gate

```text
BUILD GATE FAIL (fail, 6 errors, 2 warnings)
  error: mic [head]: head and spiral-0 are 3.58132 apart on centerlines nearest (7.55761, 12.6143)<->(10.4982, 14.6584); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [head]: head and spiral-1 are 3.58132 apart on centerlines nearest (40.4424, 12.6143)<->(37.5018, 14.6584); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [spiral-0]: spiral-0 and spiral-1 are 2 apart on centerlines nearest (23, 20)<->(25, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [spiral-0]: spiral-0 and mouth are 3.42808 apart on centerlines nearest (20.2675, 26.7676)<->(22.2414, 29.5703); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [spiral-1]: spiral-1 and mouth are 3.42808 apart on centerlines nearest (27.7325, 26.7676)<->(25.7586, 29.5703); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 1 undersized holes; 0 pinches
  warning: internal-spacing [spiral-0]: spiral-0 and spiral-0 have 0.0239 units of ink clearance over 22.2361 units; requires 4; review required
  warning: internal-spacing [spiral-1]: spiral-1 and spiral-1 have 0.0239 units of ink clearance over 22.2361 units; requires 4; review required

```
