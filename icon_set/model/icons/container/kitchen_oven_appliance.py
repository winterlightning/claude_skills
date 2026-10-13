"""A kitchen oven with three solid control dots above its large door.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide smartphone informs quarter-circle enclosure corners. The source render supplies the three controls and shared door divider; no extra inset window is added.
Hosting measured with compose.py: plus invalid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (kitchen-oven-appliance SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class KitchenOvenAppliance(Container64):
    icon_id = 'kitchen-oven-appliance'
    keyshape = Keyshape.SQUARE
    aliases = ('oven',)
    keywords = ('kitchen', 'oven', 'appliance')

    def build(self) -> None:
        self.add_line('top', (10, 6), (54, 6))
        self.add_arc('nw', (6, 10), (10, 6), radius_x=4)
        self.add_line('left-header', (6, 26), (6, 10))
        self.add_arc('ne', (54, 6), (58, 10), radius_x=4)
        self.add_line('right-header', (58, 10), (58, 26))
        self.add_line('divider', (6, 26), (58, 26))
        self.add_line('right-door', (58, 26), (58, 54))
        self.add_arc('se', (58, 54), (54, 58), radius_x=4)
        self.add_line('bottom', (54, 58), (10, 58))
        self.add_arc('sw', (10, 58), (6, 54), radius_x=4)
        self.add_line('left-door', (6, 54), (6, 26))
        self.add_dot('knob-18', (20, 17))
        self.add_dot('knob-32', (32, 17))
        self.add_dot('knob-46', (44, 17))
        self.add_contour('header-left', 'left-header', 'nw')
        self.add_contour('header-right', 'ne', 'right-header')
        self.add_contour('door', 'right-door', 'se', 'bottom', 'sw', 'left-door')
        self.relate('connect', 'top', 'header-left')
        self.relate('connect', 'top', 'header-right')
        self.relate('connect', 'divider', 'header-left')
        self.relate('connect', 'divider', 'header-right')
        self.relate('connect', 'divider', 'door')
        self.relate('connect', 'door', 'header-left')
        self.relate('connect', 'door', 'header-right')
