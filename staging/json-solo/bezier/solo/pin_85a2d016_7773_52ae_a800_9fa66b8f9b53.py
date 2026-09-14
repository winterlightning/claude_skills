"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85a2d016-7773-52ae-a800-9fa66b8f9b53'
SOURCE_PATH = 'icons-json/interface-essential/pin_85a2d016-7773-52ae-a800-9fa66b8f9b53.json'
AUTHOR = 'json_to_solo'

class Pin85a2d016(Solo48):
    icon_id = 'pin-85a2d016'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 18), (30, 18), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 18), (18, 18), radius_x=6, radius_y=5)
        self.add_bezier('sym-e2', (24, 44), ((19.64, 38.773), (15.62, 33.682), (12, 28)))
        self.add_bezier('sym-e3', (12, 28), ((10.33, 25.382), (8, 21.109), (8, 18)))
        self.add_bezier('sym-e4', (8, 18), ((8, 17.709), (8, 18.291), (8, 18)))
        self.add_bezier('sym-e5', (8, 18), ((8, 17.709), (8, 17.291), (8, 17)))
        self.add_bezier('sym-e6', (8, 17), ((8, 16.164), (8.77, 14.8), (9, 14)))
        self.add_bezier('sym-e7', (9, 14), ((10.67, 8.091), (16.33, 4), (23, 4)))
        self.add_bezier('sym-e8', (23, 4), ((23.227, 4), (23.773, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.227, 4), (24.773, 4), (25, 4)))
        self.add_bezier('sym-e10', (25, 4), ((31.67, 4), (37.33, 8.091), (39, 14)))
        self.add_bezier('sym-e11', (39, 14), ((39.23, 14.8), (40, 16.164), (40, 17)))
        self.add_bezier('sym-e12', (40, 17), ((40, 17.291), (40, 17.709), (40, 18)))
        self.add_bezier('sym-e13', (40, 18), ((40, 18.291), (40, 17.709), (40, 18)))
        self.add_bezier('sym-e14', (40, 18), ((40, 21.109), (37.67, 25.382), (36, 28)))
        self.add_bezier('sym-e15', (36, 28), ((32.38, 33.682), (28.36, 38.773), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
