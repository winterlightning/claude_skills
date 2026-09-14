"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e43b261d-5d07-450c-ab97-9058803311d6'
SOURCE_PATH = 'icons-json/interface-essential/lock_e43b261d-5d07-450c-ab97-9058803311d6.json'
AUTHOR = 'json_to_solo'

class Lock(Solo48):
    icon_id = 'lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 19), (35, 15))
        self.add_line('e1', (14, 14), (14, 19))
        self.add_line('e2', (24, 34), (24, 29))
        self.add_line('e3', (37, 19), (11, 19))
        self.add_line('e4', (8, 25), (8, 40))
        self.add_line('e5', (11, 44), (36, 44))
        self.add_line('e6', (40, 42), (40, 22))
        self.add_arc('e7-1', (35, 15), (24, 4), radius_x=11, sweep=False)
        self.add_arc('e7-2', (24, 4), (14, 14), radius_x=10, sweep=False)
        self.add_line('e8', (40, 22), (37, 19))
        self.add_line('e9-1', (11, 19), (9, 21))
        self.add_arc('e9-2', (9, 21), (8, 24), radius_x=5, sweep=False)
        self.add_line('e9-3', (8, 24), (8, 25))
        self.add_line('e10-1', (8, 40), (9, 43))
        self.add_arc('e10-2', (9, 43), (11, 44), radius_x=3)
        self.add_line('e11-1', (36, 44), (38, 44))
        self.add_arc('e11-2', (38, 44), (40, 42), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e8', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10-1', 'e10-2', 'e5', 'e11-1', 'e11-2', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
