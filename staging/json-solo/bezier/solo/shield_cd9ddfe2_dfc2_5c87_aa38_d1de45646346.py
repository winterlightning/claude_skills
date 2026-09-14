"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9ddfe2-dfc2-5c87-aa38-d1de45646346'
SOURCE_PATH = 'icons-json/protection/shield_cd9ddfe2-dfc2-5c87-aa38-d1de45646346.json'
AUTHOR = 'json_to_solo'

class Shield(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('sym-e0', (8, 9), (8, 23))
        self.add_bezier('sym-e1', (8, 23), ((8, 23.2), (8, 23.8), (8, 24)))
        self.add_bezier('sym-e2', (8, 24), ((8, 29.582), (10.126, 34.382), (14, 38)))
        self.add_bezier('sym-e3', (14, 38), ((15.112, 39.036), (16.762, 40.136), (18, 41)))
        self.add_bezier('sym-e4', (18, 41), ((19.339, 41.936), (22.383, 44), (24, 44)))
        self.add_bezier('sym-e5', (24, 44), ((24.029, 44), (23.973, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((24.027, 44), (23.971, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((25.617, 44), (28.661, 41.936), (30, 41)))
        self.add_bezier('sym-e8', (30, 41), ((31.238, 40.136), (32.888, 39.036), (34, 38)))
        self.add_bezier('sym-e9', (34, 38), ((37.874, 34.382), (40, 29.582), (40, 24)))
        self.add_bezier('sym-e10', (40, 24), ((40, 23.8), (40, 23.2), (40, 23)))
        self.add_line('sym-e11', (40, 23), (40, 9))
        self.add_bezier('sym-e12', (40, 9), ((39.891, 8.818), (40, 8.173), (40, 8)))
        self.add_bezier('sym-e13', (40, 8), ((39.309, 7.055), (37.027, 6.336), (36, 6)))
        self.add_bezier('sym-e14', (36, 6), ((32.573, 4.891), (28.596, 4), (25, 4)))
        self.add_bezier('sym-e15', (25, 4), ((24.672, 4), (24.328, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.997, 4), (24.003, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((23.997, 4), (24.003, 4), (24, 4)))
        self.add_bezier('sym-e18', (24, 4), ((23.672, 4), (23.328, 4), (23, 4)))
        self.add_bezier('sym-e19', (23, 4), ((19.404, 4), (15.427, 4.891), (12, 6)))
        self.add_bezier('sym-e20', (12, 6), ((10.973, 6.336), (8.691, 7.055), (8, 8)))
        self.add_bezier('sym-e21', (8, 8), ((8, 8.173), (8.109, 8.818), (8, 9)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
