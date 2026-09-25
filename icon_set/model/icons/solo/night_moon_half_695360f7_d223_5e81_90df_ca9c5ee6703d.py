"""Night moon half (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '695360f7-d223-5e81-90df-ca9c5ee6703d'
SOURCE_PATH = 'pictographic-primitives/weather/night moon half_695360f7-d223-5e81-90df-ca9c5ee6703d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class NightMoonHalfWeather(Solo48):
    icon_id = 'night-moon-half-weather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('night', 'moon', 'half', 'weather')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (40, 44), (40, 4))
        self.add_bezier('e1', (40, 4), ((39.187, 4), (38.387, 4.009), (37.573, 4.009)), ((24.907, 4.009), (13.093, 9.582), (9.347, 17.9)), ((8.653, 19.445), (8.013, 21.173), (8.013, 22.8)), ((8.013, 23.015), (8, 23.221), (8, 23.435)), ((8, 23.8), (8.027, 24.155), (8.027, 24.509)), ((8.027, 27.355), (9.267, 30.236), (11.187, 32.736)), ((16.64, 39.791), (27.533, 43.991), (39.147, 43.991)), ((39.427, 43.991), (39.72, 44), (40, 44)))
        self.add_contour('c0', 'e1', 'e0', closed=True)
