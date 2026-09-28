"""A dog collar seen from the front and slightly above: a wide band with a round tag hanging
from a short link.

Symbol plan: symmetric about x = 24. The band is drawn as a short cylinder: a closed top
ellipse (rx 18, ry 5) about (24, 11), vertical sides x 6 and 42 from y 11 to 20, and a
front edge made of two quarter ellipses (rx 18, ry 5) meeting at (24, 25), 9 below the
top ellipse. A straight link drops from (24, 25) to the top of an r4 tag ring about
(24, 38), 9 below the band, whose bottom is the keyshape's bottom edge.
Lucide construction: 'cylinder' (ellipse top, straight sides, front arc) for the band,
'circle' for the tag.
Keyshape SQUARE: centerline x 6..42 (band sides), y 6..42 (top ellipse, tag bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "23613560-7dd5-5dd6-a408-af639d617ca0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-collar-with-tag-ring/20260926T055140Z-thuan-mac/reference/dog collar_23613560-7dd5-5dd6-a408-af639d617ca0.svg"
AUTHOR = "claude-opus-5-5"


class DogCollarWithTagRing(Solo48):
    icon_id = "dog-collar-with-tag-ring"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pet"
    aliases = ("dog collar", "pet collar", "collar tag")
    keywords = ("collar", "dog", "pet", "tag", "id", "band", "leash", "puppy", "accessory")

    def ellipse(self, name, cx, cy, rx, ry):
        pts = [(cx - rx, cy), (cx, cy - ry), (cx + rx, cy), (cx, cy + ry)]
        names = tuple(f"{name}-{q}" for q in ("nw", "ne", "se", "sw"))
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *names, closed=True)

    def build(self) -> None:
        cx, top_y, rx, ry, side = 24, 11, 18, 5, 20
        self.ellipse("band-top", cx, top_y, rx, ry)
        front = side + ry
        self.add_line("band-side-left", (cx - rx, top_y), (cx - rx, side))
        self.add_arc("band-front-left", (cx - rx, side), (cx, front), radius_x=rx, radius_y=ry, sweep=False)
        self.add_arc("band-front-right", (cx, front), (cx + rx, side), radius_x=rx, radius_y=ry, sweep=False)
        self.add_line("band-side-right", (cx + rx, side), (cx + rx, top_y))
        self.add_contour("band-front", "band-side-left", "band-front-left", "band-front-right",
                         "band-side-right")
        self.relate("connect", "band-top", "band-front")
        tr, tag_cy = 4, 38
        self.add_line("link", (cx, front), (cx, tag_cy - tr))
        self.ellipse("tag", cx, tag_cy, tr, tr)
        self.relate("connect", "band-front", "link")
        self.relate("connect", "link", "tag")
