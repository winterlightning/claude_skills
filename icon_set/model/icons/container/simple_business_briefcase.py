"""A rounded business case has a centered top carrying handle.

HRECT_XL: visible bounds (0, 4, 64, 60), chosen for the subject proportions.
Lucide briefcase: rounded enclosure and symmetrical handle; original and atomic-debug inspected.
Source plain case retained without added straps; no source features dropped.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-business-briefcase HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleBusinessBriefcase(Container64):
    icon_id = 'simple-business-briefcase'
    keyshape = Keyshape.SQUARE
    aliases = ('business-briefcase',)
    keywords = ('simple', 'business', 'briefcase')

    def build(self) -> None:
        # SQUARE (was HRECT_L): case 6..58 x 18..58 under the handle, so the case holds a symbol of 28 with a
        # 4 px gap (was 20 in the shorter landscape case). Mirrored about x = 32.
        self.add_line('case0', (14, 18), (50, 18))
        self.add_arc('case1', (50, 18), (58, 26), radius_x=8)
        self.add_line('case2', (58, 26), (58, 50))
        self.add_arc('case3', (58, 50), (50, 58), radius_x=8)
        self.add_line('case4', (50, 58), (14, 58))
        self.add_arc('case5', (14, 58), (6, 50), radius_x=8)
        self.add_line('case6', (6, 50), (6, 26))
        self.add_arc('case7', (6, 26), (14, 18), radius_x=8)
        self.add_line('handle-left', (22, 18), (22, 12))
        self.add_arc('handle-nw', (22, 12), (28, 6), radius_x=6)
        self.add_line('handle-top', (28, 6), (36, 6))
        self.add_arc('handle-ne', (36, 6), (42, 12), radius_x=6)
        self.add_line('handle-right', (42, 12), (42, 18))
        self.add_contour('case', 'case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', closed=True)
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right')
        self.relate('connect', 'case', 'handle')
