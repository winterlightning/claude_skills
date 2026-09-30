"""A soap bottle enclosure with a raised neck and a left-facing pump.

Keyshape VRECT_M: centerline extremes recorded in build below.
Lucide soap-dispenser-droplet informs the connected stem and curved spout. Both supplied bottles map here; the disconnected reference stem is restored. The spout is intentionally asymmetric.
Hosting (compose.py): plus invalid, heart invalid, check invalid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (liquid-soap-dispenser-bottle VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class LiquidSoapDispenserBottle(Container64):
    icon_id = 'liquid-soap-dispenser-bottle'
    keyshape = Keyshape.VRECT_M
    aliases = ('soap-pump',)
    keywords = ('liquid', 'soap', 'dispenser', 'bottle')

    def build(self) -> None:
        self.add_line('neck-top-left', (27, 14), (32, 14))
        self.add_line('neck-top-right', (32, 14), (37, 14))
        self.add_line('neck-slope-right', (37, 14), (40, 22))
        self.add_line('shoulder-right', (40, 22), (47, 22))
        self.add_arc('ne', (47, 22), (52, 28), radius_x=5, radius_y=6)
        self.add_line('right', (52, 28), (52, 54))
        self.add_arc('se', (52, 54), (47, 60), radius_x=5, radius_y=6)
        self.add_line('bottom', (47, 60), (17, 60))
        self.add_arc('sw', (17, 60), (12, 54), radius_x=5, radius_y=6)
        self.add_line('left', (12, 54), (12, 28))
        self.add_arc('nw', (12, 28), (17, 22), radius_x=5, radius_y=6)
        self.add_line('shoulder-left', (17, 22), (24, 22))
        self.add_line('neck-slope-left', (24, 22), (27, 14))
        self.add_line('stem', (32, 14), (32, 4))
        self.add_line('pump-right', (39, 4), (32, 4))
        self.add_line('pump-left', (32, 4), (25, 4))
        self.add_arc('spout', (25, 4), (19, 10), radius_x=6, sweep=False)
        self.add_contour('bottle', 'neck-top-left', 'neck-top-right', 'neck-slope-right', 'shoulder-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'shoulder-left', 'neck-slope-left', closed=True)
        self.add_contour('pump', 'pump-right', 'pump-left', 'spout')
        self.relate('connect', 'bottle', 'stem')
        self.relate('connect', 'stem', 'pump')
