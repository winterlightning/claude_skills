# nun

A nun wearing a veil and a cross.

Keyshape: SQUARE. Balanced or approximately square subject; target centerline extremes (6,6)-(42,42).

Plan: Circular face, symmetric arched veil, detached shoulders and cross; shared human-reference vocabulary.

References: No useful Lucide match; shared human_ref/user.svg supplies circular head and broad shoulders.

Omissions: Facial band and neck seams omitted; veil and cross retained.

Visual review: Face and veil remain visible, but cross merges into the lower shoulder/baseline area. Native-size silhouette is too generic. Not visually approved.

Human construction: human_ref/user.svg inspected. Face bottom centerline y=28, shoulder top y=36: centerline gap 8, ink gap 4. Face radius 7; symmetrical shoulders.

```text
status: invalid
  ERROR  canvas/keyshape bounds: visible ink (4, 4, 44, 45) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 1.0], tolerance 0.0)
  ERROR  mic [shoulders]: parallel straight edges shoulder-top and cross-l are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [shoulders]: parallel straight edges shoulder-top and cross-r are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [shoulders]: parallel straight edges shoulder-top and veil-sides-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [cross-l]: parallel straight edges cross-l and veil-sides-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cross-r]: parallel straight edges cross-r and veil-sides-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  WARN   mic [veil]: veil and face are 7.99985 apart on centerlines nearest (24.0491, 6.0003)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
