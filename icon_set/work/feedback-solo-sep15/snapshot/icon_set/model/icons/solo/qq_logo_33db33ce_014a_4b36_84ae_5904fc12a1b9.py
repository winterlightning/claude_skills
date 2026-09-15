"""Qq logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33db33ce-014a-4b36-84ae-5904fc12a1b9'
SOURCE_PATH = 'pictographic-primitives/logos/qq logo_33db33ce-014a-4b36-84ae-5904fc12a1b9.svg'
AUTHOR = 'gpt-6'

class QqLogo(Solo48):
    icon_id = 'qq-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('qq', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e1', (24, 4), (34, 12), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('sym-e2', (34, 12), (35, 15))
        self.add_arc('sym-e3', (35, 15), (35, 18), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e4', (35, 18), (38, 25))
        self.add_arc('sym-e5', (38, 25), (40, 32), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_line('sym-e7', (40, 32), (40, 33))
        self.add_arc('sym-e8', (40, 33), (38, 34), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e9', (38, 34), (37, 34))
        self.add_line('sym-e10', (37, 34), (36, 32))
        self.add_arc('sym-e11', (36, 32), (33, 39), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_line('sym-e12', (33, 39), (37, 39))
        self.add_line('sym-e14-1', (37, 39), (36, 42))
        self.add_line('sym-e14-2', (36, 42), (33, 44))
        self.add_arc('sym-e15', (33, 44), (30, 44), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_line('sym-e16', (30, 44), (27, 44))
        self.add_arc('sym-e17', (27, 44), (24, 43), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e20', (24, 43), (21, 44), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e21', (21, 44), (18, 44))
        self.add_arc('sym-e22', (18, 44), (15, 44), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_line('sym-e23-1', (15, 44), (12, 42))
        self.add_line('sym-e23-2', (12, 42), (11, 39))
        self.add_line('sym-e24', (11, 39), (15, 39))
        self.add_arc('sym-e26', (15, 39), (12, 32), radius_x=32, radius_y=32, large_arc=False, sweep=False)
        self.add_line('sym-e27', (12, 32), (11, 34))
        self.add_line('sym-e28', (11, 34), (10, 34))
        self.add_arc('sym-e29', (10, 34), (8, 33), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e30', (8, 33), (8, 32))
        self.add_arc('sym-e32', (8, 32), (10, 25), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_line('sym-e33', (10, 25), (13, 18))
        self.add_line('sym-e34', (13, 18), (13, 15))
        self.add_arc('sym-e35', (13, 15), (14, 12), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('sym-e36', (14, 12), (24, 4), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23-1', 'sym-e23-2', 'sym-e24', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', closed=True)
