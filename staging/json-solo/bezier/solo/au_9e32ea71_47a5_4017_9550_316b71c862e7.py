"""Au (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e32ea71-47a5-4017-9550-316b71c862e7'
SOURCE_PATH = 'icons-json/symbol/Au_9e32ea71-47a5-4017-9550-316b71c862e7.json'
AUTHOR = 'json_to_solo'

class AuSymbol(Solo48):
    icon_id = 'au-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('au', 'symbol')

    def build(self):
        self.add_line('e0', (23, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_line('e3', (33, 19), (33, 34))
        self.add_line('e4', (44, 19), (44, 40))
        self.add_bezier('e5', (15, 10), ((14.618, 8.622), (14.145, 8.025), (12.955, 8.025)), ((12.838, 8.012), (12.722, 8), (12.606, 8)), ((12.604, 8), (12.602, 8), (12.6, 8)), ((12.545, 8.012), (12.482, 8.012), (12.427, 8.025)), ((11.664, 8.025), (11.391, 8.323), (11, 9)))
        self.add_bezier('e6', (33, 34), ((33, 37.495), (35.618, 39.975), (38.136, 39.975)), ((38.245, 39.988), (38.355, 39.988), (38.464, 40)), ((38.582, 40), (38.7, 39.988), (38.809, 39.988)), ((40.936, 39.988), (43.991, 37.206), (43.991, 33.994)), ((43.991, 33.945), (44, 34.049), (44, 34)))
        self.add_contour('c0', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e6')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
