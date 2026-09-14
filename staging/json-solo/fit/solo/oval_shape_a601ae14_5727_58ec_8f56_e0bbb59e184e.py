"""Oval shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a601ae14-5727-58ec-8f56-e0bbb59e184e'
SOURCE_PATH = 'icons-json/design/oval shape_a601ae14-5727-58ec-8f56-e0bbb59e184e.json'
AUTHOR = 'json_to_solo'

class OvalShapeDesign(Solo48):
    icon_id = 'oval-shape-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('oval', 'shape', 'design')

    def build(self):
        self.add_arc('sym-e1', (4, 24), (18, 9), radius_x=17)
        self.add_line('sym-e2', (18, 9), (22, 8))
        self.add_line('sym-e3', (22, 8), (24, 8))
        self.add_line('sym-e8', (24, 8), (26, 8))
        self.add_line('sym-e9', (26, 8), (30, 9))
        self.add_arc('sym-e10', (30, 9), (44, 24), radius_x=17)
        self.add_arc('sym-e13', (44, 24), (30, 39), radius_x=16)
        self.add_line('sym-e14', (30, 39), (26, 40))
        self.add_line('sym-e15', (26, 40), (24, 40))
        self.add_line('sym-e20', (24, 40), (22, 40))
        self.add_line('sym-e21', (22, 40), (18, 39))
        self.add_arc('sym-e22', (18, 39), (4, 24), radius_x=16)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
