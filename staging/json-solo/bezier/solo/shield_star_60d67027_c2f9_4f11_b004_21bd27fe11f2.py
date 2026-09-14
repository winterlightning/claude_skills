"""Shield star (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = 'icons-json/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.json'
AUTHOR = 'json_to_solo'

class ShieldStarProtection(Solo48):
    icon_id = 'shield-star-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'star', 'protection')

    def build(self):
        self.add_line('sym-e0', (18, 30), (20, 24))
        self.add_line('sym-e1', (20, 24), (15, 19))
        self.add_line('sym-e2', (15, 19), (21, 19))
        self.add_line('sym-e3', (21, 19), (24, 11))
        self.add_line('sym-e4', (24, 11), (27, 19))
        self.add_line('sym-e5', (27, 19), (33, 19))
        self.add_line('sym-e6', (33, 19), (28, 24))
        self.add_line('sym-e7', (28, 24), (30, 30))
        self.add_line('sym-e8', (30, 30), (24, 27))
        self.add_line('sym-e9', (24, 27), (18, 30))
        self.add_bezier('sym-e10', (40, 8), ((39.453, 7.609), (38.648, 7.173), (38, 7)))
        self.add_line('sym-e11', (38, 7), (32, 5))
        self.add_bezier('sym-e12', (32, 5), ((30.358, 4.555), (27.684, 4), (26, 4)))
        self.add_bezier('sym-e13', (26, 4), ((25.806, 4), (25.194, 4), (25, 4)))
        self.add_bezier('sym-e14', (25, 4), ((24.857, 4), (25.143, 4), (25, 4)))
        self.add_bezier('sym-e15', (25, 4), ((24.719, 4), (24.286, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.714, 4), (23.281, 4), (23, 4)))
        self.add_bezier('sym-e17', (23, 4), ((22.857, 4), (23.143, 4), (23, 4)))
        self.add_bezier('sym-e18', (23, 4), ((22.806, 4), (22.194, 4), (22, 4)))
        self.add_bezier('sym-e19', (22, 4), ((20.316, 4), (17.642, 4.555), (16, 5)))
        self.add_line('sym-e20', (16, 5), (10, 7))
        self.add_bezier('sym-e21', (10, 7), ((9.352, 7.173), (8.547, 7.609), (8, 8)))
        self.add_line('sym-e22', (8, 8), (8, 26))
        self.add_bezier('sym-e23', (8, 26), ((8, 26.045), (8, 25.955), (8, 26)))
        self.add_bezier('sym-e24', (8, 26), ((8, 27.118), (8.688, 27.945), (9, 29)))
        self.add_bezier('sym-e25', (9, 29), ((10.6, 34.318), (14.562, 39.309), (19, 42)))
        self.add_bezier('sym-e26', (19, 42), ((20.347, 42.818), (22.476, 44), (24, 44)))
        self.add_bezier('sym-e27', (24, 44), ((24.087, 44), (23.913, 44), (24, 44)))
        self.add_bezier('sym-e28', (24, 44), ((24.087, 44), (23.913, 44), (24, 44)))
        self.add_bezier('sym-e29', (24, 44), ((25.524, 44), (27.653, 42.818), (29, 42)))
        self.add_bezier('sym-e30', (29, 42), ((33.438, 39.309), (37.4, 34.318), (39, 29)))
        self.add_bezier('sym-e31', (39, 29), ((39.312, 27.945), (40, 27.118), (40, 26)))
        self.add_bezier('sym-e32', (40, 26), ((40, 25.955), (40, 26.045), (40, 26)))
        self.add_line('sym-e33', (40, 26), (40, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
