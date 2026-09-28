"""Bartender: a bartender's portrait bust - round head over curved shoulders, with a
bow tie centred on the chest.

Symbol plan: mirror symmetry about x=24. Portrait-bust construction (shared human
reference): the head is a radius-9 circle about (24,13) (user.svg proportions); the
shoulders are a radius-20 arc about (24,46) whose crest (24,26) sits exactly 4 below
the head's lowest point, so the two inks touch, then short vertical sides to the
open bottom. The bow tie is two tangent radius-3 rings (the approved 6-diameter
circle) meeting at the knot (24,40), 10 inside the shoulder line.
Revision (reviewer: "Replace the triangular shape with a centered bow tie inside the
curve half body"): the stick figure holding a triangular glass is replaced by the
reference's half-body bust with a centred bow tie.
Omission: the reference's ears and beard; bow-tie wings are round loops, since
triangular wings in the 8-unit chest band cannot keep open holes.
Lucide construction: 'user' bust; human reference icon_set/references/human_ref/user.svg.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (head) .. 44 (open bottom).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bartainder/20260926T073832Z-thuan-mac/reference/bartainder_f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea.svg"
AUTHOR = "claude-opus-5-5"


class Bartender(Solo48):
    icon_id = "bartainder-solo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/professions"
    human_construction = "bust"
    aliases = ("bartender", "waiter", "butler")
    keywords = ("bartender", "bow-tie", "waiter", "bar", "server", "profession", "person")

    def build(self) -> None:
        hx, hy, hr = 24, 13, 9
        self.add_arc("head-left", (hx, hy + hr), (hx, hy - hr), radius_x=hr, sweep=True)
        self.add_arc("head-right", (hx, hy - hr), (hx, hy + hr), radius_x=hr, sweep=True)
        self.add_contour("head", "head-left", "head-right", closed=True)
        self.add_line("side-left", (8, 44), (8, 34))
        self.add_arc("shoulder-left", (8, 34), (24, 26), radius_x=20, sweep=True)
        self.add_arc("shoulder-right", (24, 26), (40, 34), radius_x=20, sweep=True)
        self.add_line("side-right", (40, 34), (40, 44))
        self.add_contour("body", "side-left", "shoulder-left", "shoulder-right", "side-right")
        self.relate("connect", "head", "body")
        for name, cx, first in (("tie-left", 21, (24, 40)), ("tie-right", 27, (24, 40))):
            other = (2 * cx - 24, 40)
            self.add_arc(f"{name}-a", first, other, radius_x=3, sweep=True)
            self.add_arc(f"{name}-b", other, first, radius_x=3, sweep=True)
            self.add_contour(name, f"{name}-a", f"{name}-b", closed=True)
        self.relate("connect", "tie-left", "tie-right")
