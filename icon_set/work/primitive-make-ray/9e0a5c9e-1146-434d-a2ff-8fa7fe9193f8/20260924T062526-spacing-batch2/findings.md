# face smile hearts

Status: blocked

Keyshape: HRECT_L; bounds_for(Profile.SOLO48) = (2, 6, 46, 42). HRECT_L broadens the heart face while preserving mirrored lobes.

Reduction: Retained two heart eyes, heart outline and small smile in selected blocked candidate.

Construction references: Human references inspected; shared mirrored heart construction. No useful exact Lucide match.

Visual review at 48px and enlarged in both themes: Heart-eye interiors are open, but eyes and smile still crowd the enclosing heart.

Final validation:

```text
status: invalid
  ERROR  mic [heart]: heart and eye-0 are 5.35388 apart on centerlines nearest (6.73544, 26.2964)<->(11.217, 23.3673); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [heart]: heart and eye-1 are 5.35388 apart on centerlines nearest (41.2646, 26.2964)<->(36.783, 23.3673); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [heart]: heart and smile are 6.87481 apart on centerlines nearest (18.3145, 36.8034)<->(22, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-0]: eye-0 and eye-1 are 7.91253 apart on centerlines nearest (20.0437, 19.583)<->(27.9563, 19.583); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-0]: eye-0 and smile are 7.47997 apart on centerlines nearest (16.95, 25.4821)<->(22, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-1]: eye-1 and smile are 7.47997 apart on centerlines nearest (31.05, 25.4821)<->(26, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Final build gate:

```text
BUILD GATE FAIL (fail, 6 errors, 0 warnings)
  error: mic [heart]: heart and eye-0 are 5.35388 apart on centerlines nearest (6.73544, 26.2964)<->(11.217, 23.3673); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [heart]: heart and eye-1 are 5.35388 apart on centerlines nearest (41.2646, 26.2964)<->(36.783, 23.3673); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [heart]: heart and smile are 6.87481 apart on centerlines nearest (18.3145, 36.8034)<->(22, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-0]: eye-0 and eye-1 are 7.91253 apart on centerlines nearest (20.0437, 19.583)<->(27.9563, 19.583); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-0]: eye-0 and smile are 7.47997 apart on centerlines nearest (16.95, 25.4821)<->(22, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [eye-1]: eye-1 and smile are 7.47997 apart on centerlines nearest (31.05, 25.4821)<->(26, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

```
