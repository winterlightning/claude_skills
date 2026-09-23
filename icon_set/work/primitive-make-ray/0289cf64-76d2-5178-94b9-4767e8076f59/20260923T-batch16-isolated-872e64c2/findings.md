# Framed female bust with a symmetrical hair silhouette and detached rules.

SQUARE: Balanced composition uses visible extremes (4,4)–(44,44).

Hair and head merge visually. Frame/head/hair MIC fails; detached head-to-shoulder centerline gap is 8, but other hair gaps fail. Not approved.

Omissions: Face and neck simplified to circular head; tiny hair interior lines omitted.

Inspected Lucide scan-face original and atomic-debug; used coherent contours and round joins.

```text
status: invalid
  ERROR  mic [frame]: frame and head are 6 apart on centerlines nearest (24, 14)<->(24, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [frame]: frame and hair are 3 apart on centerlines nearest (24, 14)<->(24, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head]: head and hair are 2.99987 apart on centerlines nearest (24, 20)<->(23.9717, 17.0003); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [hair]: hair and shoulders are 5 apart on centerlines nearest (15, 29)<->(15, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
