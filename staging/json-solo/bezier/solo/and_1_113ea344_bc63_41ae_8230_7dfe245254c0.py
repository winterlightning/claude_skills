"""And 1 (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '113ea344-bc63-41ae-8230-7dfe245254c0'
SOURCE_PATH = 'icons-json/_uncategorized_03/and 1_113ea344-bc63-41ae-8230-7dfe245254c0.json'
AUTHOR = 'json_to_solo'

class And1Uncategorized03(Solo48):
    icon_id = 'and-1-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('and', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (4, 16), (14, 16))
        self.add_line('e1', (4, 31), (14, 31))
        self.add_line('e2', (44, 24), (34, 24))
        self.add_line('e3', (14, 16), (14, 31))
        self.add_line('e4', (14, 16), (14, 8))
        self.add_line('e5', (14, 8), (21, 8))
        self.add_line('e6', (14, 31), (14, 40))
        self.add_line('e7', (14, 40), (21, 40))
        self.add_bezier('e8', (21, 8), ((22.136, 8), (23.682, 8.46), (24.745, 8.86)), ((30.564, 11.08), (33.845, 17.47), (34, 24)))
        self.add_bezier('e9', (21, 40), ((22.2, 40), (23.855, 39.49), (24.964, 39.02)), ((30.791, 36.56), (33.9, 30.69), (34, 24)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e8')
        self.add_contour('c5', 'e6', 'e7', 'e9')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
