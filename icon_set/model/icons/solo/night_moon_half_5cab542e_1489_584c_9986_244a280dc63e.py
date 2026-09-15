"""Night moon half (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5cab542e-1489-584c-9986-244a280dc63e'
SOURCE_PATH = 'icons-json/weather/night moon half_5cab542e-1489-584c-9986-244a280dc63e.json'
AUTHOR = 'gpt-6'

class NightMoonHalf(Solo48):
    icon_id = 'night-moon-half'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'half', 'weather')

    def build(self):
        self.add_bezier('sym-e0', (40, 24), ((39.995, 23.748), (40, 23.26), (40, 23)))
        self.add_bezier('sym-e1', (40, 23), ((40, 14.509), (29.975, 7.191), (17, 5)))
        self.add_bezier('sym-e2', (17, 5), ((14.949, 4.655), (12.153, 4), (10, 4)))
        self.add_bezier('sym-e3', (10, 4), ((9.767, 4), (10.233, 4), (10, 4)))
        self.add_bezier('sym-e4', (10, 4), ((9.418, 4), (8.582, 4), (8, 4)))
        self.add_line('sym-e5', (8, 4), (8, 44))
        self.add_bezier('sym-e7', (8, 44), ((8.582, 44), (9.418, 44), (10, 44)))
        self.add_bezier('sym-e8', (10, 44), ((10.233, 44), (9.767, 44), (10, 44)))
        self.add_bezier('sym-e9', (10, 44), ((12.153, 44), (14.949, 43.345), (17, 43)))
        self.add_bezier('sym-e10', (17, 43), ((29.975, 40.809), (40, 33.491), (40, 25)))
        self.add_bezier('sym-e11', (40, 25), ((40, 24.74), (39.995, 24.252), (40, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
