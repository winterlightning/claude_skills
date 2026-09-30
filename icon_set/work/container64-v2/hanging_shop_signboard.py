"""Taller hanging sign with a shorter suspension and unchanged support.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hanging-shop-signboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class HangingShopSignboard(Container64):
    icon_id = 'hanging-shop-signboard'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('panel-0', (9, 20), (45, 20))
        self.add_arc('panel-1', (45, 20), (48, 23), radius_x=3)
        self.add_line('panel-2', (48, 23), (48, 53))
        self.add_arc('panel-3', (48, 53), (45, 56), radius_x=3)
        self.add_line('panel-4', (45, 56), (9, 56))
        self.add_arc('panel-5', (9, 56), (6, 53), radius_x=3)
        self.add_line('panel-6', (6, 53), (6, 23))
        self.add_arc('panel-7', (6, 23), (9, 20), radius_x=3)
        self.add_line('support-0', (6, 6), (52, 6))
        self.add_arc('support-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('support-2', (58, 12), (58, 58))
        self.add_line('hanger-12', (16, 6), (16, 20))
        self.add_line('hanger-44', (40, 6), (40, 20))
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_contour('support', 'support-0', 'support-1', 'support-2')
        self.relate('connect', 'support', 'hanger-12')
        self.relate('connect', 'panel', 'hanger-12')
        self.relate('connect', 'support', 'hanger-44')
        self.relate('connect', 'panel', 'hanger-44')
