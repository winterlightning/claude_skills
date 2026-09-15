"""Cell border full (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '074b16f1-51d9-4e55-89de-bf26c54041c1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cell border full_074b16f1-51d9-4e55-89de-bf26c54041c1.svg'
AUTHOR = 'gpt-6'

class CellBorderFull(Solo48):
    icon_id = 'cell-border-full'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cell', 'border', 'full', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 24), (6, 24))
        self.add_line('sym-e2', (6, 24), (6, 8))
        self.add_line('sym-e4', (6, 8), (8, 6))
        self.add_line('sym-e5', (8, 6), (40, 6))
        self.add_line('sym-e7', (40, 6), (42, 8))
        self.add_line('sym-e8', (42, 8), (42, 40))
        self.add_line('sym-e10', (42, 40), (40, 42))
        self.add_line('sym-e11', (40, 42), (8, 42))
        self.add_arc('sym-e13', (8, 42), (6, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e15', (6, 40), (6, 24))
        self.add_line('sym-e16', (24, 6), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', closed=False)
        self.add_contour('sym-c1', 'sym-e16', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
