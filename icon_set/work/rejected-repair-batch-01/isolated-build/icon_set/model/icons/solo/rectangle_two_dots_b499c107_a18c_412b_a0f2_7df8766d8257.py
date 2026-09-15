"""Rectangle two dots (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b499c107-a18c-412b-a0f2-7df8766d8257'
SOURCE_PATH = 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'
AUTHOR = 'gpt-6'

class RectangleTwoDots(Solo48):
    icon_id = 'rectangle-two-dots'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'two', 'dots', 'state')

    def build(self):
        self.add_arc('sym-e0', (24, 34), (24, 35), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_arc('sym-e1', (24, 15), (24, 16), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e2', (24, 44), (10, 44))
        self.add_line('sym-e3', (10, 44), (8, 42))
        self.add_line('sym-e4', (8, 42), (8, 7))
        self.add_line('sym-e7', (8, 7), (9, 4))
        self.add_line('sym-e8', (9, 4), (39, 4))
        self.add_line('sym-e12', (39, 4), (40, 7))
        self.add_line('sym-e14', (40, 7), (40, 42))
        self.add_line('sym-e16', (40, 42), (38, 44))
        self.add_line('sym-e17', (38, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', closed=False)
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e12', 'sym-e14', 'sym-e16', 'sym-e17', closed=True)
