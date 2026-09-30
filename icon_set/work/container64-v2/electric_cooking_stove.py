"""A tapered electric stove with a control band and inset base.

SQUARE: exact centerline extremes recorded in build.
Construction: Lucide smartphone, repeated rounded enclosure corners; tapered appliance silhouette comes from the supplied source. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (electric-cooking-stove SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class ElectricCookingStove(Container64):
    icon_id = 'electric-cooking-stove'
    keyshape = Keyshape.SQUARE
    aliases = ('modern-electric-cooking-stove',)
    keywords = ('electric', 'cooking', 'stove')

    def build(self) -> None:
        self.add_line('top', (18, 6), (46, 6))
        self.add_arc('ne', (46, 6), (52, 12), radius_x=6)
        self.add_line('taper-right', (52, 12), (58, 35))
        self.add_line('side-right', (58, 35), (58, 44))
        self.add_arc('se', (58, 44), (52, 50), radius_x=6)
        self.add_line('bottom', (52, 50), (12, 50))
        self.add_arc('sw', (12, 50), (6, 44), radius_x=6)
        self.add_line('side-left', (6, 44), (6, 35))
        self.add_line('taper-left', (6, 35), (12, 12))
        self.add_arc('nw', (12, 12), (18, 6), radius_x=6)
        self.add_line('divider', (6, 35), (58, 35))
        self.add_line('base-1', (12, 50), (16, 58))
        self.add_line('base-2', (16, 58), (48, 58))
        self.add_line('base-3', (48, 58), (52, 50))
        self.add_line('control-left', (24, 41), (24, 43))
        self.add_line('control-right', (40, 41), (40, 43))
        self.add_contour('outline', 'top', 'ne', 'taper-right', 'side-right', 'se', 'bottom', 'sw', 'side-left', 'taper-left', 'nw', closed=True)
        self.add_contour('base', 'base-1', 'base-2', 'base-3')
        self.relate('connect', 'divider', 'outline')
        self.relate('connect', 'base', 'outline')
