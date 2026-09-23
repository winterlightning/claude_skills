# people arrows

Two people with a bidirectional arrow between them.

Keyshape: HRECT_L. Wide scene; target centerline box (4,8)-(44,40).

Plan: Two identical circular heads and broad shoulder arcs, plus a centered horizontal double arrow.

Construction: user-search: simple circular head; shared human_ref/user.svg owns head and shoulder proportions.

Omissions: None; full bidirectional arrow retained.

Visual review: Two identical busts and full bidirectional arrow remain legible, but the arrow wings touch the shoulder ink. Not visually approved.

Human construction: Two heads r=5 at y=13 end at y=18. Shoulder arcs have apex y=26: exact centerline gap 8, ink gap 4. Busts are not stick figures.

```text
status: invalid
  ERROR  mic [person-0-shoulders]: person-0-shoulders and arrow-left are 3.99946 apart on centerlines nearest (19.9989, 31.9346)<->(16, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [person-1-shoulders]: person-1-shoulders and arrow-right are 3.99946 apart on centerlines nearest (28.0011, 31.9346)<->(32, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
