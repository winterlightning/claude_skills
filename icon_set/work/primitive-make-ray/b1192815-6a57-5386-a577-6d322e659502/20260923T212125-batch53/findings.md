# user mobility

A user node linked to three surrounding mobility nodes.

Keyshape: **SQUARE**. The complete composition is distributed across a square envelope. The module records the exact profile bounds in `ink_extremes`.

Construction reference: network: three repeated connections; human_ref/user.svg: head and shoulder vocabulary.

Omissions/reduction: None; user enclosure and three nodes retained.

Validation: **invalid**, 1 errors, 1 warnings.

Visual review at 48px and enlarged, light and dark: **needs-review**. All three satellite nodes and the user enclosure remain. The head is too close to the ring and the shoulder arc crosses it.

Human reference: `icon_set/skills/icon-design/human-reference.md; icon_set/references/human_ref/user.svg`. Detached head bottom y=22, torso top y=30: 8 centerline units / 4 ink units.

status: invalid
  ERROR  mic [user-ring]: user-ring and head are 3.9997 apart on centerlines nearest (18.0491, 12.0006)<->(18, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [user-ring]: user-ring and shoulders are 0 apart on centerlines nearest (10.1977, 33.1166)<->(10.1977, 33.1166); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

[SVG](user-mobility.svg) · [Python](user_mobility_b1192815_6a57_5386_a577_6d322e659502.py) · [Light preview](light-240.png) · [Dark preview](dark-240.png)
