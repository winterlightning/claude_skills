"""2-1 (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17d5ec75-09d3-4664-bd59-09488d4395a3'
SOURCE_PATH = 'icons-json/symbol/2-1 (text)_17d5ec75-09d3-4664-bd59-09488d4395a3.json'
AUTHOR = 'json_to_solo'

class Icon21TextSymbol(Solo48):
    icon_id = 'icon-2-1-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (11, 24), (4, 40))
        self.add_line('e1', (4, 40), (13, 40))
        self.add_line('e2', (44, 8), (44, 40))
        self.add_line('e3', (25, 22), (29, 22))
        self.add_bezier('e4', (4, 14), ((4.009, 13.984), (4.009, 14.368), (4.018, 14.352)), ((4.018, 14.128), (4.245, 13.68), (4.309, 13.52)), ((5.036, 11.6), (6.855, 8.032), (8.245, 8.032)), ((8.318, 8.016), (8.391, 8.016), (8.473, 8)), ((8.545, 8), (8.627, 8), (8.7, 8.016)), ((9.4, 8.016), (10.118, 8.752), (10.655, 9.456)), ((13.264, 12.848), (12.936, 19.744), (11, 24)))
        self.add_bezier('e5', (39, 14), ((40.809, 12.288), (42.645, 10.736), (44, 8)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
