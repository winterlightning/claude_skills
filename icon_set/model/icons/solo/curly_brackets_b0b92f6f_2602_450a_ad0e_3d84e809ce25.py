"""Curly brackets (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0b92f6f-2602-450a-ad0e-3d84e809ce25'
SOURCE_PATH = 'pictographic-primitives/programing/curly brackets_b0b92f6f-2602-450a-ad0e-3d84e809ce25.svg'
AUTHOR = 'gpt-6'

class CurlyBrackets(Solo48):
    icon_id = 'curly-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')

    def build(self):
        self.add_arc('sym-e0', (14, 6), (10, 10), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e1', (10, 10), (10, 11), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e2', (10, 11), (10, 19))
        self.add_line('sym-e4', (10, 19), (6, 24))
        self.add_line('sym-e5', (6, 24), (10, 29))
        self.add_line('sym-e6', (10, 29), (10, 37))
        self.add_arc('sym-e8', (10, 37), (10, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e9', (10, 38), (14, 42), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (34, 6), (38, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (38, 10), (38, 11), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e12', (38, 11), (38, 19))
        self.add_line('sym-e14', (38, 19), (42, 24))
        self.add_line('sym-e15', (42, 24), (38, 29))
        self.add_arc('sym-e16', (38, 29), (38, 31), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e17', (38, 31), (38, 37))
        self.add_arc('sym-e18', (38, 37), (38, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e19', (38, 38), (34, 42), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', closed=False)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=False)
