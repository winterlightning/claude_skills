"""Drop shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c25c47b-1058-47e2-8f07-a986157c4478'
SOURCE_PATH = 'icons-json/design/drop shape_6c25c47b-1058-47e2-8f07-a986157c4478.json'
AUTHOR = 'json_to_solo'

class DropShape(Solo48):
    icon_id = 'drop-shape'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('drop', 'shape', 'design')

    def build(self):
        self.add_line('sym-e0', (21, 6), (11, 17))
        self.add_arc('sym-e1', (11, 17), (8, 26), radius_x=16, sweep=False)
        self.add_line('sym-e2', (8, 26), (8, 27))
        self.add_line('sym-e3', (8, 27), (8, 28))
        self.add_arc('sym-e4', (8, 28), (23, 44), radius_x=17, sweep=False)
        self.add_arc('sym-e5', (23, 44), (24, 44), radius_x=29)
        self.add_line('sym-e8', (24, 44), (25, 44))
        self.add_arc('sym-e9', (25, 44), (40, 28), radius_x=17, sweep=False)
        self.add_line('sym-e10', (40, 28), (40, 27))
        self.add_arc('sym-e11', (40, 27), (40, 26), radius_x=28)
        self.add_arc('sym-e12', (40, 26), (37, 17), radius_x=16, sweep=False)
        self.add_line('sym-e13', (37, 17), (27, 6))
        self.add_arc('sym-e14', (27, 6), (24, 4), radius_x=7)
        self.add_arc('sym-e17', (24, 4), (21, 6), radius_x=7)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e17', closed=True)
