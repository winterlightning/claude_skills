"""Vertical rectangcle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b24697a2-f23c-47f5-882a-55246a5eb7ad'
SOURCE_PATH = 'pictographic-primitives/symbol/vertical rectangcle_b24697a2-f23c-47f5-882a-55246a5eb7ad.svg'
AUTHOR = 'gpt-6'

class VerticalRectangcle(Solo48):
    icon_id = 'vertical-rectangcle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vertical', 'rectangcle', 'symbol')

    def build(self):
        self.add_line('sym-e0', (37, 44), (11, 44))
        self.add_arc('sym-e2', (11, 44), (10, 44), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (10, 44), (8, 41), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e4', (8, 41), (8, 7))
        self.add_arc('sym-e6', (8, 7), (10, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e7', (10, 4), (38, 4))
        self.add_arc('sym-e11', (38, 4), (40, 7), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e12', (40, 7), (40, 41))
        self.add_arc('sym-e14', (40, 41), (38, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e15', (38, 44), (37, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
