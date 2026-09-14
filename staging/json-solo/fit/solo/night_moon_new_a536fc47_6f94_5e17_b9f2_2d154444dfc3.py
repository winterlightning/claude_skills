"""Night moon new (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a536fc47-6f94-5e17-b9f2-2d154444dfc3'
SOURCE_PATH = 'icons-json/weather/night moon new_a536fc47-6f94-5e17-b9f2-2d154444dfc3.json'
AUTHOR = 'json_to_solo'

class NightMoonNewA536fc47(Solo48):
    icon_id = 'night-moon-new-a536fc47'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'new', 'weather')

    def build(self):
        self.add_line('e0', (30, 5), (40, 4))
        self.add_line('e1', (40, 4), (34, 9))
        self.add_line('e2', (32, 39), (40, 44))
        self.add_arc('e3-1', (40, 44), (19, 39), radius_x=47)
        self.add_arc('e3-2', (19, 39), (8, 24), radius_x=18)
        self.add_line('e3-3', (8, 24), (10, 17))
        self.add_arc('e3-4', (10, 17), (30, 5), radius_x=34)
        self.add_arc('e4', (34, 9), (32, 39), radius_x=17, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e1', 'e4', 'e2', closed=True)
