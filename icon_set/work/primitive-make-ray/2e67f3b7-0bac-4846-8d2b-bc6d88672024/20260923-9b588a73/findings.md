# nun

Nun portrait with circular jaw, arched veil, broad shoulders and chest cross. Human reference owns head and shoulder proportions.

Keyshape: VRECT_L, Tall upright subject; visible bounds (6, 2, 42, 46).

Omissions: Neck collar and inner headwear seam omitted to limit crowding; veil, face, shoulders and cross retained.

Visual review: Veil and cross identify the nun, but face-to-veil and chest-cross spacing fail. Jaw bottom y=23 and shoulder top y=31 establish exactly 8 centerline / 4 ink units; shared human_ref/user.svg informed proportions.

```text
status: invalid
  ERROR  mic [veil]: veil and face are 3.99975 apart on centerlines nearest (34.9995, 15.955)<->(31, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [veil]: veil and cross-bottom are 4 apart on centerlines nearest (24, 44)<->(24, 40); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [shoulders]: shoulders and cross-top are 0.999995 apart on centerlines nearest (24.0031, 31)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
