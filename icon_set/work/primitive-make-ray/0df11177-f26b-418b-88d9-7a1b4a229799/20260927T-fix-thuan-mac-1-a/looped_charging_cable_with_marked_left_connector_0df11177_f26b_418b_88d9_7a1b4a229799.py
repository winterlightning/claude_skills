"""Thunderbolt cable: looped charging cable with a marked left connector.

Symbol plan (HRECT_L): left connector = rounded body (4..20 x 8..26, r3)
carrying a short centred mark (the reference's bolt, reduced: a 16-wide body
leaves only its centre line 8 from both walls) above a narrower neck
(8..16 x 26..32). The cable leaves the neck at (12,32), turns through an r8
U (bottom y=40), rises at x=28 (8 from the left body and from the right
plug), arches over with r6 and drops at x=40 into the right plug: an 8x8
body (36..44 x 24..32) with a centre pin down to y=40.
Revision: the rejected drawing dropped the left connector's mark and neck
and the right plug's pin, so neither end read as a connector.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0df11177-f26b-418b-88d9-7a1b4a229799"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__looped-charging-cable-with-marked-left-connector/20260927T153253Z-thuan-mac-1/reference/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg"
AUTHOR = "claude-opus-5-5"


class LoopedChargingCable(Solo48):
    icon_id = "looped-charging-cable-with-marked-left-connector"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    categories = ("primitives", "devices")
    aliases = ("thunderbolt cable", "charging cable")
    keywords = ("cable", "thunderbolt", "usb", "charger", "connector", "plug")

    def build(self) -> None:
        l, t, r, b, q = 4, 8, 20, 26, 3
        self.add_line("body-top", (l + q, t), (r - q, t))
        self.add_arc("body-tr", (r - q, t), (r, t + q), radius_x=q)
        self.add_line("body-right", (r, t + q), (r, b))
        self.add_line("body-bottom-right", (r, b), (16, b))
        self.add_line("body-bottom-mid", (16, b), (8, b))
        self.add_line("body-bottom-left", (8, b), (l, b))
        self.add_line("body-left", (l, b), (l, t + q))
        self.add_arc("body-tl", (l, t + q), (l + q, t), radius_x=q)
        self.add_contour("body", "body-top", "body-tr", "body-right", "body-bottom-right",
                         "body-bottom-mid", "body-bottom-left", "body-left", "body-tl", closed=True)
        self.add_line("mark", (12, 16), (12, 18))
        self.add_polyline("neck", (8, b), (8, 32), (12, 32), (16, 32), (16, b))
        self.relate("connect", "body", "neck")

        self.add_arc("cable-u", (12, 32), (28, 32), radius_x=8, sweep=False)
        self.add_line("cable-rise", (28, 32), (28, 16))
        self.add_arc("cable-arch", (28, 16), (40, 16), radius_x=6, sweep=True)
        self.add_line("cable-drop", (40, 16), (40, 24))
        self.add_contour("cable", "cable-u", "cable-rise", "cable-arch", "cable-drop")
        self.relate("connect", "neck", "cable")

        self.add_line("plug-top-left", (36, 24), (40, 24))
        self.add_line("plug-top-right", (40, 24), (44, 24))
        self.add_line("plug-right", (44, 24), (44, 32))
        self.add_line("plug-bottom-right", (44, 32), (40, 32))
        self.add_line("plug-bottom-left", (40, 32), (36, 32))
        self.add_line("plug-left", (36, 32), (36, 24))
        self.add_contour("plug", "plug-top-left", "plug-top-right", "plug-right",
                         "plug-bottom-right", "plug-bottom-left", "plug-left", closed=True)
        self.add_line("pin", (40, 32), (40, 40))
        self.relate("connect", "plug", "cable")
        self.relate("connect", "plug", "pin")
