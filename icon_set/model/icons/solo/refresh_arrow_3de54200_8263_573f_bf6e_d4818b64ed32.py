"""Refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3de54200-8263-573f-bf6e-d4818b64ed32'
SOURCE_PATH = 'icons-json/interface-essential/refresh arrow_3de54200-8263-573f-bf6e-d4818b64ed32.json'
AUTHOR = 'json_to_solo'

class RefreshArrow(Solo48):
    icon_id = 'refresh-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 38), (14, 38))
        self.add_line('e1', (14, 38), (14, 29))
        self.add_line('e2-1', (21, 41), (26, 42))
        self.add_arc('e2-2', (26, 42), (34, 39), radius_x=19, sweep=False)
        self.add_arc('e2-3', (34, 39), (41, 30), radius_x=18, sweep=False)
        self.add_line('e2-4', (41, 30), (42, 24))
        self.add_line('e2-5', (42, 24), (41, 18))
        self.add_arc('e2-6', (41, 18), (39, 14), radius_x=17, sweep=False)
        self.add_arc('e2-7', (39, 14), (34, 9), radius_x=18, sweep=False)
        self.add_arc('e2-8', (34, 9), (25, 6), radius_x=18, sweep=False)
        self.add_arc('e2-9', (25, 6), (24, 6), radius_x=19)
        self.add_arc('e2-10', (24, 6), (13, 10), radius_x=18, sweep=False)
        self.add_arc('e2-11', (13, 10), (6, 24), radius_x=19, sweep=False)
        self.add_arc('e2-12', (6, 24), (13, 38), radius_x=18, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e2-12')
        self.add_contour('c1', 'e0', 'e1')
        self.relate('connect', 'c0', 'c1')
