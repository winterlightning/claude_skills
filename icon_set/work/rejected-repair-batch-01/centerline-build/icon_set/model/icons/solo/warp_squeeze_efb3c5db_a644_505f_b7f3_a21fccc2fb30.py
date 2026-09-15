"""Warp squeeze (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'efb3c5db-a644-505f-b7f3-a21fccc2fb30'
SOURCE_PATH = 'pictographic-primitives/design/warp squeeze_efb3c5db-a644-505f-b7f3-a21fccc2fb30.svg'
AUTHOR = 'gpt-6'

class WarpSqueeze(Solo48):
    icon_id = 'warp-squeeze'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'squeeze', 'design')

    def build(self):
        self.add_line('sym-e1-1', (24, 44), (17, 43))
        self.add_arc('sym-e1-2', (17, 43), (11, 40), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e2', (11, 40), (9, 38))
        self.add_arc('sym-e3', (9, 38), (8, 38), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e4', (8, 38), (14, 32))
        self.add_arc('sym-e6', (14, 32), (11, 13), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e7', (11, 13), (8, 10))
        self.add_line('sym-e9', (8, 10), (11, 8))
        self.add_arc('sym-e10', (11, 8), (23, 4), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_line('sym-e11', (23, 4), (25, 4))
        self.add_arc('sym-e15', (25, 4), (37, 8), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_arc('sym-e16', (37, 8), (40, 10), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_arc('sym-e18', (40, 10), (37, 13), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (37, 13), (34, 32), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e20', (34, 32), (40, 38))
        self.add_arc('sym-e22', (40, 38), (39, 38), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e23', (39, 38), (37, 40))
        self.add_arc('sym-e24-1', (37, 40), (31, 43), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e24-2', (31, 43), (24, 44))
        self.add_contour('sym-c0', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24-1', 'sym-e24-2', closed=True)
