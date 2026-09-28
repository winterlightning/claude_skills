"""A dog looking up at a ball and reaching toward it with a raised front paw.

Symbol plan: the dog faces left and looks up at the ball. The head is one open contour:
from the inner edge of the floppy ear (33, 20) down to (33, 26), round the ear's r4 bottom
(centre (37, 26)) and up its back edge x 41 to the skull, over an r8 quarter-arc skull
(centre (33, 14)) to the crown (33, 6), along the snout top to the nose (21, 10), down the
nose front and back along a short jaw to (25, 18). The neck falls from the ear bottom
(37, 30) to (42, 42). The chest drops from (25, 27), 9 below the jaw, to the ground; the
raised front leg leaves it at (25, 32), runs forward to (14, 30) and lifts its paw to
(9, 22) toward the ball, an r3 ring (approved 6-diameter circle) about (9, 9).
A first attempt without the ear (attempts/v1-no-ear.svg) read as a letter.
Lucide construction: no Lucide dog profile; quarter-arc skull and snout follow Lucide's
rounded-corner construction, the ball Lucide's circle.
Keyshape SQUARE: centerline x 6..42 (ball, neck end), y 6..42 (ball and crown, chest and neck ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5e7c3d9-93a4-51aa-af25-f4dfca60a44e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-reaching-for-ball/20260926T055140Z-thuan-mac/reference/dog playing ball_f5e7c3d9-93a4-51aa-af25-f4dfca60a44e.svg"
AUTHOR = "claude-opus-5-5"


class DogReachingForBall(Solo48):
    icon_id = "dog-reaching-for-ball"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("dog playing ball", "dog play", "fetch")
    keywords = ("dog", "ball", "play", "fetch", "pet", "puppy", "toy", "game", "paw")

    def build(self) -> None:
        self.add_line("ear-front", (33, 20), (33, 26))
        self.add_arc("ear-bottom-front", (33, 26), (37, 30), radius_x=4, sweep=False)
        self.add_arc("ear-bottom-back", (37, 30), (41, 26), radius_x=4, sweep=False)
        self.add_line("ear-back", (41, 26), (41, 14))
        self.add_arc("skull", (41, 14), (33, 6), radius_x=8, sweep=False)
        self.add_line("snout-top", (33, 6), (21, 10))
        self.add_line("nose", (21, 10), (21, 16))
        self.add_line("jaw", (21, 16), (25, 18))
        self.add_contour("head", "ear-front", "ear-bottom-front", "ear-bottom-back", "ear-back", "skull",
                         "snout-top", "nose", "jaw")
        self.add_line("neck", (37, 30), (42, 42))
        self.relate("connect", "head", "neck")
        self.add_line("chest-upper", (25, 27), (25, 32))
        self.add_line("chest-lower", (25, 32), (25, 42))
        self.add_contour("chest", "chest-upper", "chest-lower")
        self.add_polyline("raised-leg", (25, 32), (14, 30), (9, 22))
        self.relate("connect", "chest", "raised-leg")
        cx, cy, r = 9, 9, 3
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ("ball-nw", "ball-ne", "ball-se", "ball-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("ball", *names, closed=True)
