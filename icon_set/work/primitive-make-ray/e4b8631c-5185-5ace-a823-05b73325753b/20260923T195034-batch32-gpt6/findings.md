# pen tools

A pen nib beneath vector curve control handles.

Keyshape: SQUARE. Balanced composition; target centerline box (6,6)-(42,42).

Plan: Symmetric nib, central hole, repeated control nodes and a broad curve.

Construction: pen-tool: nib, slit and circular hole; source adds curve handles.

Omissions: None; all defining controls and nib parts retained.

Visual review: Curve handles, control node and nib remain present. The nib hole closes at 48px and the nib crowds the control square. Not visually approved.

```text
status: invalid
  ERROR  mic [control-square]: control-square and nib are 4 apart on centerlines nearest (24, 14)<->(24, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [curve-left]: curve-left and curve-right are 8 apart on centerlines nearest (20, 10)<->(28, 10); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
