"""Picker (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'faa9f9be-f031-5d45-90b8-776c436ca609'
SOURCE_PATH = 'icons-json/design/picker_faa9f9be-f031-5d45-90b8-776c436ca609.json'
AUTHOR = 'gpt-6'

class PickerDesign(Solo48):
    icon_id = 'picker-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'design')

    def build(self):
        self.add_line('sym-e0', (40, 18), (8, 18))
        self.add_arc('sym-e1-1', (14, 10), (16, 6), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e1-2', (16, 6), (23, 4))
        self.add_arc('sym-e2', (23, 4), (24, 4), radius_x=71, radius_y=71, large_arc=False, sweep=False)
        self.add_line('sym-e3', (24, 4), (25, 4))
        self.add_line('sym-e4-1', (25, 4), (32, 6))
        self.add_line('sym-e4-2', (32, 6), (34, 10))
        self.add_line('sym-e5', (34, 10), (34, 31))
        self.add_arc('sym-e6', (34, 31), (34, 32), radius_x=32, radius_y=32, large_arc=False, sweep=False)
        self.add_line('sym-e7', (34, 32), (33, 35))
        self.add_line('sym-e8', (33, 35), (29, 39))
        self.add_arc('sym-e9', (29, 39), (26, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e10', (26, 44), (22, 44))
        self.add_arc('sym-e12', (22, 44), (19, 39), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e13', (19, 39), (15, 35))
        self.add_line('sym-e14', (15, 35), (14, 32))
        self.add_arc('sym-e15', (14, 32), (14, 31), radius_x=43, radius_y=43, large_arc=False, sweep=True)
        self.add_line('sym-e16', (14, 31), (14, 10))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
