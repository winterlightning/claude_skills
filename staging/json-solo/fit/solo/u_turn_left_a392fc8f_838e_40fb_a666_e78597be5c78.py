"""U turn left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a392fc8f-838e-40fb-a666-e78597be5c78'
SOURCE_PATH = 'icons-json/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.json'
AUTHOR = 'json_to_solo'

class UTurnLeftTransportation(Solo48):
    icon_id = 'u-turn-left-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('u', 'turn', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (13, 21), (13, 33))
        self.add_line('e1', (6, 25), (13, 33))
        self.add_line('e2', (13, 33), (23, 25))
        self.add_line('e3-1', (42, 42), (41, 15))
        self.add_arc('e3-2', (41, 15), (35, 8), radius_x=12, sweep=False)
        self.add_line('e3-3', (35, 8), (27, 6))
        self.add_arc('e3-4', (27, 6), (13, 21), radius_x=15, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
