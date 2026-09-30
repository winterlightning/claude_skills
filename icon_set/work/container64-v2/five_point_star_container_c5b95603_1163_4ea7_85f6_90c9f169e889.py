"""Five Pointed Star Symbol: independently authored container.

Construction plan: One five-point outline, mirrored about the vertical axis; no inner symbol.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg. Lucide star original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (five-point-star-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'c5b95603-1163-4ea7-85f6-90c9f169e889'
SOURCE_PATH = 'pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg'
AUTHOR = 'claude-opus-5-5'


class FivePointStarContainer(Container64):
    icon_id = 'five-point-star-container'
    keyshape = Keyshape.SQUARE
    category = 'holidays'
    categories = ('holidays', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('five', 'point', 'star', 'container')

    def build(self) -> None:
        self.add_line('star-1', (32, 6), (40, 25))
        self.add_line('star-2', (40, 25), (58, 25))
        self.add_line('star-3', (58, 25), (44, 37))
        self.add_line('star-4', (44, 37), (50, 58))
        self.add_line('star-5', (50, 58), (32, 47))
        self.add_line('star-6', (32, 47), (14, 58))
        self.add_line('star-7', (14, 58), (20, 37))
        self.add_line('star-8', (20, 37), (6, 25))
        self.add_line('star-9', (6, 25), (24, 25))
        self.add_line('star-10', (24, 25), (32, 6))
        self.add_contour('star', 'star-1', 'star-2', 'star-3', 'star-4', 'star-5', 'star-6', 'star-7', 'star-8', 'star-9', 'star-10', closed=True)
