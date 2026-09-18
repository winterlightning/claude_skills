"""A soap bottle enclosure with a raised neck and a left-facing pump.

Keyshape VRECT_M: centerline extremes recorded in build below.
Lucide soap-dispenser-droplet informs the connected stem and curved spout. Both supplied bottles map here; the disconnected reference stem is restored. The spout is intentionally asymmetric.
Hosting (compose.py): plus invalid, heart invalid, check invalid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class LiquidSoapDispenserBottleVariant3(Container64):
    icon_id = 'liquid-soap-dispenser-bottle-v3'
    variant_of = 'liquid-soap-dispenser-bottle'
    variant_label = 'Modest four-unit expansion'
    keyshape = Keyshape.VRECT_L
    aliases = ('soap-pump',)
    keywords = ('liquid', 'soap', 'dispenser', 'bottle')

    def build(self) -> None:
        self.add_line('neck-top-left', (26, 12), (32, 12))
        self.add_line('neck-top-right', (32, 12), (38, 12))
        self.add_line('neck-slope-right', (38, 12), (41, 20))
        self.add_line('shoulder-right', (41, 20), (48, 20))
        self.add_arc('ne', (48, 20), (54, 26), radius_x=6)
        self.add_line('right', (54, 26), (54, 56))
        self.add_arc('se', (54, 56), (48, 62), radius_x=6)
        self.add_line('bottom', (48, 62), (16, 62))
        self.add_arc('sw', (16, 62), (10, 56), radius_x=6)
        self.add_line('left', (10, 56), (10, 26))
        self.add_arc('nw', (10, 26), (16, 20), radius_x=6)
        self.add_line('shoulder-left', (16, 20), (23, 20))
        self.add_line('neck-slope-left', (23, 20), (26, 12))
        self.add_contour('bottle', 'neck-top-left', 'neck-top-right', 'neck-slope-right', 'shoulder-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'shoulder-left', 'neck-slope-left', closed=True)
        self.add_line('stem', (32, 12), (32, 2))
        self.add_line('pump-right', (40, 2), (32, 2))
        self.add_line('pump-left', (32, 2), (24, 2))
        self.add_arc('spout', (24, 2), (18, 8), radius_x=6, sweep=False)
        self.add_contour('pump', 'pump-right', 'pump-left', 'spout')
        self.relate('connect', 'bottle', 'stem')
        self.relate('connect', 'stem', 'pump')
