"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3034182-8272-438e-bd25-32ee58c63442'
SOURCE_PATH = 'icons-json/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.json'
AUTHOR = 'json_to_solo'

class ShieldC3034182(Solo48):
    icon_id = 'shield-c3034182'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (8, 24), (8, 9))
        self.add_line('e1', (15, 9), (24, 4))
        self.add_line('e2', (24, 4), (33, 9))
        self.add_line('e3', (37, 9), (40, 8))
        self.add_bezier('e4', (40, 8), ((40, 10), (39.983, 11.627), (39.983, 13.627)), ((39.983, 16.318), (39.958, 19), (39.907, 21.691)), ((39.891, 22.945), (40, 24.364), (39.747, 25.6)), ((38.602, 31.245), (34.88, 35.609), (30.897, 39.218)), ((29.364, 40.609), (27.789, 41.864), (26.08, 42.982)), ((25.566, 43.309), (24.716, 44), (24.084, 44)), ((24.083, 44), (24.083, 44), (24.082, 44)), ((24.032, 44), (23.982, 43.991), (23.933, 43.991)), ((22.771, 43.991), (19.545, 41.227), (18.56, 40.4)), ((14.248, 36.764), (9.794, 32.355), (8.429, 26.427)), ((8.261, 25.664), (8, 24.782), (8, 24)))
        self.add_bezier('e5', (8, 9), ((8.404, 8.773), (8.817, 8.091), (9.221, 7.864)), ((9.238, 7.864), (10.375, 8.5), (10.501, 8.564)), ((11.756, 9.218), (13.594, 9.827), (15, 9)))
        self.add_bezier('e6', (33, 9), ((34.389, 9.818), (35.594, 9.755), (37, 9)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e2', 'e6', 'e3', closed=True)
