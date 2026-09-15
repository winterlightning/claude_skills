"""Layout 3 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b6bc3c6-f4b2-4636-8a31-131c24535fca'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 3_4b6bc3c6-f4b2-4636-8a31-131c24535fca.svg'
AUTHOR = 'gpt-6'

class Layout3(Solo48):
    icon_id = 'layout-3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 31))
        self.add_line('sym-e1', (24, 31), (6, 31))
        self.add_line('sym-e2', (6, 31), (6, 40))
        self.add_line('sym-e3', (6, 40), (8, 42))
        self.add_line('sym-e5', (8, 42), (40, 42))
        self.add_line('sym-e8', (40, 42), (42, 40))
        self.add_line('sym-e9', (42, 40), (42, 31))
        self.add_line('sym-e10', (42, 31), (24, 31))
        self.add_line('sym-e11', (6, 20), (42, 20))
        self.add_line('sym-e12', (42, 20), (42, 31))
        self.add_line('sym-e13', (6, 31), (6, 8))
        self.add_line('sym-e15', (6, 8), (8, 6))
        self.add_line('sym-e16', (8, 6), (40, 6))
        self.add_line('sym-e18', (40, 6), (42, 8))
        self.add_line('sym-e19', (42, 8), (42, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12', closed=False)
        self.add_contour('sym-c2', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
