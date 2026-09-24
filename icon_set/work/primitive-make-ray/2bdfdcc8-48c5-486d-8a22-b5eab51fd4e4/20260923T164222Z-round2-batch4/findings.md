# co working space plug users

Two coworkers below a disconnected plug and socket joined by an outer cord.

**SQUARE**: The overall composition uses the 36 by36 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: plug: cap and paired prongs; human_ref/user.svg: equivalent circular heads and shoulders.

Reduction: Socket holes reduced from two to one; closed shoulder bases omitted for clear bust silhouettes.

Validation: **invalid**, 4 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. Both users, plug, socket and cord are retained. Cord-to-plug and socket-hole spacing remain too tight; shoulders are shallow relative to the shared human reference. Not approved.

Human construction evidence:

```json
{
  "reference": "icon_set/references/human_ref/user.svg",
  "figures": 2,
  "head_centers": [
    [
      13,
      28
    ],
    [
      35,
      28
    ]
  ],
  "radius": 4,
  "head_bottom": 32,
  "shoulder_apex_y": 40,
  "centerline_gap": 8,
  "ink_gap": 4,
  "construction": "Outlined busts, not stick figures. Shoulder arcs are shallow; visual approval withheld."
}
```

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [plug]: parallel straight edges plug-6-1, plug-6-0 and cord-left-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [plug]: parallel straight edges plug-4-0 and cord-left-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [socket]: parallel straight edges socket-4-0 and cord-right-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [socket]: socket and socket-hole are 5 apart on centerlines nearest (42, 12)<->(37, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](co-working-space-plug-users.svg) · [Python](co_working_space_plug_users_2bdfdcc8_48c5_486d_8a22_b5eab51fd4e4.py) · [Light](light-240.png) · [Dark](dark-240.png)
