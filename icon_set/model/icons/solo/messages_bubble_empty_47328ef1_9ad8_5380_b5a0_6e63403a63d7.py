"""Messages bubble empty (chat), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47328ef1-9ad8-5380-b5a0-6e63403a63d7'
SOURCE_PATH = 'pictographic-primitives/chat/messages bubble empty_47328ef1-9ad8-5380-b5a0-6e63403a63d7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MessagesBubbleEmpty(Solo48):
    icon_id = 'messages-bubble-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    categories = ('chat', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('messages', 'bubble', 'empty', 'chat')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (19, 40), (27, 33))
        self.add_line('e1', (27, 33), (33, 33))
        self.add_line('e2', (32, 8), (16, 8))
        self.add_line('e3', (16, 33), (19, 33))
        self.add_line('e4', (19, 33), (19, 40))
        self.add_bezier('e6', (33, 33), ((33.736, 33), (34.764, 32.63), (35.473, 32.39)), ((39.891, 30.85), (43.991, 26.42), (43.991, 21.03)), ((43.991, 20.882), (44, 20.735), (44, 20.587)), ((44, 20.35), (43.991, 20.13), (43.991, 19.9)), ((43.991, 13.7), (38.373, 8.01), (32.845, 8.01)), ((32.7, 8.01), (32.555, 8), (32.4, 8)), ((32.327, 8), (32.073, 8), (32, 8)))
        self.add_bezier('e7', (16, 8), ((15.845, 8), (15.518, 8.01), (15.364, 8.01)), ((10.455, 8.01), (5.645, 12.06), (4.391, 17.29)), ((4.227, 17.96), (4.009, 18.74), (4.009, 19.44)), ((4.009, 19.598), (4, 19.745), (4, 19.903)), ((4, 20.15), (4.009, 20.39), (4.009, 20.63)), ((4.009, 26.14), (7.664, 30.33), (12.145, 32.13)), ((13.273, 32.59), (14.791, 33), (16, 33)))
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4', closed=True)
