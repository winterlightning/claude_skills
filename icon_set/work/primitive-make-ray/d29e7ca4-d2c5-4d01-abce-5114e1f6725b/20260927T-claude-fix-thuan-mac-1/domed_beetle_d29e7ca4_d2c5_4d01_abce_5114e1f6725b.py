"""Domed beetle: a beetle seen from above -- small head with two curling
antennae, a big domed shell split down the middle into two wing cases, and three
jointed legs on each side.

Revision (disapproved, reason not recorded): the rejected drawing had no head;
its antennae were two straight lines crossing in an X over the shell and its
legs were straight stubs, so it read as a crossed-out bug. The original shows a
distinct head carrying two antennae that curve up and outward, a domed shell
with a centre seam, and bent legs. All three are restored.

Symbol plan: mirror axis x=24. Shell: flat shoulders (14,21)-(34,21) with radius-4
corners, straight sides to y=31 and a radius-10 rear about (24,31) (tail 41).
Seam: x=24 from the head (24,12) to the tail, splitting the shell into two 10-wide
wing cases. Head: radius-3 ring about (24,9), 9 above the shoulders. Antennae:
cubics from the head's sides (21,9)/(27,9) sweeping out to (13,6)/(35,6). Legs,
one bend each: front (14,25)-(9,22)-(6,16), middle (14,31)-(8,31)-(6,34), hind
from the rear's 6-8-10 point (18,39)-(12,40)-(10,42), mirrored on the right.
Omissions: the pronotum (a second band would close sub-minimum holes).
Lucide construction: 'bug' (head, split body, legs).
Keyshape SQUARE: centerline (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d29e7ca4-d2c5-4d01-abce-5114e1f6725b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__domed-beetle/20260926T182653Z-thuan-mac-1/reference/silk bug_d29e7ca4-d2c5-4d01-abce-5114e1f6725b.svg"
AUTHOR = "claude-opus-5-5"


def mirror(p):
    return (48 - p[0], p[1])


class DomedBeetle(Solo48):
    icon_id = "domed-beetle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/insects"
    aliases = ("beetle", "silk-bug", "bug")
    keywords = ("beetle", "bug", "insect", "shell", "antennae", "legs", "silk")

    def build(self) -> None:
        self.add_line("shoulder-left", (18, 21), (24, 21))
        self.add_line("shoulder-right", (24, 21), (30, 21))
        self.add_arc("corner-right", (30, 21), (34, 25), radius_x=4)
        self.add_line("side-right", (34, 25), (34, 31))
        self.add_arc("rear-right", (34, 31), (30, 39), radius_x=10)
        self.add_arc("rear-mid-right", (30, 39), (24, 41), radius_x=10)
        self.add_arc("rear-mid-left", (24, 41), (18, 39), radius_x=10)
        self.add_arc("rear-left", (18, 39), (14, 31), radius_x=10)
        self.add_line("side-left", (14, 31), (14, 25))
        self.add_arc("corner-left", (14, 25), (18, 21), radius_x=4)
        self.add_contour("shell", "shoulder-right", "corner-right", "side-right", "rear-right", "rear-mid-right",
                         "rear-mid-left", "rear-left", "side-left", "corner-left", "shoulder-left", closed=True)
        self.add_line("neck", (24, 12), (24, 21))
        self.add_line("seam", (24, 21), (24, 41))
        self.add_contour("spine", "neck", "seam")
        self.relate("connect", "shell", "spine")

        cx, cy, r = 24, 9, 3
        self.add_arc("head-a", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("head-b", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("head-c", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc("head-d", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour("head", "head-a", "head-b", "head-c", "head-d", closed=True)
        self.relate("connect", "head", "spine")

        for side, m in (("left", lambda p: p), ("right", mirror)):
            self.add_bezier(f"antenna-{side}", m((21, 9)), (m((18, 9)), m((16, 7.5)), m((13, 6))))
            self.relate("connect", "head", f"antenna-{side}")
            for leg, pts in (("front", ((14, 25), (9, 22), (6, 16))),
                             ("middle", ((14, 31), (8, 31), (6, 34))),
                             ("hind", ((18, 39), (12, 40), (10, 42)))):
                self.add_polyline(f"leg-{leg}-{side}", *(m(p) for p in pts))
                self.relate("connect", "shell", f"leg-{leg}-{side}")
