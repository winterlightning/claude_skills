"""Arrow (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5762ca4d-99c2-4016-910c-36aa0e18889f'
SOURCE_PATH = 'icons-json/wayfinding/arrow_5762ca4d-99c2-4016-910c-36aa0e18889f.json'
AUTHOR = 'json_to_solo'

class Arrow5762ca4d(Solo48):
    icon_id = 'arrow-5762ca4d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('arrow', 'wayfinding')

    def build(self):
        self.add_line('e0', (25, 8), (33, 8))
        self.add_line('e1', (36, 31), (4, 31))
        self.add_line('e2', (13, 21), (4, 31))
        self.add_line('e3', (13, 40), (4, 31))
        self.add_bezier('e4', (33, 8), ((33.709, 8), (34.627, 8.28), (35.309, 8.51)), ((39.764, 9.98), (43.991, 14.56), (43.991, 19.96)), ((43.991, 20.039), (44, 20.108), (44, 20.186)), ((44, 20.188), (44, 20.189), (44, 20.19)), ((44, 20.46), (43.991, 20.72), (43.991, 20.99)), ((43.991, 25.63), (40.455, 31), (36, 31)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
