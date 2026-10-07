"""Simple Heart Symbol: independently authored container.

Construction plan: Two circular lobes flow into broad lower shoulders and a central pointed base; symmetric enclosure.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg. Lucide heart original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-outline-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '724cec2d-4e21-444d-b8dc-15e8d8bedd82'
SOURCE_PATH = 'pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg'
AUTHOR = 'claude-opus-5-5'


class HeartOutlineContainer(Container64):
    icon_id = 'heart-outline-container'
    keyshape = Keyshape.SQUARE
    category = 'romance'
    categories = ('romance', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('heart', 'outline', 'container')

    def build(self) -> None:
        # SQUARE (was HRECT_L): a full heart, lobes topping out at (18,6)/(46,6), widest at y 27, tip at (32,58);
        # mirrored about x = 32. Holds a symbol of 24 with a 4 px gap (was 15.5 in the landscape frame).
        self.add_bezier('heart-left', (32, 12), ((30, 8), (25, 6), (18, 6)), ((10, 6), (6, 14), (6, 27)), ((6, 42), (21, 51), (32, 58)))
        self.add_bezier('heart-right', (32, 58), ((43, 51), (58, 42), (58, 27)), ((58, 14), (54, 6), (46, 6)), ((39, 6), (34, 8), (32, 12)))
        self.add_contour('heart', 'heart-left', 'heart-right', closed=True)
