"""Usb (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = 'gpt-6'

class Usb(Solo48):
    icon_id = 'usb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('usb', 'state')

    def build(self):
        self.add_line('sym-e0', (13, 17), (35, 17))
        self.add_line('sym-e1', (35, 17), (35, 4))
        self.add_line('sym-e2', (35, 4), (13, 4))
        self.add_line('sym-e3', (13, 4), (13, 17))
        self.add_line('sym-e4', (13, 17), (10, 17))
        self.add_arc('sym-e5', (10, 17), (8, 19), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e6', (8, 19), (8, 38))
        self.add_arc('sym-e7', (8, 38), (16, 44), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (16, 44), (17, 44), radius_x=26, radius_y=26, large_arc=False, sweep=True)
        self.add_line('sym-e9', (17, 44), (31, 44))
        self.add_arc('sym-e11', (31, 44), (32, 44), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (32, 44), (40, 38), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e13', (40, 38), (40, 19))
        self.add_arc('sym-e14', (40, 19), (38, 17), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e15', (38, 17), (35, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
