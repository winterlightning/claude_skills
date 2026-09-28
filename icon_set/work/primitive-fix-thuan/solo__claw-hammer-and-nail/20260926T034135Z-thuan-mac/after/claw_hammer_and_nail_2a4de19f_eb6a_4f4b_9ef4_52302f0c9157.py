"""A claw hammer and a nail: a diagonal hammer with a curved claw, and a nail standing at the bottom right.

Symbol plan: everything on the 45-degree grid. The handle axis is x+y=48 and the head's
long axis is x-y=13; the head is a closed outline between the long sides x-y=7 and
x-y=19 (8.5 apart), a flat striking face on x+y=61, and a curved claw at the other end
(two cubics out to an integer tip, one back to the head). The handle is an open tube
between x+y=41 and x+y=55 (9.9 apart) hanging from the head's lower side at shared
points, closed by an r5 cap whose 3-4-5 endpoints keep the tube sides on the grid.
The nail is a T: a flat head line and a shank, 8+ from the hammer.
Lucide construction: 'hammer' - diagonal handle with a perpendicular head and claw.
Keyshape SQUARE: centerline x 6..42 (handle cap, nail head), y 6..42 (claw top, cap / nail point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2a4de19f-eb6a-4f4b-9ef4-52302f0c9157"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__claw-hammer-and-nail/20260926T034135Z-thuan-mac/reference/hardware hammer nail_2a4de19f-eb6a-4f4b-9ef4-52302f0c9157.svg"
AUTHOR = "claude-opus-5-5"


def _on(s: int, d: int) -> tuple[int, int]:
    """Point with x+y = s and x-y = d (same parity)."""
    return ((s + d) // 2, (s - d) // 2)


class ClawHammerAndNail(Solo48):
    icon_id = "claw-hammer-and-nail"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("hammer and nail", "hardware", "claw hammer")
    keywords = ("hammer", "nail", "tool", "hardware", "build", "carpentry", "diy", "repair", "construction")

    def build(self) -> None:
        low, up = 7, 19           # head long sides (x-y)
        claw_end, face = 35, 61   # head ends (x+y)
        tube_a, tube_b = 41, 55   # handle sides (x+y)
        cap_c = (11, 37)          # handle cap centre, on x+y=48
        # head
        u_claw, u_face = _on(claw_end, up), _on(face, up)
        l_face, l_b, l_a, l_claw = _on(face, low), _on(tube_b, low), _on(tube_a, low), _on(claw_end, low)
        tip, crest = (14, 15), (20, 6)
        self.add_line("head-top", u_claw, u_face)
        self.add_line("head-face", u_face, l_face)
        self.add_line("head-bottom-face", l_face, l_b)
        self.add_line("head-bottom-mid", l_b, l_a)
        self.add_line("head-bottom-claw", l_a, l_claw)
        self.add_bezier("claw-inner", l_claw, ((18, 14), (16, 15), tip))
        self.add_bezier("claw-outer", tip, ((14, 10), (16, 6), crest), ((23, 6), (25, 7), u_claw))
        self.add_contour("head", "head-top", "head-face", "head-bottom-face", "head-bottom-mid",
                         "head-bottom-claw", "claw-inner", "claw-outer", closed=True)
        # handle
        cap_a, cap_b = (cap_c[0] - 3, cap_c[1] - 4), (cap_c[0] + 4, cap_c[1] + 3)
        self.add_line("handle-upper", l_a, cap_a)
        self.add_arc("handle-cap", cap_a, cap_b, radius_x=5, large_arc=True, sweep=False)
        self.add_line("handle-lower", cap_b, l_b)
        self.add_contour("handle", "handle-upper", "handle-cap", "handle-lower")
        self.relate("connect", "head", "handle")
        # nail
        self.add_line("nail-head-l", (34, 36), (38, 36))
        self.add_line("nail-head-r", (38, 36), (42, 36))
        self.add_line("nail-shank", (38, 36), (38, 42))
        self.relate("connect", "nail-head-l", "nail-shank")
        self.relate("connect", "nail-head-r", "nail-shank")
        self.relate("connect", "nail-head-l", "nail-head-r")
