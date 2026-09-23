# ui webpage skull

Browser page containing an open-jawed skull with eye dots and a middle tooth stroke.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg`.

panels-top-left and skull: circular cranium with narrowed jaw; human_ref/user.svg supplies circular head principle. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

- Two tiny chrome dashes omitted to give the skull room.

## Visual review

Circular cranium, eye dots and three jaw strokes retained. Eyes and jaw details crowd both the skull and the browser; not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [skull]: parallel straight edges jaw-right and middle-tooth are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [middle-tooth]: parallel straight edges middle-tooth and jaw-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [browser]: browser and skull are 5 apart on centerlines nearest (20, 42)<->(20, 37); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [browser]: browser and middle-tooth are 5 apart on centerlines nearest (24, 42)<->(24, 37); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-21 are 4.99939 apart on centerlines nearest (16.0012, 28.0782)<->(21, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and eye-27 are 4.99939 apart on centerlines nearest (31.9988, 28.0782)<->(27, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [skull]: skull and middle-tooth are 4 apart on centerlines nearest (20, 35)<->(24, 35); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-21]: eye-21 and eye-27 are 6 apart on centerlines nearest (21, 28)<->(27, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-21]: eye-21 and middle-tooth are 6.7082 apart on centerlines nearest (21, 28)<->(24, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [eye-27]: eye-27 and middle-tooth are 6.7082 apart on centerlines nearest (27, 28)<->(24, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

Circular head construction inspected. This subject is an isolated skull without a torso, so detached head/body spacing and stick-figure flags do not apply.
