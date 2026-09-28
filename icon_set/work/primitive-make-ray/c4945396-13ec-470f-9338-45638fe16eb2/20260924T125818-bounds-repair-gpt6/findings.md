# amazon web service elemental medialive

Status: **blocked**. Keyshape: `VRECT_L`.

Blocked after five repair rounds. Exact VRECT_L bounds are met, but play triangle crowds top and right media nodes. Both themes show near-touching paint. No passing reconstruction found.

Omissions: Three peripheral scan marks removed to recover space.

Construction references: lucide/hexagon: repeated six-sided contours.

Final gate:

```text
BUILD GATE FAIL (fail, 4 errors, 0 warnings)
  error: mic [play]: parallel straight edges play-2 and right-6 are 4.02492 apart on centerlines (ink gap 0.0249224); requires at least 8 centerline / 4 ink (midpoint-normal)
  error: mic [top]: parallel straight edges top-4 and play-1 are 6.7082 apart on centerlines (ink gap 2.7082); requires at least 8 centerline / 4 ink (overlap-fallback)
  error: mic [top]: top and play are 6.7082 apart on centerlines nearest (24, 16)<->(21, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [play]: play and right are 4.02492 apart on centerlines nearest (32.2, 28.4)<->(34, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Attempts are preserved in `attempts/`; 5 revisions after initial authoring.
