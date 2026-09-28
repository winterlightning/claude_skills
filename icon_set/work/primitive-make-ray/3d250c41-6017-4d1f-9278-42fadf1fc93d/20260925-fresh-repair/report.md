# social-media-like-button

All four LIKE letters remain in source order inside a rounded horizontal button; taller E strokes cure the old row spacing.

- Source UUID: `3d250c41-6017-4d1f-9278-42fadf1fc93d`
- Reference: `pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg`
- Author: `gpt-6`
- Keyshape: `HRECT_L`; visible ink bounds `[2, 6, 46, 42]`. Wide envelope preserves horizontal text and its enclosure.
- Full QA: **fail**.

## Construction and omissions

Lucide rectangle-ellipsis original and atomic-debug: rounded horizontal enclosure; supplied reference governs LIKE.

I serifs omitted.

## Visual review

Both themes/native48: full LIKE text is readable but crowded; E horizontal levels are now 8 centerline units apart. Other letter and wall gaps still fail. No visual approval for release.

## Validation

- mic [k-stem]: parallel straight edges k-stem-1, k-stem-2 and i are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [l]: parallel straight edges l-1 and frame-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [frame]: frame and l are 6 apart on centerlines nearest (4, 16)<->(10, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [frame]: frame and e are 6 apart on centerlines nearest (44, 16)<->(38, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [l]: l and i are 5 apart on centerlines nearest (14, 32)<->(19, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [i]: i and k-stem are 5 apart on centerlines nearest (19, 16)<->(24, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [k-arms]: k-arms and e are 5 apart on centerlines nearest (28, 16)<->(33, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [frame]: frame and i are 8 apart on centerlines nearest (19, 8)<->(19, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [frame]: frame and k-stem are 8 apart on centerlines nearest (24, 8)<->(24, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
