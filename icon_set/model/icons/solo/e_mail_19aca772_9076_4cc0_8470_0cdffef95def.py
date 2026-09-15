"""E mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '19aca772-9076-4cc0-8470-0cdffef95def'
SOURCE_PATH = 'icons-json/symbol/e mail_19aca772-9076-4cc0-8470-0cdffef95def.json'
AUTHOR = 'gpt-6'

class EMail(Solo48):
    icon_id = 'e-mail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('e', 'mail', 'symbol')

    def build(self):
        self.add_line('sym-e0', (43, 39), (41, 40))
        self.add_arc('sym-e1', (41, 40), (40, 40), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_line('sym-e2', (40, 40), (8, 40))
        self.add_arc('sym-e3', (8, 40), (7, 40), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e4', (7, 40), (5, 39))
        self.add_line('sym-e5', (5, 39), (19, 24))
        self.add_arc('sym-e6', (19, 24), (24, 27), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (24, 27), (29, 24), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('sym-e8', (29, 24), (43, 39))
        self.add_line('sym-e9', (43, 39), (44, 36))
        self.add_line('sym-e10', (44, 36), (44, 12))
        self.add_line('sym-e11', (44, 12), (29, 24))
        self.add_line('sym-e12', (44, 12), (43, 10))
        self.add_arc('sym-e13', (43, 10), (40, 8), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e14', (40, 8), (8, 8))
        self.add_arc('sym-e16', (8, 8), (5, 10), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e17', (5, 10), (4, 12))
        self.add_line('sym-e18', (4, 12), (19, 24))
        self.add_line('sym-e19', (5, 39), (4, 36))
        self.add_line('sym-e20', (4, 36), (4, 12))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=False)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', closed=False)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
