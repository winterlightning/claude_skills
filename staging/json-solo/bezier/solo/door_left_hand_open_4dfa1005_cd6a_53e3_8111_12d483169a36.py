"""Door left hand open (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dfa1005-cd6a-53e3-8111-12d483169a36'
SOURCE_PATH = 'icons-json/building/door left hand open_4dfa1005-cd6a-53e3-8111-12d483169a36.json'
AUTHOR = 'json_to_solo'

class DoorLeftHandOpenBuilding(Solo48):
    icon_id = 'door-left-hand-open-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'open', 'building')

    def build(self):
        self.add_line('e0', (8, 44), (8, 6))
        self.add_line('e1', (11, 4), (40, 4))
        self.add_line('e2', (40, 4), (40, 44))
        self.add_line('e3', (40, 44), (35, 43))
        self.add_line('e4', (35, 43), (24, 41))
        self.add_line('e5', (20, 39), (20, 15))
        self.add_line('e6', (38, 6), (40, 6))
        self.add_arc('e7-top', (25, 25), (29, 25), radius_x=2)
        self.add_arc('e7-bottom', (29, 25), (25, 25), radius_x=2)
        self.add_bezier('e8', (8, 6), ((8, 5.873), (8, 5.564), (8, 5.436)), ((8, 4.636), (8.77, 4.009), (9.63, 4.009)), ((9.71, 4.009), (9.79, 4), (9.86, 4)), ((10.09, 4), (10.32, 4.018), (10.56, 4.018)), ((10.7, 4.009), (10.85, 4.009), (11, 4)))
        self.add_bezier('e9', (24, 41), ((22.55, 40.764), (21.08, 40.827), (20.35, 39.509)), ((20.2, 39.245), (20, 39.3), (20, 39)))
        self.add_bezier('e10', (20, 15), ((20, 13.8), (19.83, 12.355), (20.76, 11.364)), ((21.75, 10.309), (24.27, 9.836), (25.7, 9.382)), ((29.77, 8.091), (33.84, 7.027), (38, 6)))
        self.add_contour('c0', 'e0', 'e8', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
