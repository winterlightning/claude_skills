"""Up double (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f643becf-a00c-4502-9a86-e70d6557b7b0'
SOURCE_PATH = 'icons-json/arrows/up double_f643becf-a00c-4502-9a86-e70d6557b7b0.json'
AUTHOR = 'json_to_solo'

class UpDoubleArrows(Solo48):
    icon_id = 'up-double-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('up', 'double', 'arrows')

    def build(self):
        self.add_line('sym-e0', (6, 10), (10, 6))
        self.add_line('sym-e1', (10, 6), (15, 11))
        self.add_line('sym-e2', (10, 6), (10, 29))
        self.add_arc('sym-e3', (10, 29), (11, 32), radius_x=11, sweep=False)
        self.add_arc('sym-e4', (11, 32), (23, 42), radius_x=14, sweep=False)
        self.add_arc('sym-e5', (23, 42), (24, 42), radius_x=27)
        self.add_arc('sym-e8', (24, 42), (25, 42), radius_x=29)
        self.add_arc('sym-e9', (25, 42), (37, 32), radius_x=14, sweep=False)
        self.add_line('sym-e10', (37, 32), (38, 29))
        self.add_line('sym-e11', (38, 29), (38, 6))
        self.add_line('sym-e12', (38, 6), (42, 10))
        self.add_line('sym-e13', (33, 11), (38, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
