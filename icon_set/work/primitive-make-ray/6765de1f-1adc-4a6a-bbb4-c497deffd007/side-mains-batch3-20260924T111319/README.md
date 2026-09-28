# ui webpage social profile

Social profile webpage with header marks, portrait and text.

SQUARE: A square envelope provides room for the complete composition and its internal marks. Visible bounds: [4, 4, 44, 44].

Construction: Lucide id-card: portrait and text; human_ref/user.svg for head and shoulders.

Reductions: Header dashes reduced to dots; all three marks, portrait and both text lines retained.

Visual review: All page components retained, including three header marks, detached portrait and two text lines. Header and portrait crowd the enclosure; MIC failures remain. The detached head-to-shoulder gap is exactly 4 ink units.

```text
status: invalid
  ERROR  mic [page]: page and header-dot-0 are 5 apart on centerlines nearest (14, 6)<->(14, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [page]: page and header-dot-1 are 5 apart on centerlines nearest (22, 6)<->(22, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [page]: page and header-dot-2 are 5 apart on centerlines nearest (30, 6)<->(30, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [header]: header and head are 5 apart on centerlines nearest (18, 16)<->(18, 21); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [page]: page and shoulders are 3 apart on centerlines nearest (14, 42)<->(14, 39); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [page]: page and text-1 are 8 apart on centerlines nearest (31, 42)<->(31, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
