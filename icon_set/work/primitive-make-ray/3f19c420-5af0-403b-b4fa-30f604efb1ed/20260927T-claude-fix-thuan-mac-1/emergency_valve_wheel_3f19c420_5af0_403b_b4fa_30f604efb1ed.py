"""Emergency valve wheel: a toothed valve handwheel -- a cogged outer rim, a
central hub and spokes joining them.

Revision (disapproved, reason not recorded): the rejected drawing was a plain
round rim crossed by four spokes, which reads as a steering wheel or crosshair;
the original's rim is cogged with eight teeth round a spoked wheel. The toothed
rim is restored around the hub and spokes.

Symbol plan: 8-fold symmetry about (24,24). Rim: one closed polyline of eight
teeth centred between the axes (22.5 + 45k degrees): tooth tips at radius 19
spanning +-6 degrees, tooth roots at radius 16 spanning +-11 degrees, so the root
flats straddle the four axes; every corner is rounded to the grid, which keeps
the rim's axis and diagonal mirror symmetry. Hub: radius-5 ring. Spokes: four
axis strokes from the hub (29,24)... to the rim's root flats (40,24)...
Omissions: the separate inner wheel ring and the other two spokes (they would cut
the rim into sectors below the hole minimum).
Lucide construction: 'settings' cog teeth; 'ship-wheel' spokes.
Keyshape SQUARE: centerline (6,6)-(42,42).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f19c420-5af0-403b-b4fa-30f604efb1ed"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__emergency-valve-wheel/20260926T182653Z-thuan-mac-1/reference/emergency valve_3f19c420-5af0-403b-b4fa-30f604efb1ed.svg"
AUTHOR = "claude-opus-5-5"

C, TIP_R, ROOT_R, HUB_R = 24, 19, 16, 5


def rim_points():
    """Eight teeth centred on 22.5 + 45k degrees; every corner rounded to the grid.
    Rounding is symmetric under the axis and diagonal mirrors, so the rim keeps
    its 8-fold symmetry. Root flats straddle the axes, where the spokes land."""
    out = []
    for k in range(8):
        phi = 22.5 + 45 * k
        for ang, r in ((phi - 11, ROOT_R), (phi - 6, TIP_R), (phi + 6, TIP_R), (phi + 11, ROOT_R)):
            a = math.radians(ang)
            out.append((C + round(r * math.cos(a)), C + round(r * math.sin(a))))
    # Split the root flats at the axis points so the spokes can land on nodes.
    full = []
    for i, p in enumerate(out):
        full.append(p)
        if i % 4 == 3:
            k = i // 4
            ang = math.radians(45 * (k + 1))
            full.append((C + round(ROOT_R * math.cos(ang)), C + round(ROOT_R * math.sin(ang)))) if (k + 1) % 2 == 0 else None
    return full


class EmergencyValveWheel(Solo48):
    icon_id = "emergency-valve-wheel"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "safety/industrial"
    aliases = ("valve-handwheel", "emergency-valve")
    keywords = ("valve", "wheel", "handwheel", "emergency", "shutoff", "pipe", "industrial")

    def build(self) -> None:
        self.add_polyline("rim", *rim_points(), closed=True)
        self.add_arc("hub-a", (C - HUB_R, C), (C, C - HUB_R), radius_x=HUB_R)
        self.add_arc("hub-b", (C, C - HUB_R), (C + HUB_R, C), radius_x=HUB_R)
        self.add_arc("hub-c", (C + HUB_R, C), (C, C + HUB_R), radius_x=HUB_R)
        self.add_arc("hub-d", (C, C + HUB_R), (C - HUB_R, C), radius_x=HUB_R)
        self.add_contour("hub", "hub-a", "hub-b", "hub-c", "hub-d", closed=True)
        for i, (dx, dy) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1))):
            self.add_line(f"spoke-{i}", (C + HUB_R * dx, C + HUB_R * dy), (C + ROOT_R * dx, C + ROOT_R * dy))
            self.relate("connect", f"spoke-{i}", "hub")
            self.relate("connect", f"spoke-{i}", "rim")
