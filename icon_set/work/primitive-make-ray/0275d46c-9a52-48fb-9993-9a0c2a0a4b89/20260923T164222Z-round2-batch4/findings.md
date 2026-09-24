# circle skull 1

A skull with slanted eyes inside a circular badge.

**CIRCLE**: The reference is defined by a circular enclosure; centerline radius20 about (24,24). The module obtains its exact visible bounds from the profile.

Construction references: skull: domed head and narrowed open jaw; source dictates circular enclosure.

Reduction: Slanted eye strokes shortened for clearance.

Validation: **invalid**, 2 errors, 2 warnings.

Visual review at48px and240px in light and dark: **not approved**. Circle, skull dome, slanted eyes and open jaw remain recognizable. Eyes are too close to the skull boundary; shortened eye strokes are weak at native size. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [skull]: skull and eye--1 are 5.99955 apart on centerlines nearest (13.0009, 22.9264)<->(19, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-1 are 5.99955 apart on centerlines nearest (34.9991, 22.9264)<->(29, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [ring]: ring and skull are 7.99985 apart on centerlines nearest (23.9509, 4.0003)<->(24, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [skull]: skull and mouth are 8 apart on centerlines nearest (16, 32)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](circle-skull-1.svg) · [Python](circle_skull_1_0275d46c_9a52_48fb_9993_9a0c2a0a4b89.py) · [Light](light-240.png) · [Dark](dark-240.png)
