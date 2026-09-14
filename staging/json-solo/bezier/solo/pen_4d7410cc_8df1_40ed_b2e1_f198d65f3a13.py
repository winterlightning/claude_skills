"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d7410cc-8df1-40ed-b2e1-f198d65f3a13'
SOURCE_PATH = 'icons-json/design/pen_4d7410cc-8df1-40ed-b2e1-f198d65f3a13.json'
AUTHOR = 'json_to_solo'

class Pen(Solo48):
    icon_id = 'pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (35, 22), (26, 13))
        self.add_line('e1', (6, 42), (11, 30))
        self.add_line('e2', (11, 30), (32, 8))
        self.add_line('e3', (35, 21), (19, 38))
        self.add_bezier('e4', (32, 8), ((33.079, 6.88), (34.588, 6), (36.141, 6)), ((36.166, 6), (36.191, 6), (36.215, 6)), ((38.76, 6), (41.043, 7.685), (41.755, 10.124)), ((41.861, 10.484), (42, 10.901), (42, 11.277)), ((42, 11.278), (42, 11.279), (42, 11.28)), ((42, 11.336), (42, 11.393), (42, 11.449)), ((42, 11.572), (41.992, 11.695), (41.992, 11.817)), ((41.992, 14.215), (40.331, 15.663), (38.809, 17.258)), ((37.696, 18.42), (36.113, 19.838), (35, 21)))
        self.add_bezier('e5', (19, 38), ((16.275, 39.366), (13.2, 39.865), (10.279, 40.699)), ((9.207, 41.002), (8.037, 41.231), (7.039, 41.722)), ((6.867, 41.812), (6.695, 41.91), (6.524, 42)), ((6.352, 42), (6.172, 42), (6, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4', 'e3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
