"""Material brick (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f74192f3-55c3-51b9-93e2-e900d8b1570c'
SOURCE_PATH = 'icons-json/construction/material brick_f74192f3-55c3-51b9-93e2-e900d8b1570c.json'
AUTHOR = 'json_to_solo'

class MaterialBrickConstruction(Solo48):
    icon_id = 'material-brick-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('material', 'brick', 'construction')

    def build(self):
        self.add_line('e0', (39, 29), (39, 40))
        self.add_line('e1', (39, 40), (9, 40))
        self.add_line('e2', (9, 40), (9, 29))
        self.add_line('e3', (24, 40), (24, 29))
        self.add_line('e4', (31, 29), (31, 19))
        self.add_line('e5', (17, 29), (17, 19))
        self.add_line('e6', (39, 19), (39, 8))
        self.add_line('e7', (39, 8), (9, 8))
        self.add_line('e8', (9, 8), (9, 19))
        self.add_line('e9', (24, 8), (24, 19))
        self.add_line('e10', (44, 29), (4, 29))
        self.add_line('e11', (4, 29), (4, 19))
        self.add_line('e12', (4, 19), (44, 19))
        self.add_line('e13', (44, 19), (44, 29))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7', 'e8')
        self.add_contour('c5', 'e9')
        self.add_contour('c6', 'e10', 'e11', 'e12', 'e13', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c4')
        self.relate('connect', 'c5', 'c6')
