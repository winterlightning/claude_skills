# band saw

A band saw frame with a toothed wheel and base.

**SQUARE**: Balanced overall composition uses the 36 by 36 centerline envelope. Exact visible bounds are recorded by `ink_extremes` in the module.

Construction references: cog: repeated radial teeth and central hole; source determines the nested machine frame.

Reduction: Tooth count reduced to six broad teeth; ledge shortened where occluded by the wheel.

Validation: **invalid**, 3 errors, 0 warnings.

Visual review: **needs review**, inspected at 48px and enlarged in light and dark. Frame, base and toothed wheel remain present, but the wheel, hub and inner frame are visually congested. The failed parallel and hub clearances remain unresolved; not approved.

Validation findings:

```text
status: invalid
  ERROR  mic [inner]: parallel straight edges inner-1 and frame-left-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [inner]: parallel straight edges inner-2 and wheel-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [base]: base and hub are 2 apart on centerlines nearest (31, 34)<->(31, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](band-saw.svg) · [Python](band_saw_f8387852_af8b_4221_a8f7_998fc1b24294.py) · [Light](light-240.png) · [Dark](dark-240.png)
