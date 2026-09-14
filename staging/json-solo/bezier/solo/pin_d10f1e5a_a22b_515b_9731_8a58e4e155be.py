"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd10f1e5a-a22b-515b-9731-8a58e4e155be'
SOURCE_PATH = 'icons-json/interface-essential/pin_d10f1e5a-a22b-515b-9731-8a58e4e155be.json'
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
        self.add_line('sym-e0', (9, 42), (14, 42))
        self.add_line('sym-e1', (14, 42), (24, 44))
        self.add_line('sym-e2', (24, 44), (34, 42))
        self.add_line('sym-e3', (34, 42), (39, 42))
        self.add_bezier('sym-e4', (24, 39), ((22.043, 37.164), (20.748, 34.945), (19, 33)))
        self.add_bezier('sym-e5', (19, 33), ((16.674, 30.418), (14.055, 27.709), (12, 25)))
        self.add_bezier('sym-e6', (12, 25), ((10.129, 22.536), (8, 19.918), (8, 17)))
        self.add_bezier('sym-e7', (8, 17), ((8, 16.855), (8, 16.136), (8, 16)))
        self.add_bezier('sym-e8', (8, 16), ((8, 15.791), (8, 16.209), (8, 16)))
        self.add_bezier('sym-e9', (8, 16), ((8, 10.091), (14.828, 4), (23, 4)))
        self.add_bezier('sym-e10', (23, 4), ((23.185, 4), (23.815, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.041, 4), (23.959, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((24.041, 4), (23.959, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((24.185, 4), (24.815, 4), (25, 4)))
        self.add_bezier('sym-e14', (25, 4), ((33.172, 4), (40, 10.091), (40, 16)))
        self.add_bezier('sym-e15', (40, 16), ((40, 16.209), (40, 15.791), (40, 16)))
        self.add_bezier('sym-e16', (40, 16), ((40, 16.136), (40, 16.855), (40, 17)))
        self.add_bezier('sym-e17', (40, 17), ((40, 19.918), (37.871, 22.536), (36, 25)))
        self.add_bezier('sym-e18', (36, 25), ((33.945, 27.709), (31.326, 30.418), (29, 33)))
        self.add_bezier('sym-e19', (29, 33), ((27.252, 34.945), (25.957, 37.164), (24, 39)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
