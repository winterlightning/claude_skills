"""R (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0a452e4-7e75-43bf-a3a5-6d48e6aee99c'
SOURCE_PATH = 'icons-json/typeface/r_c0a452e4-7e75-43bf-a3a5-6d48e6aee99c.json'
AUTHOR = 'json_to_solo'

class RC0a452e4(Solo48):
    icon_id = 'r-c0a452e4'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('r', 'typeface')

    def build(self):
        self.add_line('e0', (8, 6), (8, 44))
        self.add_bezier('e1', (40, 8), ((40, 8), (39.988, 7.627), (39.988, 7.627)), ((39.988, 7.518), (37.871, 6.409), (37.686, 6.318)), ((35.065, 5.045), (31.778, 4.009), (28.591, 4.009)), ((28.348, 4.009), (28.094, 4), (27.852, 4)), ((27.848, 4), (27.844, 4), (27.84, 4)), ((27.582, 4), (27.323, 4.018), (27.065, 4.018)), ((25.711, 4.018), (24.258, 4.282), (22.966, 4.573)), ((17.083, 5.9), (12.886, 9.273), (10.215, 13.255)), ((9.612, 14.155), (8.025, 16.545), (8.025, 17.573)), ((8.025, 17.591), (8, 17.973), (8, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
