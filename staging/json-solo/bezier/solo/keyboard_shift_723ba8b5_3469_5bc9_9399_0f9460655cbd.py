"""Keyboard shift (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '723ba8b5-3469-5bc9-9399-0f9460655cbd'
SOURCE_PATH = 'icons-json/interface-essential/keyboard shift_723ba8b5-3469-5bc9-9399-0f9460655cbd.json'
AUTHOR = 'json_to_solo'

class KeyboardShiftInterfaceEssential(Solo48):
    icon_id = 'keyboard-shift-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'shift', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 22), (32, 42))
        self.add_line('e1', (30, 44), (17, 44))
        self.add_line('e2', (16, 42), (16, 22))
        self.add_line('e3', (16, 22), (8, 22))
        self.add_line('e4', (8, 22), (24, 4))
        self.add_line('e5', (24, 4), (40, 22))
        self.add_line('e6', (40, 22), (32, 22))
        self.add_bezier('e7', (32, 42), ((32, 43.118), (31.68, 43.982), (30.712, 43.982)), ((30.442, 43.982), (30.269, 44), (30, 44)))
        self.add_bezier('e8', (17, 44), ((15.771, 43.473), (16.505, 43.364), (16, 42)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
