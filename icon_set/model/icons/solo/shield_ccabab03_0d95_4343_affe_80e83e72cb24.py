"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccabab03-0d95-4343-affe-80e83e72cb24'
SOURCE_PATH = 'icons-json/protection/shield_ccabab03-0d95-4343-affe-80e83e72cb24.json'
AUTHOR = 'json_to_solo'

class ShieldCcabab03(Solo48):
    icon_id = 'shield-ccabab03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (8, 9), (12, 4))
        self.add_line('e1', (12, 4), (18, 8))
        self.add_line('e2', (18, 8), (24, 4))
        self.add_line('e3', (24, 4), (30, 8))
        self.add_line('e4', (30, 8), (36, 4))
        self.add_line('e5', (36, 4), (39, 9))
        self.add_line('e6', (37, 19), (39, 23))
        self.add_line('e7', (10, 23), (11, 19))
        self.add_bezier('e8', (39, 9), ((37.164, 11.345), (35.924, 13.155), (35.874, 16.327)), ((35.857, 17.391), (36.394, 18.118), (37, 19)))
        self.add_bezier('e9', (39, 23), ((39.699, 24.009), (39.992, 25.409), (39.992, 26.627)), ((39.992, 26.779), (40, 26.94), (40, 27.093)), ((40, 27.095), (40, 27.098), (40, 27.1)), ((40, 27.373), (39.992, 27.645), (39.992, 27.927)), ((39.992, 34.773), (33.507, 39.055), (28.573, 41.827)), ((27.857, 42.227), (24.657, 44), (24.093, 44)), ((24.077, 44), (24.061, 44), (24.044, 44)), ((23, 44), (20.414, 42.346), (19.419, 41.809)), ((15.714, 39.809), (11.587, 37.109), (9.465, 33.118)), ((8.867, 31.991), (8.017, 30.491), (8.017, 29.145)), ((8.008, 29.055), (8.008, 28.964), (8, 28.873)), ((8, 28.755), (8.008, 28.636), (8.008, 28.518)), ((8.008, 27.136), (8.699, 25.855), (9.179, 24.627)), ((9.373, 24.127), (9.815, 23.509), (10, 23)))
        self.add_bezier('e10', (11, 19), ((11.126, 18.655), (11.545, 17.791), (11.613, 17.427)), ((11.756, 16.709), (11.992, 15.982), (11.949, 15.236)), ((11.789, 12.509), (9.651, 10.809), (8, 9)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e8', 'e6', 'e9', 'e7', 'e10', closed=True)
