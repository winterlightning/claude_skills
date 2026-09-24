# christmas postcard 2

A Christmas postcard with a snowflake, divider, stamp and address rules.

**HRECT_L**: The wide composition uses the 40 by32 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: snowflake: branched axial strokes; source postcard layout.

Reduction: Two address rules reduced to one; all four snowflake branches retained.

Validation: **invalid**, 6 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Postcard layout remains identifiable, but snowflake branches merge at native size and crowd the divider. Stamp and address rule also crowd the outer frame. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [card]: card and flake-h are 5 apart on centerlines nearest (4, 24)<->(9, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [card]: card and stamp are 5 apart on centerlines nearest (44, 20)<->(39, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [card]: card and address are 6 apart on centerlines nearest (44, 32)<->(38, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [divider]: divider and flake-h are 4 apart on centerlines nearest (27, 24)<->(23, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [divider]: divider and stamp are 6 apart on centerlines nearest (27, 20)<->(33, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [divider]: divider and address are 6.08276 apart on centerlines nearest (27, 31)<->(33, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](christmas-postcard-2.svg) · [Python](christmas_postcard_2_6341f7cd_9be8_48da_9d1f_bb8141ad4804.py) · [Light](light-240.png) · [Dark](dark-240.png)
