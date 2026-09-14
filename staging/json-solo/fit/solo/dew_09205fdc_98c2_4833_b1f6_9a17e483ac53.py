"""Dew (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09205fdc-98c2-4833-b1f6-9a17e483ac53'
SOURCE_PATH = 'icons-json/_uncategorized_14/dew_09205fdc-98c2-4833-b1f6-9a17e483ac53.json'
AUTHOR = 'json_to_solo'

class DewUncategorized(Solo48):
    icon_id = 'dew-uncategorized'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('dew', '_uncategorized')

    def build(self):
        self.add_line('sym-e0', (24, 44), (25, 44))
        self.add_arc('sym-e1', (25, 44), (40, 31), radius_x=16, sweep=False)
        self.add_arc('sym-e3', (40, 31), (40, 30), radius_x=32)
        self.add_arc('sym-e4', (40, 30), (29, 10), radius_x=42, sweep=False)
        self.add_line('sym-e5', (29, 10), (25, 5))
        self.add_line('sym-e6', (25, 5), (24, 4))
        self.add_line('sym-e7', (24, 4), (23, 5))
        self.add_line('sym-e8', (23, 5), (19, 10))
        self.add_arc('sym-e9', (19, 10), (8, 30), radius_x=42, sweep=False)
        self.add_line('sym-e10', (8, 30), (8, 31))
        self.add_arc('sym-e12', (8, 31), (23, 44), radius_x=16, sweep=False)
        self.add_arc('sym-e13', (23, 44), (24, 44), radius_x=55)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', closed=True)
