"""Tank top female (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21d58f2e-6689-5795-8249-4a28fef84464'
SOURCE_PATH = 'icons-json/clothes/tank top female_21d58f2e-6689-5795-8249-4a28fef84464.json'
AUTHOR = 'json_to_solo'

class TankTopFemaleClothes(Solo48):
    icon_id = 'tank-top-female-clothes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('tank', 'top', 'female', 'clothes')

    def build(self):
        self.add_line('e0', (32, 4), (34, 4))
        self.add_line('e1', (40, 18), (38, 29))
        self.add_line('e2', (38, 33), (39, 39))
        self.add_line('e3', (27, 44), (22, 44))
        self.add_line('e4', (8, 41), (9, 36))
        self.add_line('e5', (10, 25), (8, 18))
        self.add_line('e6', (13, 11), (14, 4))
        self.add_line('e7', (14, 4), (16, 4))
        self.add_bezier('e8', (24, 19), ((28.48, 14.718), (31.21, 9.955), (32, 4)))
        self.add_bezier('e9', (34, 4), ((34.42, 9.382), (35.44, 14.236), (40, 18)))
        self.add_bezier('e10', (38, 29), ((37.73, 30.482), (37.73, 31.518), (38, 33)))
        self.add_bezier('e11', (39, 39), ((39.09, 39.509), (39.18, 39.564), (39.38, 40.055)), ((39.56, 40.5), (39.98, 41.055), (39.98, 41.545)), ((39.99, 41.591), (39.99, 41.627), (40, 41.664)), ((39.92, 41.691), (39.85, 41.727), (39.77, 41.764)), ((38.91, 42.136), (37.98, 42.409), (37.05, 42.627)), ((33.94, 43.345), (30.67, 43.982), (27.43, 43.982)), ((27.29, 43.991), (27.14, 43.991), (27, 44)))
        self.add_bezier('e12', (22, 44), ((21.83, 43.991), (21.67, 43.991), (21.5, 43.982)), ((17.55, 43.982), (11.47, 42.673), (8, 41)))
        self.add_bezier('e13', (9, 36), ((9.73, 32.045), (11.13, 29.118), (10, 25)))
        self.add_bezier('e14', (8, 18), ((10.05, 16.409), (12.64, 13.591), (13, 11)))
        self.add_bezier('e15', (16, 4), ((16.81, 9.818), (19.41, 14.891), (24, 19)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', 'e7', 'e15')
