"""Bone (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdd6c205-c49b-4436-8ff7-3c7c0b842d86'
SOURCE_PATH = 'icons-json/symbol/bone_bdd6c205-c49b-4436-8ff7-3c7c0b842d86.json'
AUTHOR = 'json_to_solo'

class BoneSymbol(Solo48):
    icon_id = 'bone-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bone', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (42, 24), ((41.988, 24.023), (41, 23.994), (41, 24)))
        self.add_bezier('sym-e1', (41, 24), ((41, 24.145), (42.7, 25.418), (43, 26)))
        self.add_bezier('sym-e2', (43, 26), ((43.709, 27.367), (44, 29.211), (44, 31)))
        self.add_bezier('sym-e3', (44, 31), ((44, 35.524), (41.918, 40), (39, 40)))
        self.add_bezier('sym-e4', (39, 40), ((38.827, 40), (38.173, 40), (38, 40)))
        self.add_bezier('sym-e5', (38, 40), ((37.909, 40), (38.082, 40), (38, 40)))
        self.add_bezier('sym-e6', (38, 40), ((36.045, 40), (33.873, 37.749), (33, 35)))
        self.add_bezier('sym-e7', (33, 35), ((32.618, 33.778), (32.318, 32.265), (32, 31)))
        self.add_line('sym-e8', (32, 31), (16, 31))
        self.add_bezier('sym-e9', (16, 31), ((15.755, 32.12), (15.3, 33.924), (15, 35)))
        self.add_bezier('sym-e10', (15, 35), ((14.173, 37.953), (12.036, 40), (10, 40)))
        self.add_bezier('sym-e11', (10, 40), ((9.936, 40), (10.064, 39.985), (10, 40)))
        self.add_bezier('sym-e12', (10, 40), ((9.836, 40), (9.164, 40), (9, 40)))
        self.add_bezier('sym-e13', (9, 40), ((6.291, 40), (4, 36.451), (4, 32)))
        self.add_bezier('sym-e14', (4, 32), ((4, 31.956), (4, 32.044), (4, 32)))
        self.add_bezier('sym-e15', (4, 32), ((4, 31.738), (4, 31.262), (4, 31)))
        self.add_bezier('sym-e16', (4, 31), ((4, 29.225), (4.245, 27.265), (5, 26)))
        self.add_bezier('sym-e17', (5, 26), ((5.273, 25.549), (7, 24.044), (7, 24)))
        self.add_bezier('sym-e18', (7, 24), ((6.99, 23.985), (7.01, 24.015), (7, 24)))
        self.add_bezier('sym-e19', (7, 24), ((7.01, 23.985), (6.99, 24.015), (7, 24)))
        self.add_bezier('sym-e20', (7, 24), ((7, 23.956), (5.273, 22.451), (5, 22)))
        self.add_bezier('sym-e21', (5, 22), ((4.245, 20.735), (4, 18.775), (4, 17)))
        self.add_bezier('sym-e22', (4, 17), ((4, 16.738), (4, 16.262), (4, 16)))
        self.add_bezier('sym-e23', (4, 16), ((4, 15.956), (4, 16.044), (4, 16)))
        self.add_bezier('sym-e24', (4, 16), ((4, 11.549), (6.291, 8), (9, 8)))
        self.add_bezier('sym-e25', (9, 8), ((9.164, 8), (9.836, 8), (10, 8)))
        self.add_bezier('sym-e26', (10, 8), ((10.064, 8.015), (9.936, 8), (10, 8)))
        self.add_bezier('sym-e27', (10, 8), ((12.036, 8), (14.173, 10.047), (15, 13)))
        self.add_bezier('sym-e28', (15, 13), ((15.3, 14.076), (15.755, 15.88), (16, 17)))
        self.add_line('sym-e29', (16, 17), (32, 17))
        self.add_bezier('sym-e30', (32, 17), ((32.318, 15.735), (32.618, 14.222), (33, 13)))
        self.add_bezier('sym-e31', (33, 13), ((33.873, 10.251), (36.045, 8), (38, 8)))
        self.add_bezier('sym-e32', (38, 8), ((38.082, 8), (37.909, 8), (38, 8)))
        self.add_bezier('sym-e33', (38, 8), ((38.173, 8), (38.827, 8), (39, 8)))
        self.add_bezier('sym-e34', (39, 8), ((41.918, 8), (44, 12.476), (44, 17)))
        self.add_bezier('sym-e35', (44, 17), ((44, 18.789), (43.709, 20.633), (43, 22)))
        self.add_bezier('sym-e36', (43, 22), ((42.7, 22.582), (41, 23.855), (41, 24)))
        self.add_bezier('sym-e37', (41, 24), ((41, 24.006), (41.988, 23.977), (42, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', closed=True)
