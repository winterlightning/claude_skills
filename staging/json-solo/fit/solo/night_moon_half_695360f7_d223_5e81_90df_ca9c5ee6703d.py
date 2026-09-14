"""Night moon half (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '695360f7-d223-5e81-90df-ca9c5ee6703d'
SOURCE_PATH = 'icons-json/weather/night moon half_695360f7-d223-5e81-90df-ca9c5ee6703d.json'
AUTHOR = 'json_to_solo'

class NightMoonHalf695360f7(Solo48):
    icon_id = 'night-moon-half-695360f7'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'half', 'weather')

    def build(self):
        self.add_line('e0', (40, 44), (40, 4))
        self.add_arc('e1-1', (40, 4), (34, 4), radius_x=78)
        self.add_line('e1-2', (34, 4), (25, 6))
        self.add_arc('e1-3', (25, 6), (18, 9), radius_x=34, sweep=False)
        self.add_arc('e1-4', (18, 9), (8, 23), radius_x=17, sweep=False)
        self.add_line('e1-5', (8, 23), (10, 31))
        self.add_arc('e1-6', (10, 31), (23, 41), radius_x=26, sweep=False)
        self.add_arc('e1-7', (23, 41), (29, 43), radius_x=40, sweep=False)
        self.add_line('e1-8', (29, 43), (40, 44))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e0', closed=True)
