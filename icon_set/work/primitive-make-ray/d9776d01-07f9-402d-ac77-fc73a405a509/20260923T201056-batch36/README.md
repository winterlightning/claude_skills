# rating booklet

A rating booklet with an outlined star and text lines.

Keyshape: VRECT_L. The tall envelope preserves the stacked head, page, or book arrangement.

Tall cover with a raised rear leaf contains a central star and two lower rules. Ink extremes (6,2)-(42,46).

Construction reference: star: five-point outline with purposeful corners; book: upright cover and offset leaf.

Omissions/reductions: None; star and both text rules retained.

Visual review: Booklet, raised rear leaf and star are identifiable, but lower text rules merge and crowd the cover bottom. Star-to-cover spacing is also insufficient. Not visually approved.

Human construction: Not applicable.

Validation: **invalid**; outcome: **failed-validation**

```text
status: invalid
  ERROR  mic [text-0]: parallel straight edges text-0 and text-1 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [text-0]: parallel straight edges text-0 and cover-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [text-1]: parallel straight edges text-1 and cover-4 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cover]: cover and rating-star are 6 apart on centerlines nearest (24, 12)<->(24, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [cover]: cover and text-0 are 6 apart on centerlines nearest (20, 44)<->(20, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [cover]: cover and text-1 are 3 apart on centerlines nearest (20, 44)<->(20, 41); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [rating-star]: rating-star and text-0 are 4.47214 apart on centerlines nearest (18, 34)<->(20, 38); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [rating-star]: rating-star and text-1 are 7.28011 apart on centerlines nearest (18, 34)<->(20, 41); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [text-0]: text-0 and text-1 are 3 apart on centerlines nearest (20, 38)<->(20, 41); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Author: `gpt-6`. Source UUID: `d9776d01-07f9-402d-ac77-fc73a405a509`.
