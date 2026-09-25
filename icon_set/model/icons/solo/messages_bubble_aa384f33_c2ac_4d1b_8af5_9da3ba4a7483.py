"""Messages bubble (chat), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa384f33-c2ac-4d1b-8af5-9da3ba4a7483'
SOURCE_PATH = 'pictographic-primitives/chat/messages bubble_aa384f33-c2ac-4d1b-8af5-9da3ba4a7483.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MessagesBubble(Solo48):
    icon_id = 'messages-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    categories = ('chat', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('messages', 'bubble', 'chat')

    def build(self):
        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.
        # Reference: original stroke graph and contour extremes.
        self.add_line('e0', (19, 35), (7, 40))
        self.add_line('e1', (7, 40), (11, 32))
        self.add_bezier('e2', (11, 32), ((7.436, 29.684), (4.0, 26.392), (4, 22.063)), ((4, 21.811), (4.009, 21.558), (4.009, 21.305)), ((4.009, 19.907), (4.473, 18.467), (5.118, 17.213)), ((8.182, 11.251), (16.218, 8.017), (23.1, 8.017)), ((23.297, 8.017), (23.494, 8), (23.691, 8)), ((24.182, 8), (24.664, 8.017), (25.155, 8.017)), ((32.191, 8.017), (40.6, 11.705), (43.236, 18.055)), ((43.664, 19.074), (43.991, 20.244), (43.991, 21.347)), ((43.991, 21.43), (44, 21.525000000000002), (44, 21.608)), ((44, 21.819), (43.991, 22.029), (43.991, 22.24)), ((43.991, 25.794), (41.436, 29.061), (38.591, 31.208)), ((32.973, 35.444), (25.882, 36.297), (19, 35)))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
