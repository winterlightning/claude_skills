"""Simple Heart Symbol: independently authored container.

Construction plan: Two circular lobes flow into broad lower shoulders and a central pointed base; symmetric enclosure.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg. Lucide heart original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-outline-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '724cec2d-4e21-444d-b8dc-15e8d8bedd82'
SOURCE_PATH = 'pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg'
AUTHOR = 'claude-opus-5-5'


class HeartOutlineContainer(Container64):
    icon_id = 'heart-outline-container'
    keyshape = Keyshape.HRECT_L
    category = 'romance'
    categories = ('romance', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('heart', 'outline', 'container')

    def build(self) -> None:
        self.add_arc('heart-0', (32, 17), (20, 10), radius_x=12, radius_y=7, sweep=False)
        self.add_arc('heart-1', (20, 10), (4, 24), radius_x=16, radius_y=14, sweep=False)
        self.add_arc('heart-2', (4, 24), (12, 36), radius_x=13, sweep=False)
        self.add_line('heart-3', (12, 36), (32, 54))
        self.add_line('heart-4', (32, 54), (52, 36))
        self.add_arc('heart-5', (52, 36), (60, 24), radius_x=13, sweep=False)
        self.add_arc('heart-6', (60, 24), (44, 10), radius_x=16, radius_y=14, sweep=False)
        self.add_arc('heart-7', (44, 10), (32, 17), radius_x=12, radius_y=7, sweep=False)
        self.add_contour('heart', 'heart-0', 'heart-1', 'heart-2', 'heart-3', 'heart-4', 'heart-5', 'heart-6', 'heart-7', closed=True)
