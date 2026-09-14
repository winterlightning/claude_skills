"""Picker (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c14d32f5-65d7-5567-a4d2-48d6e8e4dcb4'
SOURCE_PATH = 'icons-json/design/picker_c14d32f5-65d7-5567-a4d2-48d6e8e4dcb4.json'
AUTHOR = 'json_to_solo'

class PickerC14d32f5(Solo48):
    icon_id = 'picker-c14d32f5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'design')

    def build(self):
        self.add_line('sym-e0', (40, 19), (8, 19))
        self.add_line('sym-e1', (24, 4), (24, 4))
        self.add_arc('sym-e3', (24, 4), (28, 5), radius_x=11)
        self.add_arc('sym-e4', (28, 5), (34, 10), radius_x=7)
        self.add_line('sym-e5', (34, 10), (34, 31))
        self.add_line('sym-e6', (34, 31), (32, 36))
        self.add_line('sym-e7', (32, 36), (28, 39))
        self.add_arc('sym-e8', (28, 39), (26, 44), radius_x=4)
        self.add_arc('sym-e9', (26, 44), (24, 44), radius_x=6, sweep=False)
        self.add_arc('sym-e12', (24, 44), (22, 44), radius_x=6, sweep=False)
        self.add_arc('sym-e13', (22, 44), (20, 39), radius_x=4)
        self.add_line('sym-e14', (20, 39), (16, 36))
        self.add_arc('sym-e15', (16, 36), (14, 31), radius_x=6)
        self.add_line('sym-e16', (14, 31), (14, 10))
        self.add_arc('sym-e17', (14, 10), (20, 5), radius_x=8)
        self.add_arc('sym-e18', (20, 5), (24, 4), radius_x=11)
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
