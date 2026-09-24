# baggage weight

A suitcase below a floating weighing dial.

**VRECT_L**: Upright envelope supplies 40 centerline units of height for stacked or nested parts. Exact visible bounds are recorded by `ink_extremes` in the module.

Construction references: gauge: circular dial and diagonal needle; luggage: joined top handle.

Reduction: Both decorative suitcase stripes omitted to preserve the case opening.

Validation: **invalid**, 1 errors, 0 warnings.

Visual review: **needs review**, inspected at 48px and enlarged in light and dark. The separate dial, diagonal needle, handle and case are recognizable. The dial needle remains too close to the rim. The case is shallow after removing its stripes; not approved.

Validation findings:

```text
status: invalid
  ERROR  mic [dial]: dial and needle are 5.17118 apart on centerlines nearest (29.6114, 6.29882)<->(26, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](baggage-weight.svg) · [Python](baggage_weight_ee2a071e_6904_4d7d_a879_a7315aec3bd6.py) · [Light](light-240.png) · [Dark](dark-240.png)
