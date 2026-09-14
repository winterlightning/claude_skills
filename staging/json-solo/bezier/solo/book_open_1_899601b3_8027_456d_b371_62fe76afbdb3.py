"""Book open 1 (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '899601b3-8027-456d-b371-62fe76afbdb3'
SOURCE_PATH = 'icons-json/content/book open 1_899601b3-8027-456d-b371-62fe76afbdb3.json'
AUTHOR = 'json_to_solo'

class BookOpen1(Solo48):
    icon_id = 'book-open-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 13), (24, 40))
        self.add_bezier('sym-e1', (24, 40), ((25.009, 39.377), (25.891, 38.505), (27, 38)))
        self.add_bezier('sym-e2', (27, 38), ((29.082, 37.065), (31.718, 37.236), (34, 37)))
        self.add_line('sym-e3', (34, 37), (42, 36))
        self.add_bezier('sym-e4', (42, 36), ((42.645, 35.688), (43.636, 35.632), (44, 35)))
        self.add_bezier('sym-e5', (44, 35), ((44, 34.84), (43.918, 34.152), (44, 34)))
        self.add_line('sym-e6', (44, 34), (44, 10))
        self.add_bezier('sym-e7', (44, 10), ((43.909, 9.832), (44, 9.177), (44, 9)))
        self.add_bezier('sym-e8', (44, 9), ((43.627, 8.394), (42.773, 8), (42, 8)))
        self.add_bezier('sym-e9', (42, 8), ((41.936, 8), (42.064, 8), (42, 8)))
        self.add_bezier('sym-e10', (42, 8), ((41.936, 8), (41.064, 8), (41, 8)))
        self.add_bezier('sym-e11', (41, 8), ((40.118, 8), (39.882, 8), (39, 8)))
        self.add_bezier('sym-e12', (39, 8), ((34.873, 8.143), (29.427, 8.684), (26, 11)))
        self.add_bezier('sym-e13', (26, 11), ((25.173, 11.556), (24.645, 12.259), (24, 13)))
        self.add_bezier('sym-e14', (24, 13), ((23.355, 12.259), (22.827, 11.556), (22, 11)))
        self.add_bezier('sym-e15', (22, 11), ((18.573, 8.684), (13.127, 8.143), (9, 8)))
        self.add_bezier('sym-e16', (9, 8), ((8.118, 8), (7.882, 8), (7, 8)))
        self.add_bezier('sym-e17', (7, 8), ((6.936, 8), (6.064, 8), (6, 8)))
        self.add_bezier('sym-e18', (6, 8), ((5.936, 8), (6.064, 8), (6, 8)))
        self.add_bezier('sym-e19', (6, 8), ((5.227, 8), (4.373, 8.394), (4, 9)))
        self.add_bezier('sym-e20', (4, 9), ((4, 9.177), (4.091, 9.832), (4, 10)))
        self.add_line('sym-e21', (4, 10), (4, 34))
        self.add_bezier('sym-e22', (4, 34), ((4.082, 34.152), (4, 34.84), (4, 35)))
        self.add_bezier('sym-e23', (4, 35), ((4.364, 35.632), (5.355, 35.688), (6, 36)))
        self.add_line('sym-e24', (6, 36), (14, 37))
        self.add_bezier('sym-e25', (14, 37), ((16.282, 37.236), (18.918, 37.065), (21, 38)))
        self.add_bezier('sym-e26', (21, 38), ((22.109, 38.505), (22.991, 39.377), (24, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
