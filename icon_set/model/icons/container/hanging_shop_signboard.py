"""Taller hanging sign with a shorter suspension and unchanged support.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hanging-shop-signboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn as a wide hanging sign (HRECT_L) so 4-letter words fit (container-combination64).
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class HangingShopSignboard(Container64):
    icon_id = 'hanging-shop-signboard'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # HRECT_L (was SQUARE): a wide real-estate sign. The panel 4..52 x 18..54 (radius 4) hangs on two short
        # hangers from the arm at 10, which turns down into the post at x 60, kept 8 from the panel. The panel
        # holds a 4-letter word (SOLD, RENT, SALE) at scale ~0.64 and a symbol of 24; its centre is (28, 36).
        self.add_line('panel-0', (8, 18), (48, 18))
        self.add_arc('panel-1', (48, 18), (52, 22), radius_x=4)
        self.add_line('panel-2', (52, 22), (52, 50))
        self.add_arc('panel-3', (52, 50), (48, 54), radius_x=4)
        self.add_line('panel-4', (48, 54), (8, 54))
        self.add_arc('panel-5', (8, 54), (4, 50), radius_x=4)
        self.add_line('panel-6', (4, 50), (4, 22))
        self.add_arc('panel-7', (4, 22), (8, 18), radius_x=4)
        self.add_line('support-0', (10, 10), (54, 10))
        self.add_arc('support-1', (54, 10), (60, 16), radius_x=6)
        self.add_line('support-2', (60, 16), (60, 54))
        self.add_line('hanger-14', (14, 10), (14, 18))
        self.add_line('hanger-42', (42, 10), (42, 18))
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_contour('support', 'support-0', 'support-1', 'support-2')
        self.relate('connect', 'support', 'hanger-14')
        self.relate('connect', 'panel', 'hanger-14')
        self.relate('connect', 'support', 'hanger-42')
        self.relate('connect', 'panel', 'hanger-42')
