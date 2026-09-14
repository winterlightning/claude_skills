"""Trash can (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0702c6a-8d52-4871-82ba-3206aeb5703e'
SOURCE_PATH = 'icons-json/symbol/trash can_f0702c6a-8d52-4871-82ba-3206aeb5703e.json'
AUTHOR = 'json_to_solo'

class TrashCan(Solo48):
    icon_id = 'trash-can'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'can', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 18), (11, 18))
        self.add_line('sym-e1', (11, 18), (13, 41))
        self.add_bezier('sym-e2', (13, 41), ((13.589, 42.382), (14.442, 44), (16, 44)))
        self.add_line('sym-e3', (16, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (32, 44))
        self.add_bezier('sym-e5', (32, 44), ((33.558, 44), (34.411, 42.382), (35, 41)))
        self.add_line('sym-e6', (35, 41), (37, 18))
        self.add_line('sym-e7', (37, 18), (24, 18))
        self.add_line('sym-e8', (9, 18), (11, 18))
        self.add_bezier('sym-e9', (9, 18), ((8.722, 18), (8.278, 18), (8, 18)))
        self.add_line('sym-e10', (8, 18), (8, 12))
        self.add_bezier('sym-e11', (8, 12), ((8.573, 10.991), (9.779, 10), (11, 10)))
        self.add_line('sym-e12', (11, 10), (18, 10))
        self.add_line('sym-e13', (18, 10), (18, 7))
        self.add_bezier('sym-e14', (18, 7), ((18, 5.682), (19.074, 4.673), (20, 4)))
        self.add_line('sym-e15', (20, 4), (24, 4))
        self.add_line('sym-e16', (24, 4), (28, 4))
        self.add_bezier('sym-e17', (28, 4), ((28.926, 4.673), (30, 5.682), (30, 7)))
        self.add_line('sym-e18', (30, 7), (30, 10))
        self.add_line('sym-e19', (30, 10), (37, 10))
        self.add_bezier('sym-e20', (37, 10), ((38.221, 10), (39.427, 10.991), (40, 12)))
        self.add_line('sym-e21', (40, 12), (40, 18))
        self.add_bezier('sym-e22', (40, 18), ((39.722, 18), (39.278, 18), (39, 18)))
        self.add_line('sym-e23', (39, 18), (37, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c1', 'sym-c2')
