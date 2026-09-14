"""Multiple neutral 1 (users), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9efa6ac4-2ff0-4b39-a31e-f7c05686d8cb'
SOURCE_PATH = 'icons-json/users/multiple neutral 1_9efa6ac4-2ff0-4b39-a31e-f7c05686d8cb.json'
AUTHOR = 'json_to_solo'

class MultipleNeutral1Users(Solo48):
    icon_id = 'multiple-neutral-1-users'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    aliases = ()
    keywords = ('multiple', 'neutral', 'users')

    def build(self):
        self.add_line('e0', (40, 40), (44, 40))
        self.add_line('e1', (41, 32), (37, 29))
        self.add_line('e2', (13, 21), (15, 25))
        self.add_line('e3', (13, 28), (8, 31))
        self.add_line('e4', (5, 40), (35, 40))
        self.add_line('e5', (31, 31), (27, 28))
        self.add_line('e6', (25, 25), (27, 21))
        self.add_line('e7-1', (44, 40), (44, 36))
        self.add_arc('e7-2', (44, 36), (41, 32), radius_x=5, sweep=False)
        self.add_arc('e8-1', (37, 29), (36, 27), radius_x=2)
        self.add_arc('e8-2', (36, 27), (39, 20), radius_x=10, sweep=False)
        self.add_arc('e8-3', (39, 20), (35, 14), radius_x=7, sweep=False)
        self.add_arc('e8-4', (35, 14), (28, 15), radius_x=6, sweep=False)
        self.add_arc('e8-5', (28, 15), (24, 9), radius_x=8, sweep=False)
        self.add_line('e8-6', (24, 9), (20, 8))
        self.add_line('e8-7', (20, 8), (14, 10))
        self.add_arc('e8-8', (14, 10), (12, 13), radius_x=7, sweep=False)
        self.add_arc('e8-9', (12, 13), (13, 21), radius_x=10, sweep=False)
        self.add_arc('e9', (15, 25), (13, 28), radius_x=2)
        self.add_arc('e10-1', (8, 31), (4, 36), radius_x=6, sweep=False)
        self.add_line('e10-2', (4, 36), (4, 40))
        self.add_arc('e10-3', (4, 40), (5, 40), radius_x=5)
        self.add_arc('e11', (35, 40), (31, 31), radius_x=7, sweep=False)
        self.add_arc('e12', (27, 28), (25, 25), radius_x=2)
        self.add_line('e13', (27, 21), (28, 15))
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e8-8', 'e8-9', 'e2', 'e9', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13')
