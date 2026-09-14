"""Messages bubble square (messages), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a860d203-f16c-4448-92b4-bfa82ee1a87b'
SOURCE_PATH = 'icons-json/messages/messages bubble square_a860d203-f16c-4448-92b4-bfa82ee1a87b.json'
AUTHOR = 'json_to_solo'

class MessagesBubbleSquareA860d203(Solo48):
    icon_id = 'messages-bubble-square-a860d203'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'messages'
    aliases = ()
    keywords = ('messages', 'bubble', 'square')

    def build(self):
        self.add_line('e0', (15, 33), (6, 33))
        self.add_line('e1', (4, 31), (4, 10))
        self.add_line('e2', (6, 8), (42, 8))
        self.add_line('e3', (44, 10), (44, 31))
        self.add_line('e4', (42, 33), (24, 33))
        self.add_line('e5', (23, 34), (16, 40))
        self.add_line('e6', (16, 40), (16, 33))
        self.add_arc('e7', (6, 33), (4, 31), radius_x=2)
        self.add_arc('e8', (4, 10), (6, 8), radius_x=2)
        self.add_arc('e9', (42, 8), (44, 10), radius_x=2)
        self.add_arc('e10', (44, 31), (42, 33), radius_x=2)
        self.add_line('e11', (24, 33), (23, 34))
        self.add_arc('e12', (16, 33), (15, 33), radius_x=20, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5', 'e6', 'e12', closed=True)
