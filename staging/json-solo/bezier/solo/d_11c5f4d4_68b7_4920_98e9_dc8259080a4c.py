"""D (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11c5f4d4-68b7-4920-98e9-dc8259080a4c'
SOURCE_PATH = 'icons-json/typeface/d_11c5f4d4-68b7-4920-98e9-dc8259080a4c.json'
AUTHOR = 'json_to_solo'

class D11c5f4d4(Solo48):
    icon_id = 'd-11c5f4d4'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('d', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (40, 38))
        self.add_bezier('e1', (40, 38), ((40, 38), (39.975, 37.691), (39.975, 37.709)), ((39.975, 38.618), (38.757, 39.782), (38.031, 40.418)), ((35.077, 42.964), (30.105, 43.982), (25.698, 43.982)), ((25.329, 43.982), (24.96, 44), (24.591, 44)), ((24.587, 44), (24.583, 44), (24.58, 44)), ((24.35, 44), (24.12, 43.991), (23.902, 43.991)), ((14.843, 43.991), (8.012, 37.573), (8.012, 31.164)), ((8.012, 31.003), (8, 30.841), (8, 30.672)), ((8, 30.669), (8, 30.666), (8, 30.664)), ((8, 30.455), (8.025, 30.236), (8.025, 30.018)), ((8.025, 28.418), (8.812, 26.791), (9.723, 25.364)), ((13.083, 20.073), (19.594, 17.3), (27.52, 17.773)), ((31.102, 17.991), (34.683, 18.8), (37.588, 20.4)), ((37.945, 20.591), (39.988, 21.8), (39.988, 22.145)), ((39.988, 22.164), (40, 21.991), (40, 22)))
        self.add_contour('c0', 'e0', 'e1')
