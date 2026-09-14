"""Layout 6 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a299b5ca-1eed-416f-a091-4bb307b869ec'
SOURCE_PATH = 'icons-json/interface-essential/layout 6_a299b5ca-1eed-416f-a091-4bb307b869ec.json'
AUTHOR = 'json_to_solo'

class Layout6(Solo48):
    icon_id = 'layout-6'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 24), (18, 24))
        self.add_line('sym-e1', (18, 24), (18, 42))
        self.add_line('sym-e2', (18, 42), (30, 42))
        self.add_line('sym-e3', (30, 42), (30, 24))
        self.add_line('sym-e4', (30, 24), (42, 24))
        self.add_line('sym-e5', (42, 24), (42, 40))
        self.add_line('sym-e6', (42, 40), (40, 42))
        self.add_line('sym-e7', (40, 42), (30, 42))
        self.add_line('sym-e8', (42, 24), (42, 8))
        self.add_line('sym-e10', (42, 8), (40, 6))
        self.add_line('sym-e11', (40, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (8, 6))
        self.add_line('sym-e13', (8, 6), (6, 8))
        self.add_line('sym-e15', (6, 8), (6, 24))
        self.add_line('sym-e16', (6, 24), (18, 24))
        self.add_line('sym-e17', (18, 42), (8, 42))
        self.add_arc('sym-e18', (8, 42), (6, 40), radius_x=4)
        self.add_line('sym-e19', (6, 40), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
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
