"""Dumbbell (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'icons-json/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.json'
AUTHOR = 'json_to_solo'

class DumbbellC7617317(Solo48):
    icon_id = 'dumbbell-c7617317'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('dumbbell', 'sports')

    def build(self):
        self.add_line('e0', (35, 24), (13, 24))
        self.add_line('e1', (4, 38), (4, 10))
        self.add_line('e2', (5, 8), (12, 8))
        self.add_line('e3', (13, 10), (13, 38))
        self.add_line('e4', (12, 40), (5, 40))
        self.add_line('e5', (36, 8), (43, 8))
        self.add_line('e6', (44, 10), (44, 38))
        self.add_line('e7', (43, 40), (36, 40))
        self.add_line('e8', (35, 38), (35, 10))
        self.add_bezier('e9', (4, 10), ((4, 9.893), (4, 9.564), (4, 9.476)), ((4, 8.356), (4.664, 8.373), (5, 8)))
        self.add_bezier('e10', (12, 8), ((12.364, 8.409), (12.864, 8.231), (13.055, 9.173)), ((13.064, 9.369), (12.991, 9.804), (13, 10)))
        self.add_bezier('e11', (13, 38), ((12.991, 38.196), (13.064, 38.631), (13.055, 38.827)), ((12.864, 39.769), (12.364, 39.591), (12, 40)))
        self.add_bezier('e12', (5, 40), ((4.664, 39.627), (4, 39.644), (4, 38.524)), ((4, 38.436), (4, 38.107), (4, 38)))
        self.add_bezier('e13', (43, 8), ((43.336, 8.373), (44, 8.356), (44, 9.476)), ((44, 9.564), (44, 9.893), (44, 10)))
        self.add_bezier('e14', (44, 38), ((44, 38.107), (44, 38.436), (44, 38.524)), ((44, 39.644), (43.336, 39.627), (43, 40)))
        self.add_bezier('e15', (36, 40), ((35.636, 39.591), (35.136, 39.769), (34.945, 38.827)), ((34.936, 38.631), (35.009, 38.196), (35, 38)))
        self.add_bezier('e16', (35, 10), ((35.009, 9.804), (34.936, 9.369), (34.945, 9.173)), ((35.136, 8.231), (35.636, 8.409), (36, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', closed=True)
        self.add_contour('c2', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
