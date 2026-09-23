# snorer

Sleeping person in bed with two hand-authored Z marks overhead.

SQUARE: Square overall composition; target visible envelope (4,4)-(44,44).

bed: simple bedding silhouette; human_ref/user.svg and full_body_ref.png: circular head and smooth shoulder construction.

Omitted minor pillow crease; retained pillow, blanket and both Zs.

Sleeping head, pillow, blanket and both Zs retained. Own torso junction is at y39, exactly 8 centerline units below the head bottom at y31, giving 4 ink units. Pillow and Z lettering violate clearance; not approved.

```text
status: invalid
  ERROR  mic [large]: parallel straight edges large-1 and large-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [small]: parallel straight edges small-1 and small-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [head]: head and pillow are 3.05584 apart on centerlines nearest (15.3368, 30.9628)<->(15, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [head]: head and small are 2.06242 apart on centerlines nearest (21.2181, 22.0385)<->(23, 21); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [small]: small and large are 5 apart on centerlines nearest (29, 15)<->(33, 12); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
