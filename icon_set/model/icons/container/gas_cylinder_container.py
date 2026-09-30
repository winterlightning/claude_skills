"""A squat gas vessel with rounded shoulders and a capped neck.

VRECT_L: visible (8, 0, 56, 64); centerline (10, 2)-(54, 62).
Reference: batch_05 source render. Lucide smartphone quarter-circle corners inform the smooth vessel shell..
Source bottom chamfers simplified to matching quarter-circle corners.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (gas-cylinder-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class GasCylinderContainer(Container64):
    icon_id = 'gas-cylinder-container'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('gas', 'cylinder', 'container')

    def build(self) -> None:
        self.add_line('tank-0', (22, 19), (42, 19))
        self.add_arc('tank-1', (42, 19), (52, 28), radius_x=10, radius_y=9)
        self.add_line('tank-2', (52, 28), (52, 51))
        self.add_arc('tank-3', (52, 51), (42, 60), radius_x=10, radius_y=9)
        self.add_line('tank-4', (42, 60), (22, 60))
        self.add_arc('tank-5', (22, 60), (12, 51), radius_x=10, radius_y=9)
        self.add_line('tank-6', (12, 51), (12, 28))
        self.add_arc('tank-7', (12, 28), (22, 19), radius_x=10, radius_y=9)
        self.add_line('neck-left', (26, 4), (26, 19))
        self.add_line('neck-right', (38, 4), (38, 19))
        self.add_line('cap', (20, 4), (44, 4))
        self.add_contour('tank', 'tank-0', 'tank-1', 'tank-2', 'tank-3', 'tank-4', 'tank-5', 'tank-6', 'tank-7', closed=True)
        self.relate('connect', 'neck-left', 'tank')
        self.relate('connect', 'neck-right', 'tank')
        self.relate('connect', 'cap', 'neck-left')
        self.relate('connect', 'cap', 'neck-right')
