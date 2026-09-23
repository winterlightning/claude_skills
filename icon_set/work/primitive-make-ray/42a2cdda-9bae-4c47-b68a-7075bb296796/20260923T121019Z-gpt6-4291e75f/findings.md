# keyboard button direction

Three keyboard direction keys arranged with up above left and right.

Keyshape: SQUARE — Square envelope around triangular key arrangement. Centerline extremes: [6, 6, 42, 42].

Construction: Repeated rounded keys share dimensions and arrow lengths; bottom arrows mirror.

Visual review: Reviewed in both themes at 48px and enlarged. Three keys and directions remain recognizable, but arrowheads and key walls merge. Required separation cannot fit this three-key composition at these dimensions. Not visually approved.

Omissions: None.

References:
- icon_set/work/todo-references/keyboard button direction_42a2cdda-9bae-4c47-b68a-7075bb296796.svg
- icon_set/references/lucide/original/keyboard.svg
- icon_set/references/lucide/atomic-debug/keyboard.svg

```text
status: invalid
  ERROR  mic [key-1]: parallel straight edges key-1-6 and key--1-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [up-key]: up-key and key--1 are 4 apart on centerlines nearest (19, 22)<->(19, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [up-key]: up-key and key-1 are 4 apart on centerlines nearest (29, 22)<->(29, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [up-key]: up-key and up-shaft are 4 apart on centerlines nearest (24, 6)<->(24, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [key--1]: key--1 and shaft--1 are 4 apart on centerlines nearest (6, 34)<->(10, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [key--1]: key--1 and key-1 are 4 apart on centerlines nearest (22, 29)<->(26, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [key-1]: key-1 and shaft-1 are 4 apart on centerlines nearest (42, 34)<->(38, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
