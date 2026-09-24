# card game dice

Two suit cards and foreground die; restore the reference two-pip face and enlarge the die opening.

## Provenance

Source UUID: `7313c8ec-d635-4b38-acd5-fea39286b43e`.
Input: `icon_set/work/todo-references/card game dice_7313c8ec-d635-4b38-acd5-fea39286b43e.svg`.
Prior result: `icon_set/work/primitive-make-ray/7313c8ec-d635-4b38-acd5-fea39286b43e/20260922T222321-2443bd/result.json` (invalid).

## Keyshape

SQUARE: Visible ink (4,4)–(44,44), centerline envelope (6,6)–(42,42), balances the complete composition.

## Construction references

spade, diamond and dice-4: suit shapes, die enclosure and pip series; pip count comes from the supplied reference. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

- Removed the two extra lower pips invented by the parent; the supplied reference has two visible pips.

## Visual review

Two cards, both suits and foreground die remain. The die now has the source two visible pips, correcting the parent four-pip interpretation. Suit and die clearances still fail; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [diamond]: parallel straight edges diamond-4 and diamond-2 are 6.37905 apart on centerlines (ink gap 2.37905); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [diamond]: parallel straight edges diamond-1 and diamond-3 are 7.18399 apart on centerlines (ink gap 3.18399); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [die]: die and stem are 1 apart on centerlines nearest (32, 24)<->(32, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [die]: die and pip-0 are 8 apart on centerlines nearest (18, 33)<->(26, 33); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [die]: die and pip-1 are 8 apart on centerlines nearest (42, 33)<->(34, 33); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
