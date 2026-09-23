# monitor small squares

A monitor showing two vertically stacked small squares.

Keyshape: SQUARE — Balanced square envelope around the complete composition. Exact centerline extremes are recorded in the Python module.

Construction: Shared monitor enclosure and one square definition repeated down the left screen area.

Visual review: Light/dark previews inspected at native and enlarged sizes. Both stacked outlined squares remain, but the lower square merges into the screen edge and the square openings are undersized. Not visually approved.

Omissions and reductions: None.

References:
- icon_set/work/todo-references/monitor small squares_1aef3c2a-6d0d-43a2-9616-698d70dc5298.svg
- icon_set/references/lucide/original/monitor.svg
- icon_set/references/lucide/atomic-debug/monitor.svg

```text
status: invalid
  ERROR  mic [screen]: parallel straight edges screen-0 and square-0-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [square-0]: parallel straight edges square-0-1 and square-0-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [square-0]: parallel straight edges square-0-3 and square-1-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [square-1]: parallel straight edges square-1-1 and square-1-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [square-1]: parallel straight edges square-1-3 and screen-5, screen-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [screen]: screen and square-0 are 7 apart on centerlines nearest (15, 6)<->(15, 13); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [screen]: screen and square-1 are 4 apart on centerlines nearest (23, 34)<->(23, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [square-0]: square-0 and square-1 are 5 apart on centerlines nearest (23, 19)<->(23, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
