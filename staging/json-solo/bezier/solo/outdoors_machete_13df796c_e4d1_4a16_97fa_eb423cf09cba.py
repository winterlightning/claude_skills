"""Outdoors machete (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13df796c-e4d1-4a16-97fa-eb423cf09cba'
SOURCE_PATH = 'icons-json/outdoors/outdoors machete_13df796c-e4d1-4a16-97fa-eb423cf09cba.json'
AUTHOR = 'json_to_solo'

class OutdoorsMacheteOutdoors(Solo48):
    icon_id = 'outdoors-machete-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'machete')

    def build(self):
        self.add_line('e0', (17, 26), (21, 31))
        self.add_line('e1', (17, 26), (7, 35))
        self.add_line('e2', (6, 39), (8, 42))
        self.add_line('e3', (13, 38), (21, 31))
        self.add_line('e4', (17, 26), (40, 6))
        self.add_line('e5', (39, 19), (22, 33))
        self.add_line('e6', (22, 33), (21, 31))
        self.add_bezier('e7', (7, 35), ((6.705, 35.245), (6, 35.7), (6, 36.093)), ((6, 36.584), (6.016, 37.066), (6.016, 37.557)), ((6.016, 37.713), (6.016, 37.885), (6.016, 38.048)), ((6.008, 38.097), (6.008, 38.146), (6, 38.195)), ((6, 38.375), (6, 38.828), (6, 39)))
        self.add_bezier('e8', (8, 42), ((8.172, 42), (8.79, 42), (8.962, 42)), ((9.125, 42), (9.305, 41.984), (9.477, 41.984)), ((9.51, 41.992), (9.535, 41.992), (9.567, 42)), ((9.854, 42), (10.14, 42), (10.426, 42)), ((10.574, 42), (10.86, 41.746), (10.966, 41.656)), ((12.226, 40.65), (12.656, 39.391), (13, 38)))
        self.add_bezier('e9', (40, 6), ((40.139, 6), (40.65, 6), (40.789, 6)), ((40.879, 6), (41.133, 6.704), (41.223, 6.965)), ((41.542, 7.955), (41.992, 9.101), (41.992, 10.156)), ((41.992, 10.245), (42, 10.326), (42, 10.414)), ((42, 10.415), (42, 10.417), (42, 10.418)), ((42, 10.565), (41.984, 10.721), (41.984, 10.876)), ((41.984, 13.028), (40.612, 17.634), (39, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
