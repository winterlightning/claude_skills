"""Oval 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb3135a9-0f07-4fe3-96c8-fd473915e0c0'
SOURCE_PATH = 'icons-json/symbol/oval 1_fb3135a9-0f07-4fe3-96c8-fd473915e0c0.json'
AUTHOR = 'json_to_solo'

class Oval1(Solo48):
    icon_id = 'oval-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('oval', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (8, 24), (8, 23), radius_x=14, sweep=False)
        self.add_arc('sym-e1-1', (8, 23), (10, 14), radius_x=23)
        self.add_arc('sym-e1-2', (10, 14), (18, 5), radius_x=18)
        self.add_line('sym-e2', (18, 5), (23, 4))
        self.add_arc('sym-e3', (23, 4), (24, 4), radius_x=70, sweep=False)
        self.add_line('sym-e8', (24, 4), (25, 4))
        self.add_line('sym-e9', (25, 4), (30, 5))
        self.add_arc('sym-e10-1', (30, 5), (38, 14), radius_x=17)
        self.add_arc('sym-e10-2', (38, 14), (40, 23), radius_x=23)
        self.add_line('sym-e11', (40, 23), (40, 24))
        self.add_arc('sym-e12', (40, 24), (40, 25), radius_x=14, sweep=False)
        self.add_arc('sym-e13-1', (40, 25), (38, 34), radius_x=23)
        self.add_arc('sym-e13-2', (38, 34), (30, 43), radius_x=17)
        self.add_line('sym-e14', (30, 43), (25, 44))
        self.add_arc('sym-e15', (25, 44), (24, 44), radius_x=29, sweep=False)
        self.add_line('sym-e20', (24, 44), (23, 44))
        self.add_line('sym-e21', (23, 44), (18, 43))
        self.add_arc('sym-e22-1', (18, 43), (10, 34), radius_x=18)
        self.add_arc('sym-e22-2', (10, 34), (8, 25), radius_x=23)
        self.add_arc('sym-e23', (8, 25), (8, 24), radius_x=14, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e15', 'sym-e20', 'sym-e21', 'sym-e22-1', 'sym-e22-2', 'sym-e23', closed=True)
