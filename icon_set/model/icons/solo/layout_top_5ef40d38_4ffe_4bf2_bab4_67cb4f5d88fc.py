"""Layout top (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout top_5ef40d38-4ffe-4bf2-bab4-67cb4f5d88fc.svg'
AUTHOR = 'gpt-6'

class LayoutTop(Solo48):
    icon_id = 'layout-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'top', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 16), (42, 16))
        self.add_line('sym-e1', (42, 16), (42, 40))
        self.add_line('sym-e2', (42, 40), (40, 42))
        self.add_line('sym-e3', (40, 42), (8, 42))
        self.add_arc('sym-e5', (8, 42), (6, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e6', (6, 40), (6, 8))
        self.add_arc('sym-e9', (6, 8), (8, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e11', (8, 6), (40, 6))
        self.add_arc('sym-e14', (40, 6), (42, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e16', (42, 8), (42, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e11', 'sym-e14', 'sym-e16', closed=False)
