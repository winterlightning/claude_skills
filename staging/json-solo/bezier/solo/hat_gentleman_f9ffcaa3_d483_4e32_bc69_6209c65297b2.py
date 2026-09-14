"""Batch-06/hat gentleman (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9ffcaa3-d483-4e32-bc69-6209c65297b2'
SOURCE_PATH = 'icons-json/accessories/batch-06/hat gentleman_f9ffcaa3-d483-4e32-bc69-6209c65297b2.json'
AUTHOR = 'json_to_solo'

class Batch06HatGentleman(Solo48):
    icon_id = 'batch-06-hat-gentleman'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'gentleman', 'accessories')

    def build(self):
        self.add_line('sym-e0', (38, 40), (10, 40))
        self.add_bezier('sym-e1', (10, 40), ((9.936, 39.99), (10.064, 40), (10, 40)))
        self.add_bezier('sym-e2', (10, 40), ((9.964, 40), (10.045, 40), (10, 40)))
        self.add_bezier('sym-e3', (10, 40), ((9.9, 40), (10.1, 40), (10, 40)))
        self.add_bezier('sym-e4', (10, 40), ((6.855, 40), (4, 36.22), (4, 33)))
        self.add_bezier('sym-e5', (4, 33), ((4, 32.72), (4, 32.28), (4, 32)))
        self.add_line('sym-e6', (10, 32), (38, 32))
        self.add_line('sym-e7', (38, 32), (38, 40))
        self.add_bezier('sym-e8', (38, 40), ((38.064, 39.99), (37.936, 40), (38, 40)))
        self.add_bezier('sym-e9', (38, 40), ((38.036, 40), (37.955, 40), (38, 40)))
        self.add_bezier('sym-e10', (38, 40), ((38.1, 40), (37.9, 40), (38, 40)))
        self.add_bezier('sym-e11', (38, 40), ((41.145, 40), (44, 36.22), (44, 33)))
        self.add_bezier('sym-e12', (44, 33), ((44, 32.72), (44, 32.28), (44, 32)))
        self.add_line('sym-e13', (10, 40), (10, 32))
        self.add_line('sym-e14', (10, 32), (10, 22))
        self.add_bezier('sym-e15', (10, 22), ((10, 20.9), (10.7, 20.04), (11, 19)))
        self.add_bezier('sym-e16', (11, 19), ((12.673, 13.21), (17.273, 8), (23, 8)))
        self.add_bezier('sym-e17', (23, 8), ((23.127, 8), (23.873, 8.01), (24, 8)))
        self.add_bezier('sym-e18', (24, 8), ((24.122, 8), (23.879, 8), (24, 8)))
        self.add_bezier('sym-e19', (24, 8), ((24.121, 8), (23.878, 8), (24, 8)))
        self.add_bezier('sym-e20', (24, 8), ((24.127, 8.01), (24.873, 8), (25, 8)))
        self.add_bezier('sym-e21', (25, 8), ((30.727, 8), (35.327, 13.21), (37, 19)))
        self.add_bezier('sym-e22', (37, 19), ((37.3, 20.04), (38, 20.9), (38, 22)))
        self.add_line('sym-e23', (38, 22), (38, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
