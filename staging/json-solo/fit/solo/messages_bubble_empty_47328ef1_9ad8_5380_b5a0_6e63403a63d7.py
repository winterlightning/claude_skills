"""Messages bubble empty (chat), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47328ef1-9ad8-5380-b5a0-6e63403a63d7'
SOURCE_PATH = 'icons-json/chat/messages bubble empty_47328ef1-9ad8-5380-b5a0-6e63403a63d7.json'
AUTHOR = 'json_to_solo'

class MessagesBubbleEmptyChat(Solo48):
    icon_id = 'messages-bubble-empty-chat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('messages', 'bubble', 'empty', 'chat')

    def build(self):
        self.add_line('e0', (19, 40), (27, 33))
        self.add_line('e1', (28, 33), (33, 33))
        self.add_line('e2', (32, 8), (16, 8))
        self.add_line('e3', (16, 33), (19, 33))
        self.add_line('e4', (19, 33), (19, 40))
        self.add_line('e5', (27, 33), (28, 33))
        self.add_arc('e6-1', (33, 33), (44, 21), radius_x=13, sweep=False)
        self.add_line('e6-2', (44, 21), (43, 15))
        self.add_arc('e6-3', (43, 15), (37, 9), radius_x=14, sweep=False)
        self.add_line('e6-4', (37, 9), (32, 8))
        self.add_arc('e7-1', (16, 8), (4, 20), radius_x=12, sweep=False)
        self.add_line('e7-2', (4, 20), (6, 27))
        self.add_arc('e7-3', (6, 27), (10, 31), radius_x=13, sweep=False)
        self.add_arc('e7-4', (10, 31), (16, 33), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e3', 'e4', closed=True)
