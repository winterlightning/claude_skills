"""Power button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '169cceb8-f596-5e38-8241-0caa55d29dc4'
SOURCE_PATH = 'icons-json/interface-essential/power button_169cceb8-f596-5e38-8241-0caa55d29dc4.json'
AUTHOR = 'json_to_solo'

class PowerButtonInterfaceEssential(Solo48):
    icon_id = 'power-button-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('power', 'button', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 23))
        self.add_bezier('e1', (18, 10), ((13.402, 12.118), (10.24, 15.691), (8.766, 20.982)), ((8.337, 22.509), (8.017, 24.1), (8.017, 25.7)), ((8.017, 25.951), (8, 26.192), (8, 26.443)), ((8, 26.447), (8, 26.451), (8, 26.455)), ((8.008, 26.582), (8.008, 26.718), (8.017, 26.855)), ((8.017, 35.618), (15.217, 43.991), (23.461, 43.991)), ((23.652, 43.991), (23.851, 44), (24.041, 44)), ((24.044, 44), (24.047, 44), (24.051, 44)), ((24.253, 44), (24.455, 43.982), (24.648, 43.982)), ((32.834, 43.982), (39.992, 35.645), (39.992, 26.964)), ((39.992, 26.749), (40, 26.543), (40, 26.328)), ((40, 26.325), (40, 26.322), (40, 26.318)), ((40, 26.109), (39.992, 25.891), (39.992, 25.682)), ((39.992, 18.873), (35.659, 11.709), (30, 9)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
