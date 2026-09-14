"""Layout 14 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5e174ee-dcd0-40ce-be3f-dbcdd1f52500'
SOURCE_PATH = 'icons-json/interface-essential/layout 14_a5e174ee-dcd0-40ce-be3f-dbcdd1f52500.json'
AUTHOR = 'json_to_solo'

class Layout14(Solo48):
    icon_id = 'layout-14'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 29), (24, 42))
        self.add_line('sym-e1', (24, 42), (40, 42))
        self.add_line('sym-e2', (40, 42), (42, 40))
        self.add_line('sym-e3', (42, 40), (42, 29))
        self.add_line('sym-e4', (42, 29), (24, 29))
        self.add_line('sym-e5', (24, 29), (24, 16))
        self.add_line('sym-e6', (24, 16), (42, 16))
        self.add_line('sym-e7', (42, 16), (42, 29))
        self.add_line('sym-e8', (42, 16), (42, 8))
        self.add_line('sym-e9', (42, 8), (40, 6))
        self.add_line('sym-e10', (40, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (8, 6))
        self.add_line('sym-e12', (8, 6), (6, 8))
        self.add_line('sym-e13', (6, 8), (6, 16))
        self.add_line('sym-e14', (6, 16), (6, 29))
        self.add_line('sym-e15', (6, 29), (24, 29))
        self.add_line('sym-e16', (6, 29), (6, 40))
        self.add_line('sym-e17', (6, 40), (8, 42))
        self.add_line('sym-e18', (8, 42), (24, 42))
        self.add_line('sym-e19', (24, 16), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c2', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
