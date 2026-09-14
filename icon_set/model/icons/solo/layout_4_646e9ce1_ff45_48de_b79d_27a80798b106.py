"""Layout 4 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '646e9ce1-ff45-48de-b79d-27a80798b106'
SOURCE_PATH = 'icons-json/interface-essential/layout 4_646e9ce1-ff45-48de-b79d-27a80798b106.json'
AUTHOR = 'json_to_solo'

class Layout4(Solo48):
    icon_id = 'layout-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 31), (18, 31))
        self.add_line('sym-e1', (18, 31), (18, 18))
        self.add_line('sym-e2', (18, 18), (30, 18))
        self.add_line('sym-e3', (30, 18), (30, 31))
        self.add_line('sym-e4', (30, 31), (42, 31))
        self.add_line('sym-e5', (42, 31), (42, 40))
        self.add_line('sym-e6', (42, 40), (42, 41))
        self.add_line('sym-e7', (42, 41), (40, 42))
        self.add_line('sym-e9', (40, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (8, 42))
        self.add_line('sym-e12', (8, 42), (6, 41))
        self.add_line('sym-e13', (6, 41), (6, 40))
        self.add_line('sym-e14', (6, 40), (6, 31))
        self.add_line('sym-e15', (6, 31), (18, 31))
        self.add_line('sym-e16', (30, 18), (42, 18))
        self.add_line('sym-e17', (42, 18), (42, 31))
        self.add_line('sym-e18', (42, 18), (42, 8))
        self.add_arc('sym-e19', (42, 8), (41, 6), radius_x=2)
        self.add_line('sym-e20', (41, 6), (40, 6))
        self.add_line('sym-e21', (40, 6), (24, 6))
        self.add_line('sym-e22', (24, 6), (8, 6))
        self.add_line('sym-e23', (8, 6), (7, 6))
        self.add_line('sym-e24', (7, 6), (6, 8))
        self.add_line('sym-e25', (6, 8), (6, 18))
        self.add_line('sym-e26', (6, 18), (18, 18))
        self.add_line('sym-e27', (6, 31), (6, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c2', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c3', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
