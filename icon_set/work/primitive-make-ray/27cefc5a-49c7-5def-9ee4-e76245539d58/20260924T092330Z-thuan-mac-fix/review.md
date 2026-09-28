# person-with-side-parted-hair-and-glasses

Feedback: Bad stroke drawn.

Cannot-fix: MIC hair/fringe is about4 centerline units, hair/lens6 and hair/shoulder4.81; 8 is required. A wider SQUARE attempt passed numeric checks but merged the fringe into the lens openings at 48px. Retained the failed meaning-preserving attempt; removing the long hair or glasses would lose defining features.

Reviewed reference, rejected drawing and fresh export at native48 and enlarged384 in both light and dark. Not visually approved; see blocking findings and retained attempts.

Keyshape: VRECT_L; fits the subject arrangement and bounds (6, 2, 42, 46).

Construction references: Human user.svg and Lucide glasses: circular jaw, touching shoulder ink, equal lenses and side-parted outer hair. Hair and eyewear retained; no detached human gap applies to connected portrait.

Validation:

```text
status: invalid
  ERROR  mic [hair]: hair and fringe are 3.99992 apart on centerlines nearest (8.00015, 19.9755)<->(12, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [hair]: hair and lens-17 are 6 apart on centerlines nearest (8, 22)<->(14, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [hair]: hair and shoulders are 4.80685 apart on centerlines nearest (8, 34)<->(11.0036, 37.7529); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [fringe]: fringe and lens-17 are 0 apart on centerlines nearest (14.8895, 19.8684)<->(14.8895, 19.8684); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
