"""Personal hotspot (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45b73137-0503-4586-8373-394aa93d3ff8'
SOURCE_PATH = 'icons-json/symbol/personal hotspot_45b73137-0503-4586-8373-394aa93d3ff8.json'
AUTHOR = 'json_to_solo'

class PersonalHotspot(Solo48):
    icon_id = 'personal-hotspot'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('personal', 'hotspot', 'symbol')

    def build(self):
        self.add_line('e0', (29, 19), (20, 19))
        self.add_line('e1', (21, 40), (32, 40))
        self.add_line('e2', (15, 8), (29, 8))
        self.add_bezier('e3', (20, 19), ((14.082, 19), (10.145, 27.81), (11.709, 33.58)), ((12.909, 37.99), (17.136, 39.99), (21.045, 39.99)), ((21.127, 39.99), (20.927, 40), (21, 40)))
        self.add_bezier('e4', (32, 40), ((32.182, 40), (32.545, 39.99), (32.727, 39.99)), ((36.7, 39.99), (41.091, 39.02), (43.164, 34.91)), ((43.509, 34.22), (43.991, 33.15), (43.991, 32.34)), ((43.991, 32.26), (44, 32.19), (44, 32.11)), ((44, 30.74), (44, 29.37), (44, 28)))
        self.add_bezier('e5', (4, 21), ((4, 19.72), (4, 18.44), (4, 17.15)), ((4, 16.39), (4.382, 15.48), (4.673, 14.8)), ((6.382, 10.72), (10.545, 8.02), (14.618, 8.02)), ((14.718, 8.01), (14.9, 8.01), (15, 8)))
        self.add_bezier('e6', (29, 8), ((29.418, 8), (29.382, 8.01), (29.8, 8.01)), ((31.109, 8.01), (32.364, 8.25), (33.591, 8.71)), ((41.036, 11.5), (39.882, 21.17), (35.091, 26.15)), ((31.245, 30.15), (25.773, 28.83), (21, 29)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4')
        self.add_contour('c1', 'e5', 'e2', 'e6')
