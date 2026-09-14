"""Door (furnitures), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed7f90b7-559a-4f11-8523-8dc4daea49e1'
SOURCE_PATH = 'icons-json/furnitures/door_ed7f90b7-559a-4f11-8523-8dc4daea49e1.json'
AUTHOR = 'json_to_solo'

class DoorFurnitures(Solo48):
    icon_id = 'door-furnitures'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('door', 'furnitures')

    def build(self):
        self.add_line('e0', (40, 44), (40, 6))
        self.add_line('e1', (37, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_line('e3', (8, 44), (13, 43))
        self.add_line('e4', (13, 43), (24, 41))
        self.add_line('e5', (28, 39), (28, 15))
        self.add_line('e6', (10, 6), (8, 6))
        self.add_bezier('e7', (40, 6), ((40, 5.873), (40, 5.564), (40, 5.436)), ((40, 4.636), (39.23, 4.009), (38.37, 4.009)), ((38.29, 4.009), (38.21, 4), (38.14, 4)), ((37.91, 4), (37.68, 4.018), (37.44, 4.018)), ((37.3, 4.009), (37.15, 4.009), (37, 4)))
        self.add_bezier('e8', (24, 41), ((25.45, 40.764), (26.92, 40.827), (27.65, 39.509)), ((27.8, 39.245), (28, 39.3), (28, 39)))
        self.add_bezier('e9', (28, 15), ((28, 13.8), (28.17, 12.355), (27.24, 11.364)), ((26.25, 10.309), (23.73, 9.836), (22.3, 9.382)), ((18.23, 8.091), (14.16, 7.027), (10, 6)))
        self.add_dot('e10', (19, 25))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e8', 'e5', 'e9', 'e6')
