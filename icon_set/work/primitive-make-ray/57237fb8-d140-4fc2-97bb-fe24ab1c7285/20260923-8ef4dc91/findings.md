# office desk 1

Office workstation: monitor left, clock right, desk across bottom and two legs.

Keyshape: SQUARE, Balanced near-square composition; visible bounds (4, 4, 44, 44).

Omissions: Monitor bezel and cup width reduced to simple strokes.

Visual review: Monitor, clock and desk are recognizable, but the desk thickness collapses and the clock crowds the monitor and hands; requires revision.

```text
status: invalid
  ERROR  mic [desk]: parallel straight edges desk-1 and desk-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [monitor]: monitor and clock are 4 apart on centerlines nearest (26, 12)<->(30, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [clock]: clock and hands are 1.99985 apart on centerlines nearest (35.9755, 6.0003)<->(36, 8); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
