"""Sock (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48de2726-3a31-442e-87c2-49ed8bcb4c95'
SOURCE_PATH = 'icons-json/holidays/sock_48de2726-3a31-442e-87c2-49ed8bcb4c95.json'
AUTHOR = 'json_to_solo'

class Sock(Solo48):
    icon_id = 'sock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('sock', 'holidays')

    def build(self):
        self.add_line('e0', (12, 27), (12, 12))
        self.add_line('e1', (28, 12), (12, 12))
        self.add_line('e2', (28, 12), (28, 24))
        self.add_line('e3', (30, 28), (36, 29))
        self.add_line('e4', (31, 44), (20, 40))
        self.add_line('e5', (28, 4), (11, 4))
        self.add_arc('e6', (12, 27), (20, 40), radius_x=11)
        self.add_arc('e7', (12, 27), (20, 40), radius_x=10, sweep=False)
        self.add_line('e8', (28, 24), (30, 28))
        self.add_arc('e9-1', (36, 29), (40, 36), radius_x=9)
        self.add_line('e9-2', (40, 36), (39, 40))
        self.add_arc('e9-3', (39, 40), (33, 44), radius_x=7)
        self.add_line('e9-4', (33, 44), (31, 44))
        self.add_arc('e10', (28, 12), (28, 4), radius_x=4, sweep=False)
        self.add_line('e11-1', (11, 4), (9, 5))
        self.add_line('e11-2', (9, 5), (8, 8))
        self.add_arc('e11-3', (8, 8), (12, 12), radius_x=4, sweep=False)
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e4')
        self.add_contour('c5', 'e10', 'e5', 'e11-1', 'e11-2', 'e11-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
