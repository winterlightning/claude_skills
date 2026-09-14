"""Parking (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8eb10225-b911-4521-b1e1-6f58e04f8681'
SOURCE_PATH = 'icons-json/transportation/parking_8eb10225-b911-4521-b1e1-6f58e04f8681.json'
AUTHOR = 'json_to_solo'

class Parking(Solo48):
    icon_id = 'parking'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('parking', 'transportation')

    def build(self):
        self.add_line('e0', (8, 29), (28, 29))
        self.add_line('e1', (26, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_arc('e3-1', (28, 29), (40, 17), radius_x=14, sweep=False)
        self.add_line('e3-2', (40, 17), (39, 12))
        self.add_arc('e3-3', (39, 12), (37, 9), radius_x=11, sweep=False)
        self.add_arc('e3-4', (37, 9), (26, 4), radius_x=16, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e1', 'e2')
