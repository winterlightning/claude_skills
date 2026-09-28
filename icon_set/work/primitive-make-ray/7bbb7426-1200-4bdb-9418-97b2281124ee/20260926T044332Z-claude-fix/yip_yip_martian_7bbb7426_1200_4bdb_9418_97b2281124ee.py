"""A Yip Yip martian: a bell-shaped body under two big ring eyes joined by a bridge, with curling antennae, on the ground.

Symbol plan: symmetric about x=24. Two ring eyes (r5) 8 apart, joined by a straight
bridge between their inner points. From each eye's top a bezier antenna rises, arches
outward over the top edge and hooks down at its tip. From a 3-4-5 point low on each eye's outer side a
bezier body side bulges down to the ground line, which runs across the full width
(split where the sides land). All joins are shared endpoints.
Lucide construction: none; ring-eye and dome construction.
Keyshape SQUARE: centerline x 6..42 (ground line), y 6..42 (antenna arches, ground).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7bbb7426-1200-4bdb-9418-97b2281124ee"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__yip-yip-martian/20260926T044250Z-thuan-mac/reference/sesame street yip yips_7bbb7426-1200-4bdb-9418-97b2281124ee.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class YipYipMartian(Solo48):
    icon_id = "yip-yip-martian"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/character"
    aliases = ("yip yip", "sesame street yip yips", "martian")
    keywords = ("martian", "alien", "yip yip", "antennae", "creature", "cartoon", "sesame street")

    def build(self) -> None:
        ex, ey, r = 15, 18, 5
        ground = 42
        for side, sx in (("l", 1), ("r", -1)):
            c = (ex, ey) if sx == 1 else _m((ex, ey))
            cx = c[0]
            top, inner, bot, outer = (cx, ey - r), (cx + sx * r, ey), (cx, ey + r), (cx - sx * r, ey)
            low = (cx - sx * 3, ey + 4)  # 3-4-5 point on the outer-lower side
            pts = [outer, top, inner, bot, low]
            names = [f"eye-{side}-{k}" for k in range(5)]
            for i, n in enumerate(names):
                a, b = pts[i], pts[(i + 1) % 5]
                self.add_arc(n, a, b, radius_x=r, sweep=(sx == 1))
            self.add_contour(f"eye-{side}", *names, closed=True)
            # antenna
            p = lambda x, y: (x, y) if sx == 1 else _m((x, y))
            self.add_bezier(f"antenna-{side}", top, (p(15, 8), p(13, 6), p(11, 6)), (p(9, 6), p(7, 6), p(6, 8)))
            self.relate("connect", f"eye-{side}", f"antenna-{side}")
            # body side
            self.add_bezier(f"side-{side}", low, (p(9, 27), p(7, 33), p(7, ground)))
            self.relate("connect", f"eye-{side}", f"side-{side}")
        self.add_line("bridge", (ex + r, ey), _m((ex + r, ey)))
        self.relate("connect", "eye-l", "bridge")
        self.relate("connect", "eye-r", "bridge")
        self.add_line("ground-l", (6, ground), (7, ground))
        self.add_line("ground-m", (7, ground), (41, ground))
        self.add_line("ground-r", (41, ground), (42, ground))
        self.add_contour("ground", "ground-l", "ground-m", "ground-r")
        self.relate("connect", "ground", "side-l")
        self.relate("connect", "ground", "side-r")
