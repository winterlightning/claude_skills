"""Personal Laptop Computer: independently authored container.

Construction plan: Rounded upright screen and flared base share the screen lower edge; no keyboard detail in source.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg. Lucide laptop original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (laptop-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '7a7343f1-5eae-443d-b8b7-d063758ee85e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'
AUTHOR = 'claude-opus-5-5'


class LaptopContainer(Container64):
    icon_id = 'laptop-container'
    keyshape = Keyshape.SQUARE
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('laptop', 'container')

    def build(self) -> None:
        # SQUARE (was HRECT_L): screen 10..54 x 6..48 over a base that flares to the keyshape at 58, so the
        # display holds a symbol of 28 with a 4 px gap (was 20 in the shorter landscape frame).
        self.add_line('screen-0', (10, 48), (10, 10))
        self.add_arc('screen-1', (10, 10), (14, 6), radius_x=4)
        self.add_line('screen-2', (14, 6), (50, 6))
        self.add_arc('screen-3', (50, 6), (54, 10), radius_x=4)
        self.add_line('screen-4', (54, 10), (54, 48))
        self.add_line('base-1', (10, 48), (54, 48))
        self.add_line('base-2', (54, 48), (58, 58))
        self.add_line('base-3', (58, 58), (6, 58))
        self.add_line('base-4', (6, 58), (10, 48))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4')
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', closed=True)
        self.relate('connect', 'base', 'screen')
