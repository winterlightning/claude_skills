"""Shape peg top (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c11e411-398a-4857-9680-cf334bf7be9a'
SOURCE_PATH = 'icons-json/design/shape peg top_9c11e411-398a-4857-9680-cf334bf7be9a.json'
AUTHOR = 'json_to_solo'

class ShapePegTopDesign(Solo48):
    icon_id = 'shape-peg-top-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'peg', 'top', 'design')

    def build(self):
        self.add_line('e0', (40, 24), (24, 24))
        self.add_line('e1', (40, 24), (37, 29))
        self.add_line('e2', (37, 29), (26, 42))
        self.add_line('e3', (26, 42), (24, 44))
        self.add_line('e4', (39, 23), (24, 4))
        self.add_line('e5', (24, 44), (24, 39))
        self.add_line('e6', (24, 39), (24, 24))
        self.add_line('e7', (24, 44), (8, 24))
        self.add_line('e8', (8, 24), (24, 24))
        self.add_line('e9', (8, 24), (24, 4))
        self.add_line('e10', (24, 24), (24, 4))
        self.add_bezier('e11', (40, 24), ((39.722, 23.7), (39.261, 23.327), (39, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e11', 'e4')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('c7', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
