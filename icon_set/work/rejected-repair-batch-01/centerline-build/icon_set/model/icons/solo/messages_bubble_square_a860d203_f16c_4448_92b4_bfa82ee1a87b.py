"""Messages bubble square (messages), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a860d203-f16c-4448-92b4-bfa82ee1a87b'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square_a860d203-f16c-4448-92b4-bfa82ee1a87b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MessagesBubbleSquare(Solo48):
    icon_id = 'messages-bubble-square'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'messages'
    aliases = ()
    keywords = ('messages', 'bubble', 'square')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (16, 33), (4, 33))
        self.add_line('e1', (4, 33), (4, 8))
        self.add_line('e2', (4, 8), (44, 8))
        self.add_line('e3', (44, 8), (44, 33))
        self.add_line('e4', (44, 33), (24, 33))
        self.add_line('e5', (23, 34), (16, 40))
        self.add_line('e6', (16, 40), (16, 33))
        self.add_line('e11', (24, 33), (23, 34))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e11', 'e5', 'e6', closed=True)
