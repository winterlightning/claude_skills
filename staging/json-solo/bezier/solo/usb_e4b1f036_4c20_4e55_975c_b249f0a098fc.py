"""Usb (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'icons-json/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.json'
AUTHOR = 'json_to_solo'

class UsbState(Solo48):
    icon_id = 'usb-state'
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
        self.add_bezier('sym-e5', (10, 17), ((8.338, 17.564), (8.763, 17.773), (8, 19)))
        self.add_line('sym-e6', (8, 19), (8, 38))
        self.add_bezier('sym-e7', (8, 38), ((8, 40.564), (12.468, 44), (16, 44)))
        self.add_bezier('sym-e8', (16, 44), ((16.062, 44), (16.938, 44), (17, 44)))
        self.add_line('sym-e9', (17, 44), (24, 44))
        self.add_line('sym-e10', (24, 44), (31, 44))
        self.add_bezier('sym-e11', (31, 44), ((31.062, 44), (31.938, 44), (32, 44)))
        self.add_bezier('sym-e12', (32, 44), ((35.532, 44), (40, 40.564), (40, 38)))
        self.add_line('sym-e13', (40, 38), (40, 19))
        self.add_bezier('sym-e14', (40, 19), ((39.237, 17.773), (39.662, 17.564), (38, 17)))
        self.add_line('sym-e15', (38, 17), (35, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
