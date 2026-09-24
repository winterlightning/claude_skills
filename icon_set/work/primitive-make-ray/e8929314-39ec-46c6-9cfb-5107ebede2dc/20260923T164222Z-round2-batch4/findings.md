# data lake code

Binary rows 10100 and 01100 above two water wave lines.

**SQUARE**: The overall composition uses the 36 by36 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: waves: repeated smooth lobes; source supplies literal binary strings.

Reduction: Wave count reduced from three to two lobes per row; all ten digits retained.

Validation: **invalid**, 22 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Both literal binary strings are retained. Enlarging zero counters makes them more legible than the initial solid-looking zeros, but adjacent digits and waves remain crowded. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [digit-1-2]: parallel straight edges digit-1-2 and digit-1-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [digit-0-0]: digit-0-0 and digit-0-1 are 4 apart on centerlines nearest (6, 10)<->(10, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-0]: digit-0-0 and digit-1-0 are 6.5268 apart on centerlines nearest (6, 14)<->(8.19986, 20.1449); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-1]: digit-0-1 and digit-0-2 are 4 apart on centerlines nearest (16, 10)<->(20, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-1]: digit-0-1 and digit-1-0 are 6.73202 apart on centerlines nearest (12.1999, 13.8551)<->(9.80014, 20.1449); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-1]: digit-0-1 and digit-1-1 are 6.5268 apart on centerlines nearest (13.8001, 13.8551)<->(16, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-2]: digit-0-2 and digit-0-3 are 4 apart on centerlines nearest (20, 10)<->(24, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-2]: digit-0-2 and digit-1-1 are 7.2111 apart on centerlines nearest (20, 14)<->(16, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-2]: digit-0-2 and digit-1-2 are 6 apart on centerlines nearest (20, 14)<->(20, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-3]: digit-0-3 and digit-0-4 are 4 apart on centerlines nearest (30, 10)<->(34, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-3]: digit-0-3 and digit-1-3 are 6 apart on centerlines nearest (27, 14)<->(27, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-0-4]: digit-0-4 and digit-1-4 are 6 apart on centerlines nearest (37, 14)<->(37, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-0]: digit-1-0 and digit-1-1 are 4 apart on centerlines nearest (12, 24)<->(16, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-0]: digit-1-0 and water-0 are 4.67789 apart on centerlines nearest (7.98933, 27.7662)<->(6, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-1]: digit-1-1 and digit-1-2 are 4 apart on centerlines nearest (16, 20)<->(20, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-1]: digit-1-1 and water-0 are 5.99674 apart on centerlines nearest (16, 28)<->(16.0364, 33.9966); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-2]: digit-1-2 and digit-1-3 are 4 apart on centerlines nearest (20, 24)<->(24, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-2]: digit-1-2 and water-0 are 5.43948 apart on centerlines nearest (20, 28)<->(22.0854, 33.0239); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-3]: digit-1-3 and digit-1-4 are 4 apart on centerlines nearest (30, 24)<->(34, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-3]: digit-1-3 and water-0 are 4.67789 apart on centerlines nearest (25.9893, 27.7662)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [digit-1-4]: digit-1-4 and water-0 are 5.64759 apart on centerlines nearest (37.8709, 27.8278)<->(39.963, 33.0736); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [water-0]: water-0 and water-1 are 7.20054 apart on centerlines nearest (8.39062, 33.2079)<->(6, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](data-lake-code.svg) · [Python](data_lake_code_e8929314_39ec_46c6_9cfb_5107ebede2dc.py) · [Light](light-240.png) · [Dark](dark-240.png)
