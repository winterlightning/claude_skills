"""Four square grid (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '03604e35-e3e4-40dd-8693-086f35d62ddf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/Four Square Grid_03604e35-e3e4-40dd-8693-086f35d62ddf.svg'
AUTHOR = 'gpt-6'

class FourSquareGrid(Solo48):
    icon_id = 'four-square-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('four', 'square', 'grid', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (6, 24), (42, 24))
        self.add_line('sym-e2', (42, 24), (42, 8))
        self.add_arc('sym-e3', (42, 8), (40, 6), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e4', (40, 6), (24, 6))
        self.add_line('sym-e5', (24, 6), (24, 42))
        self.add_line('sym-e7', (24, 42), (8, 42))
        self.add_arc('sym-e8', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e9', (6, 40), (6, 8))
        self.add_arc('sym-e11', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e12', (8, 6), (24, 6))
        self.add_line('sym-e13', (42, 24), (42, 40))
        self.add_arc('sym-e14', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e15', (40, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', closed=False)
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
