# veterinarian

A veterinarian with a stethoscope and cat badge.

Keyshape: **SQUARE**. The complete composition is distributed across a square envelope. The module records the exact profile bounds in `ink_extremes`.

Construction reference: human_ref/user.svg: circular head and shoulders; stethoscope: tubing and bell; source supplies cat badge.

Omissions/reduction: Fine facial detail omitted; collar, stethoscope and cat retained.

Validation: **invalid**, 6 errors, 3 warnings.

Visual review at 48px and enlarged, light and dark: **needs-review**. Clinician head remains clear, but collar, stethoscope and cat badge overlap heavily. Cat identity is weak at native size; unsuccessful attempt retained.

Human reference: `icon_set/skills/icon-design/human-reference.md; icon_set/references/human_ref/user.svg`. Detached head bottom y=18, torso top y=26: 8 centerline units / 4 ink units.

status: invalid
  ERROR  mic [shoulders]: shoulders and stethoscope-tube are 0.544138 apart on centerlines nearest (13.8883, 26.4674)<->(14, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [collar]: collar and stethoscope-tube are 2.23607 apart on centerlines nearest (16, 26)<->(14, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [collar]: collar and badge are 2.40181 apart on centerlines nearest (24, 26)<->(25.9049, 27.4629); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [collar]: collar and cat-ears are 4.12311 apart on centerlines nearest (24, 26)<->(28, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [stethoscope-bell]: stethoscope-bell and badge are 7.2362 apart on centerlines nearest (16.9675, 35.5598)<->(24.1118, 34.4103); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [badge]: badge and cat-ears are 1.18916 apart on centerlines nearest (38.7656, 26.0901)<->(38, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [shoulders]: shoulders and collar are 0 apart on centerlines nearest (16.1453, 26.1453)<->(16.1453, 26.1453); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [shoulders]: shoulders and badge are 0 apart on centerlines nearest (26.4069, 26.8747)<->(26.4069, 26.8747); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [shoulders]: shoulders and cat-ears are 0 apart on centerlines nearest (28, 27.5323)<->(28, 27.5323); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

[SVG](veterinarian.svg) · [Python](veterinarian_16ebf22c_f2dd_4834_bf5b_3033fd6dbd8a.py) · [Light preview](light-240.png) · [Dark preview](dark-240.png)
