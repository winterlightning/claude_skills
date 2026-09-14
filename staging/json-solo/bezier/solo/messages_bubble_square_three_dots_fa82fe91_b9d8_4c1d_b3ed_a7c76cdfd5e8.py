"""Messages bubble square three dots (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8'
SOURCE_PATH = 'icons-json/symbol/messages bubble square three dots_fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8.json'
AUTHOR = 'json_to_solo'

class MessagesBubbleSquareThreeDotsSymbol(Solo48):
    icon_id = 'messages-bubble-square-three-dots-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('messages', 'bubble', 'square', 'three', 'dots', 'symbol')

    def build(self):
        self.add_line('e0', (13, 35), (9, 35))
        self.add_line('e1', (6, 31), (6, 10))
        self.add_line('e2', (9, 6), (39, 6))
        self.add_line('e3', (42, 10), (42, 31))
        self.add_line('e4', (38, 35), (21, 35))
        self.add_line('e5', (21, 35), (13, 42))
        self.add_line('e6', (13, 42), (13, 35))
        self.add_bezier('e7', (9, 35), ((7.274, 35), (6, 32.555), (6, 31)))
        self.add_bezier('e8', (6, 10), ((6, 9.951), (6.008, 10.001), (6.008, 9.952)), ((6.008, 8.455), (7.497, 6.016), (9.175, 6.016)), ((9.207, 6.008), (8.967, 6.008), (9, 6)))
        self.add_bezier('e9', (39, 6), ((39.205, 6.057), (39.128, 6.041), (39.333, 6.131)), ((40.765, 6.769), (42, 8.388), (42, 10)))
        self.add_bezier('e10', (42, 31), ((42, 32.448), (40.576, 33.483), (39.39, 34.121)), ((38.932, 34.366), (38.491, 34.853), (38, 35)))
        self.add_dot('e11', (15, 21))
        self.add_dot('e12', (24, 21))
        self.add_dot('e13', (33, 21))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e5', 'e6', closed=True)
