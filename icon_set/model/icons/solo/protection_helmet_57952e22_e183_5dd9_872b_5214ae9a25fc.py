"""Protection helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57952e22-e183-5dd9-872b-5214ae9a25fc'
SOURCE_PATH = 'icons-json/protection/protection helmet_57952e22-e183-5dd9-872b-5214ae9a25fc.json'
AUTHOR = 'json_to_solo'

class ProtectionHelmet(Solo48):
    icon_id = 'protection-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('protection', 'helmet')

    def build(self):
        self.add_arc('sym-e0', (41, 32), (44, 36), radius_x=5)
        self.add_line('sym-e3', (44, 36), (44, 37))
        self.add_arc('sym-e4', (44, 37), (40, 39), radius_x=3)
        self.add_line('sym-e5', (40, 39), (26, 40))
        self.add_line('sym-e6', (26, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (22, 40))
        self.add_line('sym-e10', (22, 40), (8, 39))
        self.add_arc('sym-e11', (8, 39), (4, 37), radius_x=4)
        self.add_line('sym-e12', (4, 37), (4, 36))
        self.add_arc('sym-e15', (4, 36), (7, 32), radius_x=5)
        self.add_line('sym-e16', (7, 32), (24, 32))
        self.add_line('sym-e17', (24, 32), (41, 32))
        self.add_line('sym-e18', (41, 32), (41, 23))
        self.add_arc('sym-e19', (41, 23), (29, 9), radius_x=22, sweep=False)
        self.add_arc('sym-e20', (29, 9), (29, 10), radius_x=15, sweep=False)
        self.add_line('sym-e21', (29, 10), (29, 24))
        self.add_line('sym-e22', (29, 9), (27, 8))
        self.add_line('sym-e23', (27, 8), (25, 8))
        self.add_line('sym-e24', (25, 8), (24, 8))
        self.add_arc('sym-e25', (24, 8), (23, 8), radius_x=38)
        self.add_line('sym-e26', (23, 8), (21, 8))
        self.add_line('sym-e27', (21, 8), (19, 9))
        self.add_arc('sym-e28', (19, 9), (7, 23), radius_x=22, sweep=False)
        self.add_line('sym-e29', (7, 23), (7, 32))
        self.add_line('sym-e30', (19, 24), (19, 10))
        self.add_arc('sym-e31', (19, 10), (19, 9), radius_x=12, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
