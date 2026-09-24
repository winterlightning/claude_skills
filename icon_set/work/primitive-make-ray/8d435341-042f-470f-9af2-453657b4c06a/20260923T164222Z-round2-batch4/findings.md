# code build

A construction crane suspending a code window.

**HRECT_L**: The wide composition uses the 40 by32 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: construction: shared truss nodes; source supplies hanging window and three code strokes.

Reduction: Two truss bays reduced to one; code chevrons and slash retained.

Validation: **invalid**, 5 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Crane and hanging window are recognizable, but the code chevrons and slash fill the small window and lack clearance. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [window]: window and code-left are 4 apart on centerlines nearest (20, 32)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [window]: window and slash are 4 apart on centerlines nearest (30, 40)<->(30, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [window]: window and code-right are 3 apart on centerlines nearest (44, 32)<->(41, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [code-left]: code-left and slash are 3.16228 apart on centerlines nearest (27, 35)<->(30, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [slash]: slash and code-right are 4.12311 apart on centerlines nearest (34, 28)<->(38, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](code-build.svg) · [Python](code_build_8d435341_042f_470f_9af2_453657b4c06a.py) · [Light](light-240.png) · [Dark](dark-240.png)
