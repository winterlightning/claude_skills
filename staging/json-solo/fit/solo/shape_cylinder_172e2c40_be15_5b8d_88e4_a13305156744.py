"""Shape cylinder (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '172e2c40-be15-5b8d-88e4-a13305156744'
SOURCE_PATH = 'icons-json/design/shape cylinder_172e2c40-be15-5b8d-88e4-a13305156744.json'
AUTHOR = 'json_to_solo'

class ShapeCylinderDesign(Solo48):
    icon_id = 'shape-cylinder-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'cylinder', 'design')

    def build(self):
        self.add_line('sym-e1-1', (24, 44), (15, 43))
        self.add_arc('sym-e1-2', (15, 43), (8, 39), radius_x=10)
        self.add_line('sym-e3', (8, 39), (8, 10))
        self.add_line('sym-e4', (8, 10), (8, 11))
        self.add_line('sym-e5', (8, 11), (10, 12))
        self.add_arc('sym-e6', (10, 12), (16, 14), radius_x=18)
        self.add_arc('sym-e7', (16, 14), (24, 14), radius_x=44, sweep=False)
        self.add_arc('sym-e8', (24, 14), (32, 14), radius_x=45, sweep=False)
        self.add_arc('sym-e9', (32, 14), (38, 12), radius_x=18)
        self.add_line('sym-e10', (38, 12), (40, 11))
        self.add_line('sym-e11', (40, 11), (40, 10))
        self.add_line('sym-e12', (40, 10), (40, 39))
        self.add_arc('sym-e14-1', (40, 39), (33, 43), radius_x=10)
        self.add_line('sym-e14-2', (33, 43), (24, 44))
        self.add_line('sym-e16', (8, 10), (8, 9))
        self.add_arc('sym-e17', (8, 9), (11, 6), radius_x=4)
        self.add_line('sym-e18', (11, 6), (22, 4))
        self.add_line('sym-e19', (22, 4), (24, 4))
        self.add_line('sym-e22', (24, 4), (26, 4))
        self.add_line('sym-e23', (26, 4), (37, 6))
        self.add_arc('sym-e24', (37, 6), (40, 9), radius_x=4)
        self.add_line('sym-e25', (40, 9), (40, 10))
        self.add_contour('sym-c0', 'sym-e1-1', 'sym-e1-2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14-1', 'sym-e14-2', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
