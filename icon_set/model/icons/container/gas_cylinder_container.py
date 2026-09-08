"""A squat gas vessel with rounded shoulders and a capped neck.

VRECT_L: visible (8, 0, 56, 64); centerline (10, 2)-(54, 62).
Reference: batch_05 source render. Lucide smartphone quarter-circle corners inform the smooth vessel shell..
Source bottom chamfers simplified to matching quarter-circle corners.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class GasCylinderContainer(Container64):
    icon_id = "gas-cylinder-container"
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('gas', 'cylinder', 'container')

    def build(self) -> None:
        self.add_line('tank-0', (20, 18), (44, 18))
        self.add_arc('tank-1', (44, 18), (54, 28), radius_x=10, sweep=True)
        self.add_line('tank-2', (54, 28), (54, 52))
        self.add_arc('tank-3', (54, 52), (44, 62), radius_x=10, sweep=True)
        self.add_line('tank-4', (44, 62), (20, 62))
        self.add_arc('tank-5', (20, 62), (10, 52), radius_x=10, sweep=True)
        self.add_line('tank-6', (10, 52), (10, 28))
        self.add_arc('tank-7', (10, 28), (20, 18), radius_x=10, sweep=True)
        self.add_contour('tank', 'tank-0', 'tank-1', 'tank-2', 'tank-3', 'tank-4', 'tank-5', 'tank-6', 'tank-7', closed=True)
        self.add_line('neck-left', (24, 2), (24, 18))
        self.add_line('neck-right', (40, 2), (40, 18))
        self.add_line('cap', (18, 2), (46, 2))
        self.relate("connect", 'neck-left', 'tank')
        self.relate("connect", 'neck-right', 'tank')
        self.relate("connect", 'cap', 'neck-left')
        self.relate("connect", 'cap', 'neck-right')
