"""Batch-03/hat architect (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b14b6641-0dd7-524f-a069-fc2f7884f0f3'
SOURCE_PATH = 'icons-json/accessories/batch-03/hat architect_b14b6641-0dd7-524f-a069-fc2f7884f0f3.json'
AUTHOR = 'json_to_solo'

class Batch03HatArchitect(Solo48):
    icon_id = 'batch-03-hat-architect'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'architect', 'accessories')

    def build(self):
        self.add_arc('sym-e1', (8, 31), (7, 31), radius_x=5, sweep=False)
        self.add_arc('sym-e4', (7, 31), (4, 36), radius_x=6, sweep=False)
        self.add_arc('sym-e7-1', (4, 36), (5, 39), radius_x=5, sweep=False)
        self.add_arc('sym-e7-2', (5, 39), (7, 40), radius_x=3, sweep=False)
        self.add_line('sym-e8', (7, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (41, 40))
        self.add_arc('sym-e10-1', (41, 40), (43, 39), radius_x=3, sweep=False)
        self.add_arc('sym-e10-2', (43, 39), (44, 36), radius_x=5, sweep=False)
        self.add_arc('sym-e13', (44, 36), (41, 31), radius_x=6, sweep=False)
        self.add_line('sym-e16', (41, 31), (40, 31))
        self.add_line('sym-e18', (40, 31), (24, 31))
        self.add_line('sym-e19', (24, 31), (8, 31))
        self.add_arc('sym-e20', (8, 31), (8, 25), radius_x=24)
        self.add_arc('sym-e21', (8, 25), (19, 12), radius_x=18)
        self.add_line('sym-e22', (19, 12), (21, 8))
        self.add_line('sym-e24', (21, 8), (24, 8))
        self.add_line('sym-e25', (24, 8), (27, 8))
        self.add_line('sym-e27', (27, 8), (29, 12))
        self.add_arc('sym-e28', (29, 12), (40, 25), radius_x=18)
        self.add_line('sym-e29', (40, 25), (40, 31))
        self.add_line('sym-e31', (19, 12), (19, 19))
        self.add_arc('sym-e32', (19, 19), (22, 22), radius_x=3, sweep=False)
        self.add_line('sym-e33', (22, 22), (24, 22))
        self.add_line('sym-e34', (24, 22), (26, 22))
        self.add_arc('sym-e35', (26, 22), (29, 19), radius_x=3, sweep=False)
        self.add_line('sym-e36', (29, 19), (29, 12))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e4', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e13', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c1', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
