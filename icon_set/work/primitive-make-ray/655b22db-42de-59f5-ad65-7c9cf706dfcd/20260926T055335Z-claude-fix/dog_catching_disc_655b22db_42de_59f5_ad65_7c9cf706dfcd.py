"""A dog's head in profile, facing left, catching a flying disc in its mouth.

Symbol plan: the disc is a closed ellipse (rx 7, ry 5) about (13, 33), split at its top
and right points where the jaws attach. The head is one open outline: the snout front
rises from the disc top (13, 28) to the nose (10, 20), the muzzle top runs back to the
stop (22, 17), the forehead climbs to the ear, the pointed ear peaks at (30, 6), the back
of the skull falls on an r15 arc (centre (27, 26)) to a vertical tangent at (42, 26), and
the back of the neck drops straight to (42, 42). The lower jaw leaves the disc's right
point (20, 33) and the throat drops to (30, 42). An eye dot at (29, 23) sits 9+ from every
line. A first attempt without skull and neck (attempts/v1-*) read as a hook and failed
the build gate's internal spacing (muzzle over the disc).
Lucide construction: no Lucide dog-with-disc; the open profile outline follows Lucide's
'dog' head profile (pointed ear, domed skull, straight muzzle), the disc Lucide's ellipse construction.
Keyshape SQUARE: centerline x 6..42 (disc left, neck back), y 6..42 (ear tip, neck).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "655b22db-42de-59f5-ad65-7c9cf706dfcd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-catching-disc/20260926T055140Z-thuan-mac/reference/dog play bring disc_655b22db-42de-59f5-ad65-7c9cf706dfcd.svg"
AUTHOR = "claude-opus-5-5"


class DogCatchingDisc(Solo48):
    icon_id = "dog-catching-disc"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("dog play bring disc", "dog frisbee", "fetch")
    keywords = ("dog", "frisbee", "disc", "fetch", "play", "pet", "catch", "puppy", "toy")

    def build(self) -> None:
        cx, cy, rx, ry = 13, 33, 7, 5
        pts = [(cx - rx, cy), (cx, cy - ry), (cx + rx, cy), (cx, cy + ry)]
        names = ("disc-nw", "disc-ne", "disc-se", "disc-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=rx, radius_y=ry)
        self.add_contour("disc", *names, closed=True)
        # head outline from the disc top round the skull to the back of the neck
        self.add_line("snout-front", (cx, cy - ry), (10, 20))
        self.add_line("muzzle-top", (10, 20), (22, 17))
        self.add_line("forehead", (22, 17), (27, 12))
        self.add_line("ear-front", (27, 12), (30, 6))
        self.add_line("ear-back", (30, 6), (36, 14))
        self.add_arc("skull", (36, 14), (42, 26), radius_x=15)
        self.add_line("neck-back", (42, 26), (42, 42))
        self.add_contour("head", "snout-front", "muzzle-top", "forehead", "ear-front", "ear-back",
                         "skull", "neck-back")
        self.add_polyline("jaw", (cx + rx, cy), (26, 33), (30, 42))
        self.relate("connect", "disc", "head")
        self.relate("connect", "disc", "jaw")
        self.add_dot("eye", (29, 23))
