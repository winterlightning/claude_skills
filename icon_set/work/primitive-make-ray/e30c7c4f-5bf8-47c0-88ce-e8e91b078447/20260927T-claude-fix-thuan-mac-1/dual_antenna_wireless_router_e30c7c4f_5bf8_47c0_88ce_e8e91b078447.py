"""Dual antenna wireless router: a flat router box on two little feet with two
upright antennae, each broadcasting a signal arc above its tip.

Revision (disapproved, reason not recorded): the rejected drawing floated two
small horseshoe loops well away from short antennae, so the signal read as a pair
of magnets; in the original each antenna carries shallow broadcast arcs that
fan out above its tip. The arcs are now shallow broadcast arcs centred on each
antenna tip.

Symbol plan: mirror axis x=24. Body: rounded rectangle (4,26)-(44,36), radius-4
corners; feet (10,36)-(10,40) and (38,36)-(38,40). Antennae: x=13 and x=35 from
the body top up to their tips at y=18. Signal: one radius-10 arc about each tip,
from its 6-8-10 points (tip -6,-8) to (tip +6,-8) over the crest y=8, 10 clear of
the tip; the two arcs are 10 apart.
Omissions: the inner and outer signal arcs of each set (a second concentric arc
needs 8 more on each side; two sets would overlap in the 40-unit width).
Lucide construction: 'router' body and antennae; 'wifi' arcs.
Keyshape HRECT_L: centerline x 4..44 (body), y 8 (arcs) .. 40 (feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e30c7c4f-5bf8-47c0-88ce-e8e91b078447"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dual-antenna-wireless-router/20260926T182653Z-thuan-mac-1/reference/router signal double_e30c7c4f-5bf8-47c0-88ce-e8e91b078447.svg"
AUTHOR = "claude-opus-5-5"

TOP, BOTTOM, L, R_, CR = 26, 36, 4, 44, 4
ANTENNAE, TIP_Y = (13, 35), 18


class DualAntennaWirelessRouter(Solo48):
    icon_id = "dual-antenna-wireless-router"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/network"
    aliases = ("wifi-router", "router-signal")
    keywords = ("router", "wifi", "wireless", "antenna", "signal", "network", "internet")

    def build(self) -> None:
        a1, a2 = ANTENNAE
        self.add_line("top-a", (L + CR, TOP), (a1, TOP))
        self.add_line("top-b", (a1, TOP), (a2, TOP))
        self.add_line("top-c", (a2, TOP), (R_ - CR, TOP))
        self.add_arc("tr", (R_ - CR, TOP), (R_, TOP + CR), radius_x=CR)
        self.add_line("right", (R_, TOP + CR), (R_, BOTTOM - CR))
        self.add_arc("br", (R_, BOTTOM - CR), (R_ - CR, BOTTOM), radius_x=CR)
        self.add_line("bottom-a", (R_ - CR, BOTTOM), (38, BOTTOM))
        self.add_line("bottom-b", (38, BOTTOM), (10, BOTTOM))
        self.add_line("bottom-c", (10, BOTTOM), (L + CR, BOTTOM))
        self.add_arc("bl", (L + CR, BOTTOM), (L, BOTTOM - CR), radius_x=CR)
        self.add_line("left", (L, BOTTOM - CR), (L, TOP + CR))
        self.add_arc("tl", (L, TOP + CR), (L + CR, TOP), radius_x=CR)
        self.add_contour("body", "top-a", "top-b", "top-c", "tr", "right", "br", "bottom-a", "bottom-b",
                         "bottom-c", "bl", "left", "tl", closed=True)
        for i, x in enumerate((10, 38)):
            self.add_line(f"foot-{i}", (x, BOTTOM), (x, 40))
            self.relate("connect", "body", f"foot-{i}")
        for i, x in enumerate(ANTENNAE):
            self.add_line(f"antenna-{i}", (x, TOP), (x, TIP_Y))
            self.relate("connect", "body", f"antenna-{i}")
            self.add_arc(f"signal-{i}", (x - 6, TIP_Y - 8), (x + 6, TIP_Y - 8), radius_x=10)
