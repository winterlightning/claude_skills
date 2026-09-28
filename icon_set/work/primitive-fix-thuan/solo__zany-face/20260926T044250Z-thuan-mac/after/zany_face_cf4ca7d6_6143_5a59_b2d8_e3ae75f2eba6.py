"""A zany face: one crossed-out eye, one wide round eye, and a wide open grin with the tongue hanging out.

Symbol plan: the face's features drawn large: an X eye (two crossing diagonals, split at
the exact centre node) at the upper left, a ring eye (r4) at the upper right, and one
open run for the grin - a flat top lip from corner to corner closed by a lower lip whose
middle is the tongue: each lower-lip cubic drops to the tongue's shoulders, the tongue
walls (8 apart) run down and close in an r4 tip. Eyes sit 9 above the lip.
The reference's round head outline is dropped: inside an r20 rim every feature must stay
within radius 12 of the centre, and two eyes 8 apart plus a mouth with a tongue do not fit.
Lucide construction: 'laugh'/'smile' face features (open grin, round eyes).
Keyshape SQUARE: centerline x 6..42 (mouth corners), y 6..42 (eyes top, tongue tip).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cf4ca7d6-6143-5a59-b2d8-e3ae75f2eba6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__zany-face/20260926T044250Z-thuan-mac/reference/zany face_cf4ca7d6-6143-5a59-b2d8-e3ae75f2eba6.svg"
AUTHOR = "claude-opus-5-5"


class ZanyFace(Solo48):
    icon_id = "zany-face"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotion"
    aliases = ("crazy face", "goofy face", "zany")
    keywords = ("zany", "crazy", "goofy", "silly", "tongue", "wink", "emoji", "face", "fun")

    def build(self) -> None:
        # X eye
        ex, ey, h = 12, 10, 4
        c = (ex, ey)
        self.add_line("x-a1", (ex - h, ey - h), c)
        self.add_line("x-a2", c, (ex + h, ey + h))
        self.add_line("x-b1", (ex + h, ey - h), c)
        self.add_line("x-b2", c, (ex - h, ey + h))
        self.add_contour("x-a", "x-a1", "x-a2")
        self.add_contour("x-b", "x-b1", "x-b2")
        self.relate("connect", "x-a", "x-b")
        # ring eye
        ox, oy, r = 34, 10, 4
        pts = [(ox - r, oy), (ox, oy - r), (ox + r, oy), (ox, oy + r)]
        names = ("eye-nw", "eye-ne", "eye-se", "eye-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("eye", *names, closed=True)
        # grin with tongue
        lip, low, tl, tr, tip = 23, 33, 20, 28, 38
        self.add_line("lip-top", (6, lip), (42, lip))
        self.add_bezier("lip-right", (42, lip), ((40, 30), (34, low), (tr, low)))
        self.add_line("tongue-right", (tr, low), (tr, tip))
        self.add_arc("tongue-tip", (tr, tip), (tl, tip), radius_x=4)
        self.add_line("tongue-left", (tl, tip), (tl, low))
        self.add_bezier("lip-left", (tl, low), ((14, low), (8, 30), (6, lip)))
        self.add_contour("mouth", "lip-top", "lip-right", "tongue-right", "tongue-tip", "tongue-left",
                         "lip-left", closed=True)
