"""Phone 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'icons-json/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.json'
AUTHOR = 'json_to_solo'

class Phone1State(Solo48):
    icon_id = 'phone-1-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('phone', 'state')

    def build(self):
        self.add_line('e0', (13, 6), (19, 11))
        self.add_line('e1', (37, 29), (42, 35))
        self.add_line('e2-1', (42, 35), (42, 37))
        self.add_arc('e2-2', (42, 37), (38, 41), radius_x=11)
        self.add_line('e2-3', (38, 41), (34, 42))
        self.add_arc('e2-4', (34, 42), (6, 13), radius_x=39)
        self.add_arc('e2-5', (6, 13), (12, 6), radius_x=8)
        self.add_line('e2-6', (12, 6), (13, 6))
        self.add_arc('e3-1', (19, 11), (19, 15), radius_x=3)
        self.add_arc('e3-2', (19, 15), (17, 19), radius_x=6, sweep=False)
        self.add_arc('e3-3', (17, 19), (20, 24), radius_x=9, sweep=False)
        self.add_arc('e3-4', (20, 24), (29, 31), radius_x=16, sweep=False)
        self.add_line('e3-5', (29, 31), (35, 28))
        self.add_arc('e3-6', (35, 28), (37, 29), radius_x=2)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e1', closed=True)
