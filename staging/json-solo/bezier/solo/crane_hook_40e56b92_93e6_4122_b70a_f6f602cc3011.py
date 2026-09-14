"""Crane hook (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40e56b92-93e6-4122-b70a-f6f602cc3011'
SOURCE_PATH = 'icons-json/shipping/crane hook_40e56b92-93e6-4122-b70a-f6f602cc3011.json'
AUTHOR = 'json_to_solo'

class CraneHookShipping(Solo48):
    icon_id = 'crane-hook-shipping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('crane', 'hook', 'shipping')

    def build(self):
        self.add_line('e0', (24, 30), (24, 27))
        self.add_line('e1', (40, 6), (40, 16))
        self.add_line('e2', (40, 17), (32, 26))
        self.add_line('e3', (29, 27), (24, 27))
        self.add_line('e4', (24, 27), (19, 27))
        self.add_line('e5', (16, 26), (12, 21))
        self.add_line('e6', (37, 4), (11, 4))
        self.add_line('e7', (8, 6), (8, 16))
        self.add_line('e8', (8, 17), (12, 21))
        self.add_line('e9', (12, 21), (37, 4))
        self.add_bezier('e10', (33, 38), ((32.987, 38.673), (33.347, 38.973), (33.053, 39.618)), ((31.973, 42.045), (28.253, 43.982), (24.48, 43.982)), ((24.32, 43.982), (24.147, 44), (23.987, 44)), ((23.982, 44), (23.978, 44), (23.974, 44)), ((23.712, 44), (23.449, 43.991), (23.187, 43.991)), ((15.867, 43.991), (12.373, 38.027), (16.867, 34.2)), ((17.773, 33.418), (18.987, 32.727), (20.333, 32.318)), ((21.307, 32.018), (22.4, 31.855), (23.2, 31.327)), ((23.627, 31.045), (23.733, 30.336), (24, 30)))
        self.add_bezier('e11', (37, 4), ((38.72, 4.655), (39.2, 4.836), (40, 6)))
        self.add_bezier('e12', (40, 16), ((40, 16.3), (40, 16.7), (40, 17)))
        self.add_bezier('e13', (32, 26), ((31.08, 26.455), (30.107, 26.782), (29, 27)))
        self.add_bezier('e14', (19, 27), ((17.92, 26.773), (16.907, 26.455), (16, 26)))
        self.add_bezier('e15', (11, 4), ((10.733, 4.1), (10.107, 4.073), (9.84, 4.173)), ((8.827, 4.582), (8.48, 5.345), (8, 6)))
        self.add_bezier('e16', (8, 16), ((8, 16.3), (8, 16.7), (8, 17)))
        self.add_contour('c0', 'e10', 'e0')
        self.add_contour('c1', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5')
        self.add_contour('c3', 'e6', 'e15', 'e7', 'e16', 'e8', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
