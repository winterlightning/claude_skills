"""Location pin (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e99a5ab-bfd4-40df-ab71-0932992ba881'
SOURCE_PATH = 'icons-json/state/location pin_9e99a5ab-bfd4-40df-ab71-0932992ba881.json'
AUTHOR = 'json_to_solo'

class LocationPinState(Solo48):
    icon_id = 'location-pin-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('location', 'pin', 'state')

    def build(self):
        self.add_line('e0', (20, 39), (15, 33))
        self.add_line('e1', (36, 29), (31, 36))
        self.add_line('e2', (30, 37), (24, 44))
        self.add_line('e3', (24, 44), (22, 42))
        self.add_arc('e4-top', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('e4-bottom', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_bezier('e5', (22, 42), ((21.33, 41.1), (20.7, 39.891), (20, 39)))
        self.add_bezier('e6', (15, 33), ((11.81, 28.945), (8.01, 24.6), (8.01, 19.373)), ((8.01, 19.203), (8, 19.041), (8, 18.872)), ((8, 18.869), (8, 18.866), (8, 18.864)), ((8, 18.7), (8.01, 18.527), (8.01, 18.364)), ((8.01, 11.118), (15.27, 4.009), (23.34, 4.009)), ((23.49, 4.009), (23.63, 4), (23.78, 4)), ((23.783, 4), (23.785, 4), (23.788, 4)), ((23.955, 4), (24.113, 4), (24.28, 4)), ((32.65, 4), (39.99, 10.973), (39.99, 18.527)), ((39.99, 18.697), (40, 18.859), (40, 19.028)), ((40, 19.031), (40, 19.034), (40, 19.036)), ((40, 19.209), (39.99, 19.382), (39.99, 19.555)), ((39.99, 23.136), (38.25, 26.136), (36, 29)))
        self.add_bezier('e7', (31, 36), ((30.52, 36.609), (30.5, 36.4), (30, 37)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2', 'e3', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
