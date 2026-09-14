"""Ceramic (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9b91a34-6703-4faf-a865-315e9a81c798'
SOURCE_PATH = 'icons-json/hobbies/ceramic_d9b91a34-6703-4faf-a865-315e9a81c798.json'
AUTHOR = 'json_to_solo'

class Ceramic(Solo48):
    icon_id = 'ceramic'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('ceramic', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (24, 44), (15, 44))
        self.add_arc('sym-e1', (15, 44), (14, 37), radius_x=11, sweep=False)
        self.add_line('sym-e2', (14, 37), (11, 32))
        self.add_arc('sym-e3', (11, 32), (8, 23), radius_x=20)
        self.add_line('sym-e4', (8, 23), (8, 22))
        self.add_arc('sym-e6', (8, 22), (10, 16), radius_x=12)
        self.add_line('sym-e7', (10, 16), (14, 10))
        self.add_arc('sym-e8', (14, 10), (15, 4), radius_x=8, sweep=False)
        self.add_line('sym-e9', (15, 4), (24, 4))
        self.add_line('sym-e10', (24, 4), (33, 4))
        self.add_arc('sym-e11', (33, 4), (34, 10), radius_x=8, sweep=False)
        self.add_line('sym-e12', (34, 10), (38, 16))
        self.add_arc('sym-e13', (38, 16), (40, 22), radius_x=11)
        self.add_line('sym-e15', (40, 22), (40, 23))
        self.add_arc('sym-e16', (40, 23), (37, 32), radius_x=20)
        self.add_line('sym-e17', (37, 32), (34, 37))
        self.add_arc('sym-e18', (34, 37), (33, 44), radius_x=11, sweep=False)
        self.add_line('sym-e19', (33, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
