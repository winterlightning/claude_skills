"""Trekking shelter (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88470bfe-b79f-53bc-a66c-39911133467b'
SOURCE_PATH = 'icons-json/outdoors/trekking shelter_88470bfe-b79f-53bc-a66c-39911133467b.json'
AUTHOR = 'json_to_solo'

class TrekkingShelterOutdoors(Solo48):
    icon_id = 'trekking-shelter-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('trekking', 'shelter', 'outdoors')

    def build(self):
        self.add_line('e0', (35, 42), (38, 42))
        self.add_line('e1', (38, 42), (38, 19))
        self.add_line('e2', (35, 42), (34, 40))
        self.add_line('e3', (34, 40), (26, 25))
        self.add_line('e4', (26, 25), (24, 22))
        self.add_line('e5', (24, 22), (22, 25))
        self.add_line('e6', (22, 25), (14, 40))
        self.add_line('e7', (14, 40), (13, 42))
        self.add_line('e8', (35, 42), (13, 42))
        self.add_line('e9', (6, 24), (10, 20))
        self.add_line('e10', (10, 20), (10, 22))
        self.add_line('e11', (42, 23), (38, 19))
        self.add_line('e12', (38, 19), (25, 6))
        self.add_line('e13', (23, 6), (10, 20))
        self.add_bezier('e14', (10, 22), ((9.984, 27.236), (10.124, 32.026), (10.058, 37.263)), ((10.042, 38.425), (10.017, 39.586), (9.993, 40.748)), ((9.985, 40.945), (9.886, 41.73), (9.968, 41.845)), ((10.042, 41.935), (10.647, 41.984), (10.827, 41.984)), ((11.089, 41.984), (11.343, 42), (11.605, 42)), ((12.194, 42), (12.411, 42), (13, 42)))
        self.add_bezier('e15', (25, 6), ((24.452, 6), (23.548, 6), (23, 6)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e9', 'e10', 'e14')
        self.add_contour('c4', 'e11')
        self.add_contour('c5', 'e12', 'e15', 'e13')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
