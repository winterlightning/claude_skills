"""Door (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed7f90b7-559a-4f11-8523-8dc4daea49e1'
SOURCE_PATH = 'icons-json/furnitures/door_ed7f90b7-559a-4f11-8523-8dc4daea49e1.json'
AUTHOR = 'json_to_solo'

class Door(Solo48):
    icon_id = 'door'
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
        self.add_line('e7-1', (40, 6), (39, 4))
        self.add_arc('e7-2', (39, 4), (37, 4), radius_x=6)
        self.add_arc('e8', (24, 41), (28, 39), radius_x=3, sweep=False)
        self.add_arc('e9-1', (28, 15), (27, 11), radius_x=4, sweep=False)
        self.add_line('e9-2', (27, 11), (10, 6))
        self.add_dot('e10', (19, 25))
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e8', 'e5', 'e9-1', 'e9-2', 'e6')
