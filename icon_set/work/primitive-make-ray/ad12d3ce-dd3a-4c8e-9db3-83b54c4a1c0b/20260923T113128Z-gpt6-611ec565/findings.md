# east

A circular compass with a northeast needle and the letter E underneath.

VRECT_M: The slim upright composition uses visible extrema (8,2)-(40,46).

Construction: compass: circular housing and angular directional needle.

Reduction: Retained four compass ticks and E. Deliberate northeast orientation follows the source.

Both themes inspected at 48 and 192 px. Compass and directional needle remain identifiable; the E becomes clogged and nearly touches the rim. Not visually approved: MIC failures retained.

```text
status: invalid
  ERROR  mic [letter-e]: parallel straight edges letter-e-1 and e-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [e-middle]: parallel straight edges e-middle and letter-e-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [rim]: rim and needle are 5.51461 apart on centerlines nearest (33.9233, 8.12458)<->(30, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [rim]: rim and letter-e are 4 apart on centerlines nearest (24, 32)<->(24, 36); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
