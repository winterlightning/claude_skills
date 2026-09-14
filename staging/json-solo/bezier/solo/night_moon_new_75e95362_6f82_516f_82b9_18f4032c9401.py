"""Night moon new (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75e95362-6f82-516f-82b9-18f4032c9401'
SOURCE_PATH = 'icons-json/weather/night moon new_75e95362-6f82-516f-82b9-18f4032c9401.json'
AUTHOR = 'json_to_solo'

class NightMoonNew75e95362(Solo48):
    icon_id = 'night-moon-new-75e95362'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'new', 'weather')

    def build(self):
        self.add_bezier('e0', (8, 44), ((11.104, 42.264), (14.4, 40.582), (16.864, 38.527)), ((24.416, 32.209), (26.544, 24.264), (23.216, 16.9)), ((21.68, 13.5), (19.024, 10.045), (14.736, 7.464)), ((13.312, 6.6), (11.792, 5.818), (10.176, 5.073)), ((9.632, 4.818), (9.088, 4.555), (8.56, 4.291)), ((8.368, 4.191), (8.192, 4.1), (8, 4)), ((8.003, 4), (8.006, 4), (8.009, 4)), ((8.198, 4), (8.387, 4.018), (8.592, 4.027)), ((9.136, 4.055), (9.68, 4.091), (10.24, 4.118)), ((11.488, 4.191), (12.736, 4.264), (13.968, 4.4)), ((17.76, 4.827), (21.488, 5.818), (24.656, 7.055)), ((34.144, 10.736), (39.984, 17.036), (39.984, 23.573)), ((39.984, 23.796), (40, 24.011), (40, 24.235)), ((40, 24.238), (40, 24.242), (40, 24.245)), ((39.984, 24.345), (39.984, 24.455), (39.968, 24.555)), ((39.968, 32.291), (31.392, 39.845), (18.656, 42.709)), ((15.216, 43.482), (11.648, 43.764), (8, 44)))
        self.add_contour('c0', 'e0', closed=True)
