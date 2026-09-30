"""A circular magnifier with a diagonal lower-right handle and a short upper-left stalk ending in a separate small circle. Exclude all network nodes inside the lens.

Plan: Lens and terminal circles, with explicit stalk and handle joins. Deliberate diagonal asymmetry; bounds (2,2)-(62,62).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: invalid, check-mark: invalid.
Construction reference: Lucide search: circular lens and attached diagonal handle.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (magnifier-with-upper-left-node-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '154aad0f-3143-54c6-ad52-2c6edd95a6c2'
SOURCE_ICON_IDS = ('154aad0f-3143-54c6-ad52-2c6edd95a6c2',)
SOURCE_PATH = 'pictographic-primitives/programing/amazon inspector_154aad0f-3143-54c6-ad52-2c6edd95a6c2.svg'
AUTHOR = 'claude-opus-5-5'


class MagnifierWithUpperLeftNodeContainer(Container64):
    icon_id = 'magnifier-with-upper-left-node-container'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('magnifier', 'with', 'upper', 'left', 'node', 'container')

    def build(self) -> None:
        self.add_arc('lens-a', (26, 22), (42, 46), radius_x=15)
        self.add_arc('lens-b', (42, 46), (26, 22), radius_x=15)
        self.add_arc('terminal-a', (14, 15), (8, 7), radius_x=5)
        self.add_arc('terminal-b', (8, 7), (14, 15), radius_x=5)
        self.add_line('stalk', (14, 15), (26, 22))
        self.add_line('handle', (42, 46), (58, 58))
        self.add_contour('lens', 'lens-a', 'lens-b', closed=True)
        self.add_contour('terminal', 'terminal-a', 'terminal-b', closed=True)
        self.relate('connect', 'lens', 'stalk')
        self.relate('connect', 'terminal', 'stalk')
        self.relate('connect', 'lens', 'handle')
