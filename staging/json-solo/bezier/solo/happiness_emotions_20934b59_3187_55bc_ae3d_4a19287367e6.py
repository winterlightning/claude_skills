"""Happiness emotions (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20934b59-3187-55bc-ae3d-4a19287367e6'
SOURCE_PATH = 'icons-json/health/happiness emotions_20934b59-3187-55bc-ae3d-4a19287367e6.json'
AUTHOR = 'json_to_solo'

class HappinessEmotionsHealth(Solo48):
    icon_id = 'happiness-emotions-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('happiness', 'emotions', 'health')

    def build(self):
        self.add_line('e0', (13, 44), (13, 35))
        self.add_line('e1', (37, 15), (40, 25))
        self.add_line('e2', (37, 29), (36, 36))
        self.add_line('e3', (28, 40), (28, 44))
        self.add_bezier('e4', (30, 31), ((31.962, 33.464), (32.884, 34.873), (36, 35)))
        self.add_bezier('e5', (13, 35), ((13, 32.273), (11.225, 30.773), (10.021, 28.591)), ((8.707, 26.227), (8.008, 23.373), (8.008, 20.618)), ((8.008, 20.466), (8, 20.323), (8, 20.171)), ((8, 20.168), (8, 20.166), (8, 20.164)), ((8.008, 20.027), (8.008, 19.891), (8.017, 19.764)), ((8.017, 13.1), (11.958, 6.791), (17.886, 4.736)), ((19.057, 4.327), (20.354, 4.018), (21.592, 4.018)), ((21.785, 4.018), (21.987, 4), (22.181, 4)), ((22.184, 4), (22.187, 4), (22.191, 4)), ((22.389, 4), (22.58, 4.009), (22.779, 4.009)), ((28.573, 4.009), (35.055, 9.236), (37, 15)))
        self.add_bezier('e6', (40, 25), ((40, 25.255), (40, 25.418), (40, 25.673)), ((40, 25.873), (40, 26.082), (40, 26.282)), ((40, 26.536), (39.983, 26.782), (39.983, 27.036)), ((39.983, 28.336), (37.716, 28.918), (37, 29)))
        self.add_bezier('e7', (36, 36), ((34.493, 40.464), (31.823, 39.673), (28, 40)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.relate('connect', 'c0', 'c1')
