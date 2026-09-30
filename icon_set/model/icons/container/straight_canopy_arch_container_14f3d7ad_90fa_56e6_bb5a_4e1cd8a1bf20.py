"""An empty wedding canopy with a triangular roof, a horizontal lintel, two slender posts and short ground feet. Retain the diagonal corner braces and exclude the hanging heart. Do not add draped curtains.

Plan: Triangular canopy with paired uprights, straight corner braces, and ground feet. Bounds (2,2)-(62,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide tent: straight structural roof; source supplies curved braces and upright posts.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (straight-canopy-arch-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20'
SOURCE_ICON_IDS = ('14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20',)
SOURCE_PATH = 'pictographic-primitives/romance/wedding altar_14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20.svg'
AUTHOR = 'claude-opus-5-5'


class StraightCanopyArchContainer(Container64):
    icon_id = 'straight-canopy-arch-container'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('straight', 'canopy', 'arch', 'container')

    def build(self) -> None:
        self.add_line('roof-1', (6, 23), (32, 6))
        self.add_line('roof-2', (32, 6), (58, 23))
        self.add_line('roof-3', (58, 23), (6, 23))
        self.add_line('left-post', (10, 23), (10, 58))
        self.add_line('left-foot', (6, 58), (14, 58))
        self.add_line('left-brace', (10, 39), (24, 23))
        self.add_line('right-post', (54, 23), (54, 58))
        self.add_line('right-foot', (50, 58), (58, 58))
        self.add_line('right-brace', (54, 39), (40, 23))
        self.add_contour('roof', 'roof-1', 'roof-2', 'roof-3', closed=True)
        self.relate('connect', 'roof', 'left-post')
        self.relate('connect', 'roof', 'left-brace')
        self.relate('connect', 'left-post', 'left-brace')
        self.relate('connect', 'left-post', 'left-foot')
        self.relate('connect', 'roof', 'right-post')
        self.relate('connect', 'roof', 'right-brace')
        self.relate('connect', 'right-post', 'right-brace')
        self.relate('connect', 'right-post', 'right-foot')
