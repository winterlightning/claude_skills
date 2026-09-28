"""A desk rotary telephone: a handset resting on two cradle posts over a domed base with a round dial.

Symbol plan: symmetric about x=24. The handset is one closed pill (8 thick, r4 round
ends). Two cradle posts drop from its underside to the base (shared endpoints), 8
apart. The base is one closed outline: a short flat top between the posts, r12 shoulders
curving down to straight sides, r2 bottom corners and a flat bottom. The dial is a ring
(r3, approved 6-diameter circle) centred in the base, 9 from its top and bottom.
The reference's drooping handset ends are drawn as round pill ends (drooped ends would
sit closer than 8 to the posts), and its dial is smaller: the base is 24 tall at most
under the handset and posts.
Lucide construction: 'phone' / retro telephone - handset over a domed base with a dial.
Keyshape VRECT_L: centerline x 8..40 (handset ends, base sides), y 4..44 (handset, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c6045a6f-cf65-4a9e-88d7-2c4f251336f9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__desk-rotary-telephone/20260926T044250Z-thuan-mac/reference/phone retro_c6045a6f-cf65-4a9e-88d7-2c4f251336f9.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class DeskRotaryTelephone(Solo48):
    icon_id = "desk-rotary-telephone"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("phone retro", "rotary phone", "old telephone")
    keywords = ("telephone", "phone", "rotary", "retro", "vintage", "call", "dial", "landline")

    def build(self) -> None:
        top, under, base_top, bottom = 4, 12, 20, 44
        pl, pr = 20, 28  # posts
        # handset pill
        self.add_line("hs-top", (12, top), (36, top))
        self.add_arc("hs-end-r", (36, top), (36, under), radius_x=4)
        self.add_line("hs-under-r", (36, under), (pr, under))
        self.add_line("hs-under-m", (pr, under), (pl, under))
        self.add_line("hs-under-l", (pl, under), (12, under))
        self.add_arc("hs-end-l", (12, under), (12, top), radius_x=4)
        self.add_contour("handset", "hs-top", "hs-end-r", "hs-under-r", "hs-under-m", "hs-under-l", "hs-end-l",
                         closed=True)
        # base
        self.add_line("base-top", (pl, base_top), (pr, base_top))
        self.add_arc("shoulder-r", (pr, base_top), (40, 32), radius_x=12)
        self.add_line("side-r", (40, 32), (40, bottom - 2))
        self.add_arc("corner-r", (40, bottom - 2), (38, bottom), radius_x=2)
        self.add_line("base-bottom", (38, bottom), (10, bottom))
        self.add_arc("corner-l", (10, bottom), (8, bottom - 2), radius_x=2)
        self.add_line("side-l", (8, bottom - 2), (8, 32))
        self.add_arc("shoulder-l", (8, 32), (pl, base_top), radius_x=12)
        self.add_contour("base", "base-top", "shoulder-r", "side-r", "corner-r", "base-bottom", "corner-l",
                         "side-l", "shoulder-l", closed=True)
        # posts
        for x in (pl, pr):
            self.add_line(f"post-{x}", (x, under), (x, base_top))
            self.relate("connect", "handset", f"post-{x}")
            self.relate("connect", "base", f"post-{x}")
        # dial
        cx, cy, r = 24, 32, 3
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ("dial-nw", "dial-ne", "dial-se", "dial-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("dial", *names, closed=True)
