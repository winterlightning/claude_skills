# rectangle like text

All four LIKE letters and the rectangular border retained. Enlarged E spacing, redistributed glyphs and compared three keyshapes. Blocked: frame/letter and letter/letter clearances remain six units; I/K parallel stems are also six units apart.

Construction: local Lucide `rectangle-ellipsis` original and atomic-debug. Used its silhouette and attachment principles, re-authored at SOLO48.

Reviewed the reference and emitted light/dark previews at 48 and 240 pixels. Detailed failures, when present, are in build-gate.txt and the gate overlays.

Keyshape: HRECT_L; visible ink bounds (2,6)-(46,42). Chosen for the overall upright, square or horizontal composition.

Final status: blocked.
error: mic [k-stem]: parallel straight edges k-stem-1, k-stem-2 and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
error: mic [l]: parallel straight edges l-1 and frame-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
error: mic [frame]: frame and l are 6 apart on centerlines nearest (4, 16)<->(10, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
error: mic [frame]: frame and e are 6 apart on centerlines nearest (44, 16)<->(38, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
error: mic [l]: l and i are 6 apart on centerlines nearest (13, 32)<->(19, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
error: mic [i]: i and k-stem are 6 apart on centerlines nearest (19, 16)<->(25, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
error: mic [k-arms]: k-arms and e are 6 apart on centerlines nearest (29, 16)<->(35, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
warning: mic [frame]: frame and i are 8 apart on centerlines nearest (19, 8)<->(19, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
warning: mic [frame]: frame and k-stem are 8 apart on centerlines nearest (25, 8)<->(25, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
