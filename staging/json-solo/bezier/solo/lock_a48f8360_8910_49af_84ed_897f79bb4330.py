"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a48f8360-8910-49af-84ed-897f79bb4330'
SOURCE_PATH = 'icons-json/interface-essential/lock_a48f8360-8910-49af-84ed-897f79bb4330.json'
AUTHOR = 'json_to_solo'

class Lock(Solo48):
    icon_id = 'lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (24, 4), ((23.797, 4), (23.203, 4), (23, 4)))
        self.add_bezier('sym-e1', (23, 4), ((17.14, 4), (13, 8.864), (13, 14)))
        self.add_line('sym-e2', (13, 14), (13, 20))
        self.add_line('sym-e3', (13, 20), (24, 20))
        self.add_line('sym-e4', (24, 20), (35, 20))
        self.add_line('sym-e5', (35, 20), (35, 14))
        self.add_bezier('sym-e6', (35, 14), ((35, 8.864), (30.86, 4), (25, 4)))
        self.add_bezier('sym-e7', (25, 4), ((24.797, 4), (24.203, 4), (24, 4)))
        self.add_line('sym-e8', (24, 44), (13, 44))
        self.add_bezier('sym-e9', (13, 44), ((12.92, 44), (13.08, 44), (13, 44)))
        self.add_bezier('sym-e10', (13, 44), ((9.92, 44), (8, 41.418), (8, 39)))
        self.add_bezier('sym-e11', (8, 39), ((8, 38.682), (8, 38.318), (8, 38)))
        self.add_line('sym-e12', (8, 38), (8, 23))
        self.add_bezier('sym-e13', (8, 23), ((8, 20.527), (10.935, 20), (13, 20)))
        self.add_bezier('sym-e14', (13, 20), ((13.084, 20), (12.919, 19.999), (13, 20)))
        self.add_bezier('sym-e15', (13, 20), ((13, 20), (13, 20), (13, 20)))
        self.add_line('sym-e16', (24, 44), (35, 44))
        self.add_bezier('sym-e17', (35, 44), ((35.08, 44), (34.92, 44), (35, 44)))
        self.add_bezier('sym-e18', (35, 44), ((38.08, 44), (40, 41.418), (40, 39)))
        self.add_bezier('sym-e19', (40, 39), ((40, 38.682), (40, 38.318), (40, 38)))
        self.add_line('sym-e20', (40, 38), (40, 23))
        self.add_bezier('sym-e21', (40, 23), ((40, 20.527), (37.065, 20), (35, 20)))
        self.add_bezier('sym-e22', (35, 20), ((34.916, 20), (35.081, 19.999), (35, 20)))
        self.add_bezier('sym-e23', (35, 20), ((35, 20), (35, 20), (35, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c2', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
