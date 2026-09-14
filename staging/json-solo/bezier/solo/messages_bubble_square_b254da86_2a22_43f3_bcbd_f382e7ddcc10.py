"""Messages bubble square (messages), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b254da86-2a22-43f3-bcbd-f382e7ddcc10'
SOURCE_PATH = 'icons-json/messages/messages bubble square_b254da86-2a22-43f3-bcbd-f382e7ddcc10.json'
AUTHOR = 'json_to_solo'

class MessagesBubbleSquareB254da86(Solo48):
    icon_id = 'messages-bubble-square-b254da86'
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
        self.add_bezier('e7', (6, 33), ((5.127, 32.436), (4.018, 32.025), (4.018, 30.922)), ((4.009, 30.863), (4.009, 31.059), (4, 31)))
        self.add_bezier('e8', (4, 10), ((4, 9.966), (4.009, 9.617), (4.009, 9.583)), ((4.009, 8.716), (5.327, 8.269), (6, 8)))
        self.add_bezier('e9', (42, 8), ((43.227, 8.455), (43.509, 8.863), (44, 10)))
        self.add_bezier('e10', (44, 31), ((44, 31.067), (44, 30.872), (44, 30.939)), ((44, 32.051), (42.909, 32.469), (42, 33)))
        self.add_bezier('e11', (24, 33), ((23.7, 33.278), (23.318, 33.739), (23, 34)))
        self.add_bezier('e12', (16, 33), ((15.7, 33), (15.3, 33), (15, 33)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5', 'e6', 'e12', closed=True)
