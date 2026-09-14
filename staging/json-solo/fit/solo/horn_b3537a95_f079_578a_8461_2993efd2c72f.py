"""Horn (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3537a95-f079-578a-8461-2993efd2c72f'
SOURCE_PATH = 'icons-json/transportation/horn_b3537a95-f079-578a-8461-2993efd2c72f.json'
AUTHOR = 'json_to_solo'

class HornB3537a95(Solo48):
    icon_id = 'horn-b3537a95'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('horn', 'transportation')

    def build(self):
        self.add_line('sym-e0', (4, 10), (4, 38))
        self.add_arc('sym-e1', (4, 38), (8, 33), radius_x=26, sweep=False)
        self.add_arc('sym-e2', (8, 33), (24, 27), radius_x=32)
        self.add_arc('sym-e3', (24, 27), (33, 26), radius_x=57)
        self.add_line('sym-e4', (33, 26), (33, 24))
        self.add_arc('sym-e7', (33, 24), (33, 22), radius_x=5)
        self.add_arc('sym-e8', (33, 22), (24, 21), radius_x=57)
        self.add_arc('sym-e9', (24, 21), (8, 15), radius_x=32)
        self.add_arc('sym-e10', (8, 15), (4, 10), radius_x=26)
        self.add_line('sym-e11', (4, 10), (4, 8))
        self.add_arc('sym-e12', (33, 22), (37, 19), radius_x=6)
        self.add_arc('sym-e13', (37, 19), (44, 24), radius_x=6)
        self.add_arc('sym-e16', (44, 24), (37, 29), radius_x=6)
        self.add_arc('sym-e17', (37, 29), (33, 26), radius_x=6)
        self.add_line('sym-e18', (4, 38), (4, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c2', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
