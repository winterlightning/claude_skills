# concert rock

A horns hand gesture with three lightning accents.

**SQUARE**: The overall composition uses the 36 by36 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: hand-metal: rounded raised fingers and folded middle fingers; shared human references supply anatomy principles.

Reduction: Fine palm crease omitted; thumb contour and all three lightning accents retained.

Validation: **invalid**, 4 errors, 1 warnings.

Visual review at48px and240px in light and dark: **not approved**. The horns gesture and three energy marks remain, but folded fingers/thumb overlap and the lightning marks crowd the fingertips. Not approved.

Human construction evidence:

```json
{
  "references": [
    "icon_set/references/human_ref/user.svg",
    "icon_set/references/human_ref/full_body_ref.png",
    "icon_set/references/lucide/original/hand-metal.svg",
    "icon_set/references/lucide/atomic-debug/hand-metal.svg"
  ],
  "construction": "Continuous hand anatomy. No detached head/body gap applies. Folded fingers and thumb remain visually crowded."
}
```

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [top-bolt]: parallel straight edges top-bolt-1 and top-bolt-3 are 4.24264 apart on centerlines (ink gap 0.242641); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [hand]: hand and left-bolt are 5.4341 apart on centerlines nearest (13.86, 18.6206)<->(11, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [hand]: hand and top-bolt are 7.31371 apart on centerlines nearest (18.8284, 19.1716)<->(24, 14); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [hand]: hand and right-bolt are 6 apart on centerlines nearest (36, 18)<->(36, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [fold]: fold and thumb are 0 apart on centerlines nearest (26, 32.6072)<->(26, 32.6072); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](concert-rock.svg) · [Python](concert_rock_3a11e17f_1153_59b2_b135_910a41a584c7.py) · [Light](light-240.png) · [Dark](dark-240.png)
