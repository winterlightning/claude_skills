# circle skull

A skull with dot eyes inside a circular badge.

**CIRCLE**: The reference is defined by a circular enclosure; centerline radius20 about (24,24). The module obtains its exact visible bounds from the profile.

Construction references: skull: domed head and narrowed open jaw; source dictates circular enclosure.

Reduction: None.

Validation: **invalid**, 2 errors, 2 warnings.

Visual review at48px and240px in light and dark: **not approved**. Skull and circular enclosure read clearly, but both dot eyes crowd the skull contour. Ring/skull and mouth/jaw clearances retain warnings. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [skull]: skull and eye--1 are 6.99947 apart on centerlines nearest (13.0011, 22.9141)<->(20, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-1 are 6.99947 apart on centerlines nearest (34.9989, 22.9141)<->(28, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [ring]: ring and skull are 7.99985 apart on centerlines nearest (23.9509, 4.0003)<->(24, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [skull]: skull and mouth are 8 apart on centerlines nearest (16, 32)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](circle-skull.svg) · [Python](circle_skull_52cd86bc_bba7_4a12_8eae_e78fbf4ca2ec.py) · [Light](light-240.png) · [Dark](dark-240.png)
