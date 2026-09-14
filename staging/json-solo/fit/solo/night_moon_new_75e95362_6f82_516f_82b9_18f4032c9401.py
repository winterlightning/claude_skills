"""Night moon new (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e0-1', (8, 44), (24, 19), radius_x=22, sweep=False)
        self.add_arc('e0-2', (24, 19), (8, 4), radius_x=26, sweep=False)
        self.add_arc('e0-3', (8, 4), (32, 11), radius_x=45)
        self.add_arc('e0-4', (32, 11), (40, 24), radius_x=16)
        self.add_arc('e0-5', (40, 24), (29, 39), radius_x=17)
        self.add_arc('e0-6', (29, 39), (8, 44), radius_x=48)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', closed=True)
