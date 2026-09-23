# user drop zone 1

A large P node connected to two smaller nodes.

Keyshape: **SQUARE**. The complete composition is distributed across a square envelope. The module records the exact profile bounds in `ink_extremes`.

Construction reference: network: shared endpoints between node outlines and connecting branches.

Omissions/reduction: None; the literal P from the input is retained.

Validation: **invalid**, 2 errors, 0 warnings.

Visual review at 48px and enlarged, light and dark: **needs-review**. The P and two satellite nodes read correctly, but the P bowl crowds its enclosure and the upper branch.

status: invalid
  ERROR  mic [upper-link]: parallel straight edges upper-link and p-stem-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [main]: main and p-bowl are 4.99981 apart on centerlines nearest (28.3858, 12.7896)<->(25.3828, 16.7872); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

[SVG](user-drop-zone-1.svg) · [Python](user_drop_zone_1_d40b2438_c966_462c_8e4e_d118211694e3.py) · [Light preview](light-240.png) · [Dark preview](dark-240.png)
