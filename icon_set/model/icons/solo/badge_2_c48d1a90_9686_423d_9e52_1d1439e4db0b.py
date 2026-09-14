"""Badge 2 (other), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48d1a90-9686-423d-9e52-1d1439e4db0b'
SOURCE_PATH = 'icons-json/other/badge 2_c48d1a90-9686-423d-9e52-1d1439e4db0b.json'
AUTHOR = 'json_to_solo'

class Badge2(Solo48):
    icon_id = 'badge-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('badge', 'other')

    def build(self):
        self.add_bezier('sym-e0', (38, 30), ((38.565, 29.681), (38.517, 29.425), (39, 29)))
        self.add_bezier('sym-e1', (39, 29), ((40.055, 28.067), (42, 25.448), (42, 24)))
        self.add_bezier('sym-e2', (42, 24), ((42, 23.952), (42, 24.054), (42, 24)))
        self.add_bezier('sym-e3', (42, 24), ((42, 23.946), (42, 24.048), (42, 24)))
        self.add_bezier('sym-e4', (42, 24), ((42, 22.552), (40.055, 19.933), (39, 19)))
        self.add_bezier('sym-e5', (39, 19), ((38.517, 18.575), (38.565, 18.319), (38, 18)))
        self.add_bezier('sym-e6', (38, 18), ((39.743, 12.453), (35.58, 8.167), (30, 10)))
        self.add_bezier('sym-e7', (30, 10), ((28.816, 7.849), (26.605, 6.057), (24, 6)))
        self.add_bezier('sym-e8', (24, 6), ((21.395, 6.057), (19.184, 7.849), (18, 10)))
        self.add_bezier('sym-e9', (18, 10), ((12.42, 8.167), (8.257, 12.453), (10, 18)))
        self.add_bezier('sym-e10', (10, 18), ((9.435, 18.319), (9.483, 18.575), (9, 19)))
        self.add_bezier('sym-e11', (9, 19), ((7.945, 19.933), (6, 22.552), (6, 24)))
        self.add_bezier('sym-e12', (6, 24), ((6, 24.048), (6, 23.946), (6, 24)))
        self.add_bezier('sym-e13', (6, 24), ((6, 24.054), (6, 23.952), (6, 24)))
        self.add_bezier('sym-e14', (6, 24), ((6, 25.448), (7.945, 28.067), (9, 29)))
        self.add_bezier('sym-e15', (9, 29), ((9.483, 29.425), (9.435, 29.681), (10, 30)))
        self.add_bezier('sym-e16', (10, 30), ((8.257, 35.547), (12.42, 39.833), (18, 38)))
        self.add_bezier('sym-e17', (18, 38), ((19.184, 40.151), (21.395, 41.943), (24, 42)))
        self.add_bezier('sym-e18', (24, 42), ((26.605, 41.943), (28.816, 40.151), (30, 38)))
        self.add_bezier('sym-e19', (30, 38), ((35.58, 39.833), (39.743, 35.547), (38, 30)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
