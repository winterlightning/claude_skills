"""O (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50d906f5-5c18-404b-8dc8-1c2a2ce400ee'
SOURCE_PATH = 'icons-json/typeface/o_50d906f5-5c18-404b-8dc8-1c2a2ce400ee.json'
AUTHOR = 'json_to_solo'

class O(Solo48):
    icon_id = 'o'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('o', 'typeface')

    def build(self):
        self.add_arc('sym-e0', (24, 44), (25, 44), radius_x=29)
        self.add_arc('sym-e1-1', (25, 44), (36, 38), radius_x=14, sweep=False)
        self.add_arc('sym-e1-2', (36, 38), (39, 32), radius_x=20, sweep=False)
        self.add_arc('sym-e1-3', (39, 32), (40, 25), radius_x=26, sweep=False)
        self.add_line('sym-e2', (40, 25), (40, 24))
        self.add_line('sym-e3', (40, 24), (40, 23))
        self.add_arc('sym-e4-1', (40, 23), (39, 16), radius_x=26, sweep=False)
        self.add_arc('sym-e4-2', (39, 16), (36, 10), radius_x=20, sweep=False)
        self.add_arc('sym-e4-3', (36, 10), (25, 4), radius_x=14, sweep=False)
        self.add_line('sym-e5', (25, 4), (24, 4))
        self.add_arc('sym-e6', (24, 4), (23, 4), radius_x=71)
        self.add_arc('sym-e7-1', (23, 4), (12, 10), radius_x=14, sweep=False)
        self.add_arc('sym-e7-2', (12, 10), (9, 16), radius_x=20, sweep=False)
        self.add_arc('sym-e7-3', (9, 16), (8, 23), radius_x=26, sweep=False)
        self.add_line('sym-e8', (8, 23), (8, 24))
        self.add_line('sym-e9', (8, 24), (8, 25))
        self.add_arc('sym-e10-1', (8, 25), (9, 32), radius_x=26, sweep=False)
        self.add_arc('sym-e10-2', (9, 32), (12, 38), radius_x=20, sweep=False)
        self.add_arc('sym-e10-3', (12, 38), (23, 44), radius_x=14, sweep=False)
        self.add_line('sym-e11', (23, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1-1', 'sym-e1-2', 'sym-e1-3', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e4-3', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e7-3', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e10-3', 'sym-e11', closed=True)
