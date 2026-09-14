"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH = 'icons-json/protection/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.json'
AUTHOR = 'json_to_solo'

class HelmetProtection(Solo48):
    icon_id = 'helmet-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_arc('sym-e0', (40, 32), (40, 26), radius_x=20, sweep=False)
        self.add_arc('sym-e1', (40, 26), (28, 13), radius_x=19, sweep=False)
        self.add_line('sym-e2', (28, 13), (28, 12))
        self.add_line('sym-e3-1', (28, 12), (27, 9))
        self.add_line('sym-e3-2', (27, 9), (24, 8))
        self.add_line('sym-e4-1', (24, 8), (21, 9))
        self.add_line('sym-e4-2', (21, 9), (20, 12))
        self.add_line('sym-e5', (20, 12), (20, 13))
        self.add_arc('sym-e6', (20, 13), (8, 26), radius_x=18, sweep=False)
        self.add_arc('sym-e7', (8, 26), (8, 32), radius_x=20, sweep=False)
        self.add_arc('sym-e8-1', (8, 32), (5, 33), radius_x=4, sweep=False)
        self.add_arc('sym-e8-2', (5, 33), (4, 36), radius_x=5, sweep=False)
        self.add_line('sym-e9', (4, 36), (4, 37))
        self.add_line('sym-e10', (4, 37), (4, 38))
        self.add_arc('sym-e12', (4, 38), (6, 40), radius_x=2, sweep=False)
        self.add_arc('sym-e13', (6, 40), (7, 40), radius_x=1)
        self.add_line('sym-e14', (7, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (41, 40))
        self.add_line('sym-e16', (41, 40), (42, 40))
        self.add_arc('sym-e17', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('sym-e19', (44, 38), (44, 37), radius_x=38)
        self.add_arc('sym-e20', (44, 37), (44, 36), radius_x=38)
        self.add_arc('sym-e21-1', (44, 36), (43, 33), radius_x=5, sweep=False)
        self.add_arc('sym-e21-2', (43, 33), (40, 32), radius_x=4, sweep=False)
        self.add_line('sym-e23', (40, 32), (39, 32))
        self.add_line('sym-e24', (39, 32), (29, 32))
        self.add_line('sym-e25', (29, 32), (28, 32))
        self.add_line('sym-e26', (28, 32), (28, 13))
        self.add_line('sym-e27', (28, 32), (24, 32))
        self.add_line('sym-e28', (24, 32), (20, 32))
        self.add_line('sym-e29', (20, 32), (20, 13))
        self.add_line('sym-e30', (9, 32), (19, 32))
        self.add_line('sym-e31', (19, 32), (20, 32))
        self.add_line('sym-e33', (8, 32), (9, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21-1', 'sym-e21-2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c1', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c3', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
