"""A rounded business case has a centered top carrying handle.

HRECT_XL: visible bounds (0, 4, 64, 60), chosen for the subject proportions.
Lucide briefcase: rounded enclosure and symmetrical handle; original and atomic-debug inspected.
Source plain case retained without added straps; no source features dropped.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-business-briefcase HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleBusinessBriefcase(Container64):
    icon_id = 'simple-business-briefcase'
    keyshape = Keyshape.HRECT_L
    aliases = ('business-briefcase',)
    keywords = ('simple', 'business', 'briefcase')

    def build(self) -> None:
        self.add_line('case0', (12, 22), (52, 22))
        self.add_arc('case1', (52, 22), (60, 28), radius_x=8, radius_y=6)
        self.add_line('case2', (60, 28), (60, 46))
        self.add_arc('case3', (60, 46), (52, 54), radius_x=8)
        self.add_line('case4', (52, 54), (12, 54))
        self.add_arc('case5', (12, 54), (4, 46), radius_x=8)
        self.add_line('case6', (4, 46), (4, 28))
        self.add_arc('case7', (4, 28), (12, 22), radius_x=8, radius_y=6)
        self.add_line('handle-left', (22, 22), (22, 16))
        self.add_arc('handle-nw', (22, 16), (28, 10), radius_x=6)
        self.add_line('handle-top', (28, 10), (36, 10))
        self.add_arc('handle-ne', (36, 10), (42, 16), radius_x=6)
        self.add_line('handle-right', (42, 16), (42, 22))
        self.add_contour('case', 'case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', closed=True)
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right')
        self.relate('connect', 'handle', 'case')
