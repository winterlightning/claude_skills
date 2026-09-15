"""Glue (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cefa6872-2a4d-47f5-b5a5-612921a29892'
SOURCE_PATH = 'icons-json/design/glue_cefa6872-2a4d-47f5-b5a5-612921a29892.json'
AUTHOR = 'gpt-6'

class Glue(Solo48):
    icon_id = 'glue'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('glue', 'design')

    def build(self):
        self.add_arc('sym-e2', (24, 4), (27, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e3', (27, 6), (32, 21))
        self.add_line('sym-e5', (32, 21), (16, 21))
        self.add_line('sym-e7', (16, 21), (21, 6))
        self.add_arc('sym-e9', (21, 6), (24, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e12', (32, 21), (35, 21))
        self.add_line('sym-e13', (35, 21), (38, 23))
        self.add_line('sym-e14', (38, 23), (40, 39))
        self.add_line('sym-e15', (40, 39), (40, 40))
        self.add_arc('sym-e16', (40, 40), (36, 44), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e18', (36, 44), (12, 44))
        self.add_arc('sym-e21', (12, 44), (8, 40), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e22', (8, 40), (8, 39))
        self.add_line('sym-e23', (8, 39), (10, 23))
        self.add_line('sym-e24', (10, 23), (13, 21))
        self.add_line('sym-e25', (13, 21), (16, 21))
        self.add_contour('sym-c0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
