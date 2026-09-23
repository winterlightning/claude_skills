# ui webpage ad text

Browser page showing the hand-authored letters A and D.

## Keyshape

SQUARE: Full composition uses centerline extremes (6,6)–(42,42), visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg`.

panels-top-left: rounded browser chrome; hand-authored source lettering. Local Lucide originals and atomic-debug geometry were inspected where used.

## Reduction

- Two tiny chrome dashes omitted to give the lettering more space.

## Visual review

Hand-authored A and D remain readable. D bowl is too close to the browser wall; other exact-minimum gaps also produce warnings. Not approved.

Reviewed at native 48px and enlarged size in light and dark themes. Matched screen/box corners use shared parameters; cab, receiver, cursor and directional symbols retain source asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [browser]: browser and d-bowl are 6 apart on centerlines nearest (42, 28)<->(36, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [browser]: browser and letter-a are 8 apart on centerlines nearest (14, 42)<->(14, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [letter-a]: letter-a and d-stem are 8 apart on centerlines nearest (22, 34)<->(30, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
