"""An upright rounded playing card containing a pointed spade and broad stem. VRECT_L preserves portrait proportions. Suit geometry mirrors about x=32; curved lobes and a single contiguous stem contour preserve the source identity. Card corners have radius 6.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 invalid, heart-state-63 valid, check-mark valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (spade-playing-card VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '81760339-2759-54a7-9d7d-41a82e29e532'
SOURCE_PATH = 'pictographic-primitives/entertainment/spades card_81760339-2759-54a7-9d7d-41a82e29e532.svg'
AUTHOR = 'claude-opus-5-5'


class QueueIcon(Container64):
    icon_id = 'spade-playing-card'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Spade Playing Card',)
    keywords = ('spade', 'playing', 'card')

    def build(self) -> None:
        self.add_line('card-0', (18, 4), (46, 4))
        self.add_arc('card-1', (46, 4), (52, 10), radius_x=6)
        self.add_line('card-2', (52, 10), (52, 54))
        self.add_arc('card-3', (52, 54), (46, 60), radius_x=6)
        self.add_line('card-4', (46, 60), (18, 60))
        self.add_arc('card-5', (18, 60), (12, 54), radius_x=6)
        self.add_line('card-6', (12, 54), (12, 10))
        self.add_arc('card-7', (12, 10), (18, 4), radius_x=6)
        self.add_bezier('spade', (32, 18), ((24.4, 24.364), (14, 31), (22, 36.909)), ((25.2, 39.636), (29, 36), (28, 36)))
        self.add_line('base-1', (28, 36), (26, 46))
        self.add_line('base-2', (26, 46), (38, 46))
        self.add_line('base-3', (38, 46), (36, 36))
        self.add_bezier('right', (36, 36), ((35, 36), (38.8, 39.636), (42, 36.909)), ((50, 31), (39.6, 24.364), (32, 18)))
        self.add_contour('card', 'card-0', 'card-1', 'card-2', 'card-3', 'card-4', 'card-5', 'card-6', 'card-7', closed=True)
        self.add_contour('suit', 'spade', 'base-1', 'base-2', 'base-3', 'right', closed=True)
