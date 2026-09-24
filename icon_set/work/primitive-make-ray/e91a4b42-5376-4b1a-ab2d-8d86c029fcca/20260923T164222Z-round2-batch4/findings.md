# compass east

A circular east compass badge followed by a right arrow.

**HRECT_M**: The horizontal badge/arrow composition uses the 40 by28 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: compass: circular badge; hand-authored E and concave directional arrow.

Reduction: None.

Validation: **invalid**, 1 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. E badge and east arrow remain identifiable. The E crowds its circular boundary and the arrow counter is narrow. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [badge]: badge and e are 4.05516 apart on centerlines nearest (11.2213, 12.3557)<->(13, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](compass-east.svg) · [Python](compass_east_e91a4b42_5376_4b1a_ab2d_8d86c029fcca.py) · [Light](light-240.png) · [Dark](dark-240.png)
