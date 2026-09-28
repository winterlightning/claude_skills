"""Battery 2: an upright battery with a wide, shallow top terminal, a plus sign in its
upper half and a minus sign in its lower half.

Symbol plan: mirror symmetry about x=24. One closed outline: a tall body x 10..38,
y 8..44 with small radius-3 corners, and a terminal x 16..32 raised 4 above the body
top (its 4-unit bay closes into a solid cap at stroke 4). The plus (arms 4) is
centred at (24,20) and the minus spans the same width at y=34, each 8+ from the
walls and 10 from each other.
Omission: the reference's horizontal divider; with the plus and minus it needs
two 16-tall bands, more than the body holds.
Revision (reviewer: "make the battery taller and narrower, with smaller corner
curves. Make the top terminal wider and shallower"): VRECT_L 32 wide -> VRECT_M 28
wide and 36 tall, corners r6/r4 -> r3, terminal 8x6 -> 16x4.
Lucide construction: 'battery' - rounded body and terminal; plus/minus as in
'battery-plus'.
Keyshape VRECT_M: centerline x 10..38, y 4 (terminal) .. 44 (base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8d87115c-6db3-51bc-bed2-f5fd070b0c3d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__battery-2/20260926T061914Z-thuan-mac/reference/battery 2_8d87115c-6db3-51bc-bed2-f5fd070b0c3d.svg"
AUTHOR = "claude-opus-5-5"


class Battery2(Solo48):
    icon_id = "battery-2"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/power"
    aliases = ("battery", "battery-cell")
    keywords = ("battery", "power", "energy", "charge", "plus", "minus", "cell")

    def build(self) -> None:
        left, right, top, bottom, r = 10, 38, 8, 44, 3
        t_left, t_right, t_top = 16, 32, 4
        top_run = ((left + r, top), (t_left, top), (t_left, t_top), (t_right, t_top), (t_right, top),
                   (right - r, top))
        members = []
        for i, (p, q) in enumerate(zip(top_run, top_run[1:]), 1):
            self.add_line(f"top-edge-{i}", p, q)
            members.append(f"top-edge-{i}")
        self.add_arc("corner-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("right", (right, top + r), (right, bottom - r))
        self.add_arc("corner-br", (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line("base", (right - r, bottom), (left + r, bottom))
        self.add_arc("corner-bl", (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line("left", (left, bottom - r), (left, top + r))
        self.add_arc("corner-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_contour("battery", *members, "corner-tr", "right", "corner-br", "base",
                         "corner-bl", "left", "corner-tl", closed=True)
        self.add_polyline("plus-h", (20, 20), (24, 20), (28, 20))
        self.add_polyline("plus-v", (24, 16), (24, 20), (24, 24))
        self.relate("connect", "plus-h", "plus-v")
        self.add_line("minus", (20, 34), (28, 34))
