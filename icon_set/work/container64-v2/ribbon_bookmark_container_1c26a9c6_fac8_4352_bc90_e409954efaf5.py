"""Ribbon Shape Bookmark Tag: independently authored container.

Construction plan: Single rounded-top vertical ribbon with centered V notch; mirrored corners.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.svg. Lucide bookmark original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (ribbon-bookmark-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '1c26a9c6-fac8-4352-bc90-e409954efaf5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.svg'
AUTHOR = 'claude-opus-5-5'


class RibbonBookmarkContainer(Container64):
    icon_id = 'ribbon-bookmark-container'
    keyshape = Keyshape.VRECT_M
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('ribbon', 'bookmark', 'container')

    def build(self) -> None:
        self.add_line('ribbon-0', (12, 60), (12, 8))
        self.add_arc('ribbon-1', (12, 8), (16, 4), radius_x=4)
        self.add_line('ribbon-2', (16, 4), (48, 4))
        self.add_arc('ribbon-3', (48, 4), (52, 8), radius_x=4)
        self.add_line('ribbon-4', (52, 8), (52, 60))
        self.add_line('ribbon-5', (52, 60), (32, 45))
        self.add_line('ribbon-6', (32, 45), (12, 60))
        self.add_contour('ribbon', 'ribbon-0', 'ribbon-1', 'ribbon-2', 'ribbon-3', 'ribbon-4', 'ribbon-5', 'ribbon-6', closed=True)
