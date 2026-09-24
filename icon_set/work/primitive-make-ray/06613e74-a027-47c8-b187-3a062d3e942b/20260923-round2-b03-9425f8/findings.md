# card game diamond

Three outlined diamonds on an upright playing card; enlarge corner diamonds and reduce the center to test the spacing budget.

## Provenance

Source UUID: `06613e74-a027-47c8-b187-3a062d3e942b`.
Input: `icon_set/work/todo-references/card game diamond_06613e74-a027-47c8-b187-3a062d3e942b.svg`.
Prior result: `icon_set/work/primitive-make-ray/06613e74-a027-47c8-b187-3a062d3e942b/20260922T222300-80fc00/result.json` (invalid).

## Keyshape

VRECT_L: Visible ink (6,2)–(42,46), centerline envelope (8,4)–(40,44), preserves the upright sheet/card and gives vertical content room.

## Construction references

diamond: repeated outlined rhombi from shared center and radius parameters. Local original and atomic-debug geometry inspected where Lucide construction is used.

## Reductions

No defining feature intentionally omitted.

## Visual review

Large center diamond and both outlined corner diamonds remain. Enlarging the corner symbols improves their openings but cannot satisfy all card and suit clearances; not approved.

Reviewed at 48px and enlarged size in both themes. Repeated figures, wheels, jaws, bindings and suit instances use shared dimensions. Card overlaps, speech tails, pointing hands and bolt directions preserve intentional asymmetry.

## Validation

```text
status: invalid
  ERROR  mic [upper]: parallel straight edges upper-4 and upper-2 are 6.24695 apart on centerlines (ink gap 2.24695); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [lower]: parallel straight edges lower-4 and lower-2 are 6.24695 apart on centerlines (ink gap 2.24695); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [upper]: parallel straight edges upper-1 and upper-3 are 6.24695 apart on centerlines (ink gap 2.24695); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [lower]: parallel straight edges lower-1 and lower-3 are 6.24695 apart on centerlines (ink gap 2.24695); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [card]: card and upper are 3 apart on centerlines nearest (16, 4)<->(16, 7); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [card]: card and lower are 3 apart on centerlines nearest (32, 44)<->(32, 41); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main]: main and upper are 5.62226 apart on centerlines nearest (24, 16)<->(19.6098, 12.4878); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [main]: main and lower are 5.62226 apart on centerlines nearest (24, 32)<->(28.3902, 35.5122); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
