# pepper hot

A hot chili pepper beside a flame.

Keyshape: SQUARE. Balanced composition; target centerline box (6,6)-(42,42).

Plan: Asymmetric tapered pepper with a short stem; detached flame silhouette on the left.

Construction: No useful Lucide pepper match; smooth arc silhouette and asymmetry preserve the source.

Omissions: Small inner flame lick omitted to keep the flame open.

Visual review: Pepper and flame retain their side-by-side arrangement. Pepper rim overshoots the keyshape slightly and the flame is too close. Not approved.

```text
status: invalid
  ERROR  canvas/keyshape bounds: visible ink (4, 4, 44.2076, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.2076, 0.0], tolerance 0.0)
  ERROR  mic [flame]: parallel straight edges flame-2 and flame-4 are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [pepper]: pepper and flame are 5.89309 apart on centerlines nearest (22.0309, 40.2989)<->(18, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [pepper]: pepper and stem are 0 apart on centerlines nearest (31.9664, 13.6961)<->(31.9664, 13.6961); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
