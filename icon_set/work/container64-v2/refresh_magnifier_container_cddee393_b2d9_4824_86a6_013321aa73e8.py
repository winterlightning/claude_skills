"""Magnifying Glass with Circular Arrows: independently authored container.

Construction plan: A magnifying handle attaches to an open circular pair of refresh arrows; preserve the two directional heads.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg. Lucide refresh-cw original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (refresh-magnifier-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'cddee393-b2d9-4824-86a6-013321aa73e8'
SOURCE_PATH = 'pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'
AUTHOR = 'claude-opus-5-5'


class RefreshMagnifierContainer(Container64):
    icon_id = 'refresh-magnifier-container'
    keyshape = Keyshape.SQUARE
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('refresh', 'magnifier', 'container')

    def build(self) -> None:
        self.add_arc('upper-0', (10, 40), (6, 29), radius_x=18)
        self.add_arc('upper-1', (6, 29), (28, 6), radius_x=22, radius_y=23)
        self.add_line('upper-head-1', (20, 6), (28, 6))
        self.add_line('upper-head-2', (28, 6), (26, 12))
        self.add_arc('lower-0', (46, 14), (50, 29), radius_x=30)
        self.add_arc('lower-1', (50, 29), (41, 45), radius_x=18)
        self.add_arc('lower-2', (41, 45), (28, 50), radius_x=19)
        self.add_line('lower-head-1', (34, 50), (28, 50))
        self.add_line('lower-head-2', (28, 50), (30, 42))
        self.add_line('handle', (41, 45), (58, 58))
        self.add_contour('upper', 'upper-0', 'upper-1')
        self.add_contour('upper-head', 'upper-head-1', 'upper-head-2')
        self.add_contour('lower', 'lower-0', 'lower-1', 'lower-2')
        self.add_contour('lower-head', 'lower-head-1', 'lower-head-2')
        self.relate('connect', 'upper', 'upper-head')
        self.relate('connect', 'lower', 'lower-head')
        self.relate('connect', 'handle', 'lower')
