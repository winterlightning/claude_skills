"""Shopping bag (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'icons-json/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.json'
AUTHOR = 'json_to_solo'

class ShoppingBag(Solo48):
    icon_id = 'shopping-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self):
        self.add_line('sym-e0', (16, 23), (16, 17))
        self.add_line('sym-e1', (16, 17), (13, 17))
        self.add_bezier('sym-e2', (13, 17), ((11.568, 17), (11.691, 17.773), (11, 19)))
        self.add_line('sym-e3', (11, 19), (8, 40))
        self.add_bezier('sym-e4', (8, 40), ((8, 40.082), (8, 40.918), (8, 41)))
        self.add_bezier('sym-e5', (8, 41), ((8, 42.2), (9.04, 43.427), (10, 44)))
        self.add_bezier('sym-e6', (10, 44), ((10.278, 44), (10.722, 43.9), (11, 44)))
        self.add_line('sym-e7', (11, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (37, 44))
        self.add_bezier('sym-e9', (37, 44), ((37.278, 43.9), (37.722, 44), (38, 44)))
        self.add_bezier('sym-e10', (38, 44), ((38.96, 43.427), (40, 42.2), (40, 41)))
        self.add_bezier('sym-e11', (40, 41), ((40, 40.918), (40, 40.082), (40, 40)))
        self.add_line('sym-e12', (40, 40), (37, 19))
        self.add_bezier('sym-e13', (37, 19), ((36.309, 17.773), (36.432, 17), (35, 17)))
        self.add_line('sym-e14', (35, 17), (32, 17))
        self.add_line('sym-e15', (32, 17), (32, 23))
        self.add_line('sym-e16', (16, 17), (24, 17))
        self.add_line('sym-e17', (24, 17), (32, 17))
        self.add_line('sym-e18', (32, 17), (32, 11))
        self.add_bezier('sym-e19', (32, 11), ((32, 6.855), (27.621, 4), (24, 4)))
        self.add_bezier('sym-e20', (24, 4), ((23.983, 4), (24.017, 4), (24, 4)))
        self.add_bezier('sym-e21', (24, 4), ((23.992, 4), (24.008, 4), (24, 4)))
        self.add_bezier('sym-e22', (24, 4), ((23.992, 4), (24.008, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((23.983, 4), (24.017, 4), (24, 4)))
        self.add_bezier('sym-e24', (24, 4), ((20.379, 4), (16, 6.855), (16, 11)))
        self.add_line('sym-e25', (16, 11), (16, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
