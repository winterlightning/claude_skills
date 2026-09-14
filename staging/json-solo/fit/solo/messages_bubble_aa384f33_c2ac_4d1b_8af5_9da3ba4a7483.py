"""Messages bubble (chat), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa384f33-c2ac-4d1b-8af5-9da3ba4a7483'
SOURCE_PATH = 'icons-json/chat/messages bubble_aa384f33-c2ac-4d1b-8af5-9da3ba4a7483.json'
AUTHOR = 'json_to_solo'

class MessagesBubbleChat(Solo48):
    icon_id = 'messages-bubble-chat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('messages', 'bubble', 'chat')

    def build(self):
        self.add_line('e0', (19, 35), (7, 40))
        self.add_line('e1', (7, 40), (11, 32))
        self.add_arc('e2-1', (11, 32), (4, 22), radius_x=12)
        self.add_arc('e2-2', (4, 22), (10, 12), radius_x=12)
        self.add_arc('e2-3', (10, 12), (16, 9), radius_x=23)
        self.add_line('e2-4', (16, 9), (24, 8))
        self.add_arc('e2-5', (24, 8), (31, 9), radius_x=27)
        self.add_arc('e2-6', (31, 9), (38, 12), radius_x=22)
        self.add_arc('e2-7', (38, 12), (44, 22), radius_x=12)
        self.add_arc('e2-8', (44, 22), (36, 33), radius_x=13)
        self.add_arc('e2-9', (36, 33), (19, 35), radius_x=26)
        self.add_contour('c0', 'e0', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', closed=True)
