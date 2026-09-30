"""Widen and deepen the tank body; shorten the valve neck and base.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (propane-gas-cylinder-tank VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class PropaneGasCylinderTank(Container64):
    icon_id = 'propane-gas-cylinder-tank'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('tank-0', (18, 12), (46, 12))
        self.add_arc('tank-1', (46, 12), (54, 20), radius_x=8)
        self.add_line('tank-2', (54, 20), (54, 44))
        self.add_arc('tank-3', (54, 44), (46, 52), radius_x=8)
        self.add_line('tank-4', (46, 52), (18, 52))
        self.add_arc('tank-5', (18, 52), (10, 44), radius_x=8)
        self.add_line('tank-6', (10, 44), (10, 20))
        self.add_arc('tank-7', (10, 20), (18, 12), radius_x=8)
        self.add_line('cap', (22, 4), (42, 4))
        self.add_line('neck-24', (28, 4), (28, 12))
        self.add_line('neck-40', (36, 4), (36, 12))
        self.add_line('foot-0', (22, 52), (14, 60))
        self.add_line('foot-1', (14, 60), (50, 60))
        self.add_line('foot-2', (50, 60), (42, 52))
        self.add_contour('tank', 'tank-0', 'tank-1', 'tank-2', 'tank-3', 'tank-4', 'tank-5', 'tank-6', 'tank-7', closed=True)
        self.add_contour('foot', 'foot-0', 'foot-1', 'foot-2')
        self.relate('connect', 'cap', 'neck-24')
        self.relate('connect', 'tank', 'neck-24')
        self.relate('connect', 'cap', 'neck-40')
        self.relate('connect', 'tank', 'neck-40')
        self.relate('connect', 'tank', 'foot')
