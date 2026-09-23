# square sliders

Rounded square with three horizontal sliders and staggered circular knobs.

SQUARE preserves the square enclosure and composition; visible extremes (4,4)-(44,44), centerline extremes (6,6)-(42,42).

sliders-horizontal: shared track lengths, repeated knobs and staggered settings.

No parts omitted.

Three slider tracks and staggered knobs retained. Adjacent rows crowd the circular knobs; not approved.

```text
status: invalid
  ERROR  mic [knob-0]: knob-0 and left-1 are 6 apart on centerlines nearest (21, 18)<->(21, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [knob-1]: knob-1 and right-2 are 6 apart on centerlines nearest (27, 26)<->(27, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and knob-0 are 8 apart on centerlines nearest (21, 6)<->(21, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [frame]: frame and knob-2 are 8 apart on centerlines nearest (20, 42)<->(20, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
