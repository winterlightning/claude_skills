"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7'
SOURCE_PATH = 'icons-json/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.json'
AUTHOR = 'json_to_solo'

class Dice56c4bb3a(Solo48):
    icon_id = 'dice-56c4bb3a'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_line('e0', (6, 35), (6, 13))
        self.add_line('e1', (13, 6), (36, 6))
        self.add_line('e2', (42, 11), (42, 35))
        self.add_line('e3', (35, 42), (13, 42))
        self.add_bezier('e4', (15, 15), ((15, 15.27), (15, 15.73), (15, 16)))
        self.add_bezier('e5', (33, 15), ((33, 15.27), (33, 15.73), (33, 16)))
        self.add_bezier('e6', (33, 33), ((33, 33.27), (33, 33.73), (33, 34)))
        self.add_bezier('e7', (24, 24), ((24, 24.27), (24, 24.73), (24, 25)))
        self.add_bezier('e8', (15, 33), ((15, 33.27), (15, 33.73), (15, 34)))
        self.add_bezier('e9', (13, 42), ((13.147, 42), (12.243, 41.984), (12.095, 41.984)), ((9.371, 41.984), (7.178, 40.012), (6.36, 37.5)), ((6.196, 37.001), (6, 36.395), (6, 35.872)), ((6, 35.733), (6, 35.139), (6, 35)))
        self.add_bezier('e10', (6, 13), ((6, 12.869), (6.008, 12.284), (6.008, 12.153)), ((6.008, 8.782), (8.995, 6.016), (12.341, 6.016)), ((12.415, 6.008), (12.935, 6), (13, 6)))
        self.add_bezier('e11', (36, 6), ((38.373, 6), (40.863, 7.587), (41.665, 9.796)), ((41.795, 10.156), (42, 10.607), (42, 11)))
        self.add_bezier('e12', (42, 35), ((42, 35.327), (42, 36.109), (42, 36.436)), ((42, 39.177), (38.883, 41.992), (36.215, 41.992)), ((36.093, 41.992), (35.962, 42), (35.839, 42)), ((35.708, 42), (35.131, 42), (35, 42)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3', closed=True)
