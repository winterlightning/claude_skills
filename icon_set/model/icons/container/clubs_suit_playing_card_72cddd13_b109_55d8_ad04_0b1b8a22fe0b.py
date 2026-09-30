"""An upright rounded playing card containing a three-lobed club. VRECT_L preserves its portrait proportions; the centered suit mirrors about x=32. Rounded corner radius 6; lobes share one coherent curve. No corner rank or decorative detail added.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 valid, heart-state-63 valid, check-mark valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (clubs-suit-playing-card VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '72cddd13-b109-55d8-ad04-0b1b8a22fe0b'
SOURCE_PATH = 'pictographic-primitives/entertainment/clubs card_72cddd13-b109-55d8-ad04-0b1b8a22fe0b.svg'
AUTHOR = 'claude-opus-5-5'


class QueueIcon(Container64):
    icon_id = 'clubs-suit-playing-card'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Clubs Suit Playing Card',)
    keywords = ('clubs', 'suit', 'playing', 'card')

    def build(self) -> None:
        self.add_line('card-0', (18, 4), (46, 4))
        self.add_arc('card-1', (46, 4), (52, 10), radius_x=6)
        self.add_line('card-2', (52, 10), (52, 54))
        self.add_arc('card-3', (52, 54), (46, 60), radius_x=6)
        self.add_line('card-4', (46, 60), (18, 60))
        self.add_arc('card-5', (18, 60), (12, 54), radius_x=6)
        self.add_line('card-6', (12, 54), (12, 10))
        self.add_arc('card-7', (12, 10), (18, 4), radius_x=6)
        self.add_bezier('club', (28, 34), ((14, 37.6), (18, 20.083), (26, 25.5)), ((21.2, 11.833), (42.8, 11.833), (38, 25.5)), ((46, 20.083), (50, 37.6), (36, 34)))
        self.add_line('base-1', (36, 34), (38, 43))
        self.add_line('base-2', (38, 43), (26, 43))
        self.add_line('base-3', (26, 43), (28, 34))
        self.add_contour('card', 'card-0', 'card-1', 'card-2', 'card-3', 'card-4', 'card-5', 'card-6', 'card-7', closed=True)
        self.add_contour('suit', 'club', 'base-1', 'base-2', 'base-3', closed=True)
