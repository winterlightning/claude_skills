"""Adjustable lamp 2 (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a3dd3e8-27fe-40d4-9e28-a1002c878050'
SOURCE_PATH = 'icons-json/_uncategorized_01/adjustable lamp 2_1a3dd3e8-27fe-40d4-9e28-a1002c878050.json'
AUTHOR = 'json_to_solo'

class AdjustableLamp2(Solo48):
    icon_id = 'adjustable-lamp-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('adjustable', 'lamp', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 33))
        self.add_line('sym-e1', (24, 33), (31, 33))
        self.add_arc('sym-e2', (31, 33), (32, 32), radius_x=1, sweep=False)
        self.add_line('sym-e3', (32, 32), (30, 20))
        self.add_line('sym-e4', (30, 20), (28, 19))
        self.add_line('sym-e5', (28, 19), (24, 19))
        self.add_line('sym-e6', (24, 19), (20, 19))
        self.add_line('sym-e7', (20, 19), (18, 20))
        self.add_line('sym-e8', (18, 20), (16, 32))
        self.add_arc('sym-e9', (16, 32), (17, 33), radius_x=1, sweep=False)
        self.add_line('sym-e10', (17, 33), (24, 33))
        self.add_arc('sym-e11', (24, 4), (25, 4), radius_x=29, sweep=False)
        self.add_arc('sym-e12', (25, 4), (40, 20), radius_x=17)
        self.add_line('sym-e15', (29, 44), (24, 44))
        self.add_line('sym-e16', (24, 44), (19, 44))
        self.add_line('sym-e17', (24, 4), (23, 4))
        self.add_arc('sym-e18', (23, 4), (8, 20), radius_x=17, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
