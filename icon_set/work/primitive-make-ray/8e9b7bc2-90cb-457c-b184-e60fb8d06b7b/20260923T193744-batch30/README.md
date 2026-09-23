# noise pollution traffic

Two cars below lightning and noise zigzags.

Keyshape: HRECT_L. Horizontal room for the paired cars and noise marks.

Two repeated car silhouettes; central lightning and mirrored side noise marks. HRECT_L ink extremes (2,6)-(46,42).

Construction references: car-front: coherent rounded body and paired wheel placement.

Omissions/reductions: No defining component omitted; wheel and noise detail retained.

Visual review: Two cars and three noise motifs remain recognizable, but the lightning interior and wheel lobes are visually tight at 48px. Not visually approved; MIC blocks the adjacent marks and cars.

Human construction: Not applicable.

Validation: **invalid**

```text
status: invalid
  ERROR  mic [noise-left]: parallel straight edges noise-left-3 and noise-left-1 are 4.94975 apart on centerlines (ink gap 0.949747); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [car-0-outline]: car-0-outline and lightning are 6.84198 apart on centerlines nearest (16.0745, 27.4207)<->(22, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [car-0-outline]: car-0-outline and noise-left are 6.64225 apart on centerlines nearest (9.28069, 26.2384)<->(7, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [car-1-outline]: car-1-outline and noise-right are 4.0528 apart on centerlines nearest (37.7026, 26.0419)<->(38, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [lightning]: lightning and noise-left are 5.09902 apart on centerlines nearest (18, 18)<->(13, 19); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [lightning]: lightning and noise-right are 7.28011 apart on centerlines nearest (31, 14)<->(38, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `8e9b7bc2-90cb-457c-b184-e60fb8d06b7b`.
