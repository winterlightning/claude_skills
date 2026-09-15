"""Arrow up to bracket (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97afd5bd-3601-4717-bdb0-129f09ae3a6c'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow up to bracket_97afd5bd-3601-4717-bdb0-129f09ae3a6c.svg'
AUTHOR = 'gpt-6'

class ArrowUpToBracket(Solo48):
    icon_id = 'arrow-up-to-bracket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'up', 'to', 'bracket', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 31))
        self.add_line('sym-e1', (15, 16), (24, 6))
        self.add_line('sym-e2', (24, 6), (33, 16))
        self.add_line('sym-e3', (6, 32), (6, 37))
        self.add_arc('sym-e4-1', (6, 37), (7, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e4-2', (7, 40), (10, 42), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e5', (10, 42), (38, 42))
        self.add_arc('sym-e7-1', (38, 42), (41, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e7-2', (41, 40), (42, 37), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e8', (42, 37), (42, 32))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', closed=False)
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e7-1', 'sym-e7-2', 'sym-e8', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
