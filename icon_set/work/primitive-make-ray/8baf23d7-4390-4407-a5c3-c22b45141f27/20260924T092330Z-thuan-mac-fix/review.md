# pencil-marking-ballot

Feedback: Bad stroke drawn.

Cannot-fix: MIC between marked-box and cross-a is 4 centerline units; 8 is required. Two equal boxes containing a visible crossed mark need more than the 40-unit vertical budget once the inter-box gap is included. Shrinking the cross loses the mark; changing equal choices or removing a choice changes the reference.

Reviewed reference, rejected drawing and fresh export at native48 and enlarged384 in both light and dark. Not visually approved; see blocking findings and retained attempts.

Keyshape: VRECT_L; fits the subject arrangement and bounds (6, 2, 42, 46).

Construction references: Lucide square-pen: outlined ballot choices and pencil. Equal boxes preserve the source hierarchy; cross is essential and must remain readable.

Validation:

```text
status: invalid
  ERROR  mic [marked-box]: marked-box and cross-a are 4 apart on centerlines nearest (12, 28)<->(12, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
