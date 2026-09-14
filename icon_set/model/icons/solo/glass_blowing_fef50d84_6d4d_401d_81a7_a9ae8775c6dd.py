"""Glass blowing (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fef50d84-6d4d-401d-81a7-a9ae8775c6dd'
SOURCE_PATH = 'icons-json/hobbies/glass blowing_fef50d84-6d4d-401d-81a7-a9ae8775c6dd.json'
AUTHOR = 'json_to_solo'

class GlassBlowing(Solo48):
    icon_id = 'glass-blowing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('glass', 'blowing', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (6, 42), (17, 31))
        self.add_line('sym-e1', (17, 31), (14, 29))
        self.add_arc('sym-e2', (14, 29), (16, 24), radius_x=4)
        self.add_arc('sym-e3', (16, 24), (16, 22), radius_x=9)
        self.add_arc('sym-e4', (16, 22), (16, 17), radius_x=13)
        self.add_arc('sym-e5', (16, 17), (30, 6), radius_x=15)
        self.add_line('sym-e7', (30, 6), (31, 6))
        self.add_line('sym-e8', (31, 6), (39, 9))
        self.add_line('sym-e9', (39, 9), (42, 17))
        self.add_line('sym-e10', (42, 17), (42, 18))
        self.add_arc('sym-e12', (42, 18), (31, 32), radius_x=15)
        self.add_arc('sym-e13', (31, 32), (26, 32), radius_x=13)
        self.add_arc('sym-e14', (26, 32), (24, 32), radius_x=9)
        self.add_arc('sym-e15', (24, 32), (19, 34), radius_x=4)
        self.add_line('sym-e16', (19, 34), (17, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
