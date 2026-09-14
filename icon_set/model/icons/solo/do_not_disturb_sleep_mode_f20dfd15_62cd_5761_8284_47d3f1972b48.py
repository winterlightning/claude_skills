"""Do not disturb sleep mode (mobile), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f20dfd15-62cd-5761-8284-47d3f1972b48'
SOURCE_PATH = 'icons-json/mobile/do not disturb sleep mode_f20dfd15-62cd-5761-8284-47d3f1972b48.json'
AUTHOR = 'json_to_solo'

class DoNotDisturbSleepMode(Solo48):
    icon_id = 'do-not-disturb-sleep-mode'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('do', 'not', 'disturb', 'sleep', 'mode', 'mobile')

    def build(self):
        self.add_bezier('e0', (21, 6), ((19.396, 8.594), (17.373, 11.032), (16.808, 14.1)), ((15.646, 20.441), (18.698, 27.076), (24.155, 30.431)), ((27.796, 32.673), (32.01, 33.254), (36.158, 32.305)), ((37.533, 31.994), (38.776, 31.429), (40.045, 30.824)), ((40.486, 30.611), (40.928, 30.39), (41.37, 30.169)), ((41.476, 30.12), (41.575, 30.063), (41.681, 30.014)), ((41.787, 29.956), (41.894, 29.907), (42, 29.85)), ((42, 29.854), (42, 29.858), (42, 29.863)), ((42, 30.181), (40.228, 33.098), (39.905, 33.614)), ((36.772, 38.735), (30.611, 41.992), (24.646, 41.992)), ((24.558, 41.992), (24.469, 42), (24.381, 42)), ((24.379, 42), (24.378, 42), (24.376, 42)), ((24.262, 42), (24.147, 41.992), (24.041, 41.992)), ((14.795, 41.992), (6.016, 33.9), (6.016, 24.475)), ((6.008, 24.401), (6.008, 24.335), (6, 24.262)), ((6, 24.257), (6, 24.252), (6, 24.247)), ((6, 23.933), (6.016, 23.619), (6.016, 23.305)), ((6.016, 17.585), (9.166, 11.932), (13.936, 8.798)), ((15.982, 7.448), (18.652, 6.605), (21, 6)))
        self.add_contour('c0', 'e0', closed=True)
