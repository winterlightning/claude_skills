"""Drill on support arm: a pistol drill facing right (rounded rear, motor, chuck with a
round nose, bit) whose slanted grip is held at its base by an L-shaped robot arm.

Symbol plan: one closed body outline. Top y=6 from the rounded rear (r6 corner at
(6,6)) to the chuck nose, a semicircle r6 about (30,12); the underside y=18 returns
to the grip. The grip slants back at 1:3: front edge (16,18)-(19,27), back edge
(9,27)-(6,18), 9.5 apart; its base is two cubics meeting at the low point (14,32),
tangent to both edges. A vertical divider at x=24 separates motor and chuck. The
bit runs from the nose tip to the right edge. The support arm leaves the grip base
straight down and turns right along the bottom edge.
Deliberate asymmetry: a directional tool.
Revision: the rejected drawing bent the grip into a zigzag and hung the arm off a
corner; this follows the reference's pistol grip, chuck split and L arm.
Lucide construction: 'drill' - rounded motor body, nose chuck, projecting bit and a
slanted grip.
Keyshape SQUARE: centerline x 6 (rear) .. 42 (bit tip), y 6 (top) .. 42 (arm foot).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "36473314-e81e-4c52-8234-73a3b29780e7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__drill-on-support-arm/20260926T055144Z-thuan-mac/reference/drill robot arm_36473314-e81e-4c52-8234-73a3b29780e7.svg"
AUTHOR = "claude-opus-5-5"


class DrillOnSupportArm(Solo48):
    icon_id = "drill-on-support-arm"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    aliases = ("drill-robot-arm", "robotic-drill")
    keywords = ("drill", "robot-arm", "power-tool", "industrial", "machine", "automation", "tool")

    def build(self) -> None:
        top, under = 6, 18
        self.add_arc("rear-corner", (6, 12), (12, top), radius_x=6, sweep=True)
        self.add_line("top-motor", (12, top), (24, top))
        self.add_line("top-chuck", (24, top), (30, top))
        self.add_arc("nose-upper", (30, top), (36, 12), radius_x=6, sweep=True)
        self.add_arc("nose-lower", (36, 12), (30, under), radius_x=6, sweep=True)
        self.add_line("under-chuck", (30, under), (24, under))
        self.add_line("under-motor", (24, under), (16, under))
        self.add_line("grip-front", (16, under), (19, 27))
        self.add_bezier("grip-base", (19, 27),
                        ((20, 30), (16, 32), (14, 32)),
                        ((12, 32), (10, 30), (9, 27)))
        self.add_line("grip-back", (9, 27), (6, under))
        self.add_line("rear", (6, under), (6, 12))
        self.add_contour("body", "rear-corner", "top-motor", "top-chuck", "nose-upper",
                         "nose-lower", "under-chuck", "under-motor", "grip-front",
                         "grip-base", "grip-back", "rear", closed=True)
        self.add_line("chuck-divider", (24, top), (24, under))
        self.relate("connect", "body", "chuck-divider")
        self.add_line("bit", (36, 12), (42, 12))
        self.relate("connect", "body", "bit")
        self.add_polyline("arm", (14, 32), (14, 42), (26, 42))
        self.relate("connect", "body", "arm")
