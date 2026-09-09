# Variant of kitchen-oven-appliance; parent file remains unchanged.
"""A kitchen oven with three solid control dots above its large door.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide smartphone informs quarter-circle enclosure corners. The source render supplies the three controls and shared door divider; no extra inset window is added.
Hosting measured with compose.py: plus invalid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class KitchenOvenApplianceVariant2(Container64):
    icon_id = 'kitchen-oven-appliance-v2'
    variant_of = 'kitchen-oven-appliance'
    variant_label = 'Solid control dots'
    keyshape = Keyshape.SQUARE
    aliases = ('oven',)
    keywords = ('kitchen', 'oven', 'appliance')

    def build(self) -> None:
        self.add_line('top', (6, 2), (58, 2))
        self.add_arc('nw', (2, 6), (6, 2), radius_x=4)
        self.add_line('left-header', (2, 24), (2, 6))
        self.add_contour('header-left', 'left-header', 'nw')
        self.add_arc('ne', (58, 2), (62, 6), radius_x=4)
        self.add_line('right-header', (62, 6), (62, 24))
        self.add_contour('header-right', 'ne', 'right-header')
        self.add_line('divider', (2, 24), (62, 24))
        self.add_line('right-door', (62, 24), (62, 58))
        self.add_arc('se', (62, 58), (58, 62), radius_x=4)
        self.add_line('bottom', (58, 62), (6, 62))
        self.add_arc('sw', (6, 62), (2, 58), radius_x=4)
        self.add_line('left-door', (2, 58), (2, 24))
        self.add_contour('door', 'right-door', 'se', 'bottom', 'sw', 'left-door')
        for a, b in (('top', 'header-left'), ('top', 'header-right'), ('divider', 'header-left'), ('divider', 'header-right'), ('divider', 'door'), ('door', 'header-left'), ('door', 'header-right')):
            self.relate('connect', a, b)
        for x in (18, 32, 46):
            self.add_dot(f'knob-{x}', (x, 13))
