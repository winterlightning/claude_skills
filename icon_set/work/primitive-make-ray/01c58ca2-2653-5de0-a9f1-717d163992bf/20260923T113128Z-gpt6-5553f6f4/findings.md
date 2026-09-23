# drone add

A front-view drone with two rotors, landing supports and a plus badge.

SQUARE: The broad composition needs equal overall width and height; visible extrema (4,4)-(44,44).

Construction: drone: shared symmetry and repeated components; front-view silhouette follows the supplied reference.

Reduction: Reduced the undulating fuselage to a smooth capsule; retained badge enclosure.

Both themes inspected at 48 and 192 px. Front drone and enclosed plus remain identifiable, but the badge is crowded. Not visually approved: MIC failures retained.

```text
status: invalid
  ERROR  mic [body]: parallel straight edges body-4 and badge-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [badge]: parallel straight edges badge-1 and plus-horizontal-1, plus-horizontal-2 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [plus-horizontal]: parallel straight edges plus-horizontal-1, plus-horizontal-2 and badge-5 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [badge]: badge and plus-vertical are 3 apart on centerlines nearest (24, 28)<->(24, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
