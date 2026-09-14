"""Night moon half (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cab542e-1489-584c-9986-244a280dc63e'
SOURCE_PATH = 'icons-json/weather/night moon half_5cab542e-1489-584c-9986-244a280dc63e.json'
AUTHOR = 'json_to_solo'

class NightMoonHalf5cab542e(Solo48):
    icon_id = 'night-moon-half-5cab542e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'half', 'weather')

    def build(self):
        self.add_arc('sym-e0', (40, 24), (40, 23), radius_x=12)
        self.add_arc('sym-e1', (40, 23), (17, 5), radius_x=24, sweep=False)
        self.add_arc('sym-e2', (17, 5), (10, 4), radius_x=39, sweep=False)
        self.add_line('sym-e4', (10, 4), (8, 4))
        self.add_line('sym-e5', (8, 4), (8, 24))
        self.add_line('sym-e6', (8, 24), (8, 44))
        self.add_arc('sym-e7', (8, 44), (10, 44), radius_x=22)
        self.add_arc('sym-e9', (10, 44), (17, 43), radius_x=39, sweep=False)
        self.add_arc('sym-e10', (17, 43), (40, 25), radius_x=24, sweep=False)
        self.add_line('sym-e11', (40, 25), (40, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
