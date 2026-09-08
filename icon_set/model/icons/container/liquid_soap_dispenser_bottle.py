"""A soap bottle enclosure with a raised neck and a left-facing pump.

Keyshape VRECT_M: centerline extremes recorded in build below.
Lucide soap-dispenser-droplet informs the connected stem and curved spout. Both supplied bottles map here; the disconnected reference stem is restored. The spout is intentionally asymmetric.
Hosting (compose.py): plus invalid, heart invalid, check invalid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class LiquidSoapDispenserBottle(Container64):
    icon_id = 'liquid-soap-dispenser-bottle'
    keyshape = Keyshape.VRECT_M
    aliases = ('soap-pump',)
    keywords = ('liquid', 'soap', 'dispenser', 'bottle')

    def build(self) -> None:
        # VRECT_M centerline extremes: (14,2)-(50,62).
        self.add_line("neck-top-left", (26,12), (32,12))
        self.add_line("neck-top-right", (32,12), (38,12))
        self.add_line("neck-slope-right", (38,12), (41,20))
        self.add_line("shoulder-right", (41,20), (44,20))
        self.add_arc("ne", (44,20), (50,26), radius_x=6)
        self.add_line("right", (50,26), (50,56))
        self.add_arc("se", (50,56), (44,62), radius_x=6)
        self.add_line("bottom", (44,62), (20,62))
        self.add_arc("sw", (20,62), (14,56), radius_x=6)
        self.add_line("left", (14,56), (14,26))
        self.add_arc("nw", (14,26), (20,20), radius_x=6)
        self.add_line("shoulder-left", (20,20), (23,20))
        self.add_line("neck-slope-left", (23,20), (26,12))
        self.add_contour("bottle", "neck-top-left", "neck-top-right", "neck-slope-right", "shoulder-right", "ne", "right", "se", "bottom", "sw", "left", "nw", "shoulder-left", "neck-slope-left", closed=True)
        self.add_line("stem", (32,12), (32,2))
        self.add_line("pump-right", (40,2), (32,2))
        self.add_line("pump-left", (32,2), (24,2))
        self.add_arc("spout", (24,2), (18,8), radius_x=6, sweep=False)
        self.add_contour("pump", "pump-right", "pump-left", "spout")
        self.relate("connect", "bottle", "stem")
        self.relate("connect", "stem", "pump")
