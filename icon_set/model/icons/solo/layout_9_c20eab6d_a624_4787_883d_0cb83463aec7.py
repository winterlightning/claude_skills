"""Layout 9 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c20eab6d-a624-4787-883d-0cb83463aec7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 9_c20eab6d-a624-4787-883d-0cb83463aec7.svg'
AUTHOR = 'gpt-6'

class Layout9(Solo48):
    icon_id = 'layout-9'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (22, 24), (42, 24))
        self.add_line('sym-e1', (42, 24), (42, 40))
        self.add_line('sym-e2', (42, 40), (40, 42))
        self.add_line('sym-e3', (40, 42), (22, 42))
        self.add_line('sym-e4', (22, 42), (22, 6))
        self.add_line('sym-e6', (22, 6), (40, 6))
        self.add_line('sym-e7', (40, 6), (42, 8))
        self.add_line('sym-e8', (42, 8), (42, 24))
        self.add_line('sym-e9', (22, 42), (8, 42))
        self.add_arc('sym-e10', (8, 42), (6, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e11', (6, 40), (6, 8))
        self.add_line('sym-e13', (6, 8), (8, 6))
        self.add_line('sym-e14', (8, 6), (22, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', closed=False)
        self.add_contour('sym-c1', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
