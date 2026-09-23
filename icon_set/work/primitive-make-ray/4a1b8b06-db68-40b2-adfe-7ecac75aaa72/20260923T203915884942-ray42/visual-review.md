# shoemaker

Shoemaker with a circular head, apron and a shoe in the lower right foreground.

SQUARE: Square overall composition; visible envelope (4,4)-(44,44).

human_ref/user.svg and full_body_ref.png: circular head and broad smooth shoulders; no exact shoe match.

Omitted small apron side seam; retained apron, shoulder outline and shoe.

Circular head has exact gap 28-(13+7)=8 centerline units, 4 ink units, above its own shoulder junction. Apron and foreground shoe crowd each other; not approved.

```text
status: invalid
  ERROR  mic [shoulder-right]: shoulder-right and shoe are 1.14414 apart on centerlines nearest (34, 34)<->(34.0407, 35.1434); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [apron]: apron and shoe are 1 apart on centerlines nearest (22, 42)<->(23, 42); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
