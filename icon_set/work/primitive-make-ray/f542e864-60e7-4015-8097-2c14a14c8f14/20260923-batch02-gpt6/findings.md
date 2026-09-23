A plus-marked circular hub fans out to four connected square nodes.

Square overall composition; visible extremes (4,4)-(44,44), centerline (6,6)-(42,42).

Reference: icon_set/work/todo-references/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg

Construction: workflow: repeated box nodes with explicit connecting runs.

Omissions: Rounded corners simplified to square corners to preserve node openings.

Four-node fan composition is retained, but the plus in the hub and lower node cluster are congested. Asymmetry follows the directed fan arrangement.

```text
status: invalid
  ERROR  mic [right-lower]: parallel straight edges right-lower-4 and bottom-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [right-upper]: parallel straight edges right-upper-3 and right-lower-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [hub]: hub and plus-horizontal are 2.99977 apart on centerlines nearest (17.9995, 24.0368)<->(15, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship```
