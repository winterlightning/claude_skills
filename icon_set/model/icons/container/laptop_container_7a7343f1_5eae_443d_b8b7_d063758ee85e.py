"""Personal Laptop Computer: independently authored container.

Construction plan: Rounded upright screen and flared base share the screen lower edge; no keyboard detail in source.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg. Lucide laptop original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (laptop-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '7a7343f1-5eae-443d-b8b7-d063758ee85e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'
AUTHOR = 'claude-opus-5-5'


class LaptopContainer(Container64):
    icon_id = 'laptop-container'
    keyshape = Keyshape.HRECT_L
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('laptop', 'container')

    def build(self) -> None:
        self.add_line('screen-0', (8, 42), (8, 14))
        self.add_arc('screen-1', (8, 14), (12, 10), radius_x=4)
        self.add_line('screen-2', (12, 10), (52, 10))
        self.add_arc('screen-3', (52, 10), (56, 14), radius_x=4)
        self.add_line('screen-4', (56, 14), (56, 42))
        self.add_line('base-1', (8, 42), (56, 42))
        self.add_line('base-2', (56, 42), (60, 54))
        self.add_line('base-3', (60, 54), (4, 54))
        self.add_line('base-4', (4, 54), (8, 42))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4')
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', closed=True)
        self.relate('connect', 'base', 'screen')
