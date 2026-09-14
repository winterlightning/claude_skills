"""Earth model 1 (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5e62027-4155-4c3f-9eea-0fcf4e0f687b'
SOURCE_PATH = 'icons-json/maps/earth model 1_a5e62027-4155-4c3f-9eea-0fcf4e0f687b.json'
AUTHOR = 'json_to_solo'

class EarthModel1Maps(Solo48):
    icon_id = 'earth-model-1-maps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'model', 'maps')

    def build(self):
        self.add_line('e0', (22, 40), (22, 36))
        self.add_line('e1', (31, 44), (13, 44))
        self.add_line('e2', (15, 40), (29, 40))
        self.add_arc('e3-top', (8, 19), (36, 19), radius_x=14, radius_y=13)
        self.add_arc('e3-bottom', (36, 19), (8, 19), radius_x=14, radius_y=13)
        self.add_bezier('e4', (34, 4), ((33.83, 4.218), (33.37, 4.591), (33.41, 4.791)), ((33.42, 4.836), (33.96, 5.318), (34.18, 5.527)), ((34.88, 6.182), (35.55, 6.873), (36.15, 7.591)), ((38.51, 10.382), (39.99, 13.873), (39.99, 17.427)), ((39.99, 17.544), (40, 17.669), (40, 17.785)), ((40, 17.787), (40, 17.789), (40, 17.791)), ((40, 18.091), (39.99, 18.4), (39.99, 18.7)), ((39.99, 20.836), (39.42, 23.018), (38.57, 25)), ((35.77, 31.509), (29.59, 35.655), (22, 36)))
        self.add_bezier('e5', (8, 30), ((8.02, 29.982), (8.04, 30.318), (8.06, 30.3)), ((8.27, 30.064), (8.47, 29.836), (8.68, 29.6)), ((8.77, 29.609), (9.42, 30.336), (9.7, 30.591)), ((10.64, 31.482), (11.65, 32.282), (12.75, 33.009)), ((15.49, 34.836), (18.64, 35.873), (22, 36)))
        self.add_bezier('e6', (13, 44), ((13.04, 42.845), (13.14, 40), (15, 40)))
        self.add_bezier('e7', (29, 40), ((29.23, 40.109), (29.49, 40.491), (29.71, 40.627)), ((30.95, 41.364), (30.93, 42.809), (31, 44)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1', 'e6', 'e2', 'e7', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
