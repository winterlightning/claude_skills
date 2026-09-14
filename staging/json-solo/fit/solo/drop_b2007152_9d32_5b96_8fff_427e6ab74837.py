"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2007152-9d32-5b96-8fff-427e6ab74837'
SOURCE_PATH = 'icons-json/smileys/drop_b2007152-9d32-5b96-8fff-427e6ab74837.json'
AUTHOR = 'json_to_solo'

class Drop(Solo48):
    icon_id = 'drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_line('sym-e2', (24, 44), (25, 44))
        self.add_arc('sym-e3', (25, 44), (40, 30), radius_x=16, sweep=False)
        self.add_line('sym-e5', (40, 30), (40, 29))
        self.add_arc('sym-e6', (40, 29), (29, 10), radius_x=44, sweep=False)
        self.add_line('sym-e7', (29, 10), (25, 5))
        self.add_arc('sym-e8', (25, 5), (24, 4), radius_x=77)
        self.add_arc('sym-e9', (24, 4), (23, 5), radius_x=77, sweep=False)
        self.add_line('sym-e10', (23, 5), (19, 10))
        self.add_arc('sym-e11', (19, 10), (8, 29), radius_x=43, sweep=False)
        self.add_line('sym-e12', (8, 29), (8, 30))
        self.add_arc('sym-e14', (8, 30), (23, 44), radius_x=16, sweep=False)
        self.add_line('sym-e15', (23, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
