"""Plane 1 (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f96efa-93ca-4c4e-9556-e131c14f8073'
SOURCE_PATH = 'icons-json/travel/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.json'
AUTHOR = 'json_to_solo'

class Plane118f96efa(Solo48):
    icon_id = 'plane-1-18f96efa'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (4, 29), (16, 40))
        self.add_line('e1', (16, 40), (41, 19))
        self.add_line('e2', (39, 8), (29, 15))
        self.add_line('e3', (29, 15), (16, 12))
        self.add_line('e4', (16, 12), (9, 17))
        self.add_line('e5', (9, 17), (22, 23))
        self.add_line('e6', (22, 23), (17, 28))
        self.add_line('e7', (17, 28), (9, 25))
        self.add_line('e8', (9, 25), (4, 29))
        self.add_arc('e9-1', (41, 19), (43, 17), radius_x=8, sweep=False)
        self.add_line('e9-2', (43, 17), (44, 13))
        self.add_arc('e9-3', (44, 13), (39, 8), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
