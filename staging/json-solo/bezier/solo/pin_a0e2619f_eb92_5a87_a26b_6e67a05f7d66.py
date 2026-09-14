"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e2619f-eb92-5a87-a26b-6e67a05f7d66'
SOURCE_PATH = 'icons-json/interface-essential/pin_a0e2619f-eb92-5a87-a26b-6e67a05f7d66.json'
AUTHOR = 'json_to_solo'

class Pin(Solo48):
    icon_id = 'pin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_bezier('sym-e2', (24, 44), ((19.56, 39.073), (15.44, 33.573), (12, 28)))
        self.add_bezier('sym-e3', (12, 28), ((10.18, 25.045), (8, 22.464), (8, 19)))
        self.add_bezier('sym-e4', (8, 19), ((8, 18.773), (8, 18.227), (8, 18)))
        self.add_bezier('sym-e5', (8, 18), ((8, 17.773), (8, 17.227), (8, 17)))
        self.add_bezier('sym-e6', (8, 17), ((8, 10.136), (15.56, 4), (23, 4)))
        self.add_bezier('sym-e7', (23, 4), ((23.24, 4), (23.76, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.06, 4), (23.94, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.06, 4), (23.94, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.24, 4), (24.76, 4), (25, 4)))
        self.add_bezier('sym-e11', (25, 4), ((32.44, 4), (40, 10.136), (40, 17)))
        self.add_bezier('sym-e12', (40, 17), ((40, 17.227), (40, 17.773), (40, 18)))
        self.add_bezier('sym-e13', (40, 18), ((40, 18.227), (40, 18.773), (40, 19)))
        self.add_bezier('sym-e14', (40, 19), ((40, 22.464), (37.82, 25.045), (36, 28)))
        self.add_bezier('sym-e15', (36, 28), ((32.56, 33.573), (28.44, 39.073), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
