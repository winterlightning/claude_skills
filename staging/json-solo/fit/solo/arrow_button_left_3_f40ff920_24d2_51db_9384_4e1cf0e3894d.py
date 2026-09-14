"""Arrow button left 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f40ff920-24d2-51db-9384-4e1cf0e3894d'
SOURCE_PATH = 'icons-json/arrows/arrow button left 3_f40ff920-24d2-51db-9384-4e1cf0e3894d.json'
AUTHOR = 'json_to_solo'

class ArrowButtonLeft3Arrows(Solo48):
    icon_id = 'arrow-button-left-3-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 24))
        self.add_arc('sym-e1', (8, 24), (10, 27), radius_x=4, sweep=False)
        self.add_line('sym-e2', (10, 27), (26, 43))
        self.add_line('sym-e3', (26, 43), (27, 44))
        self.add_line('sym-e4', (27, 44), (28, 44))
        self.add_line('sym-e5', (28, 44), (29, 44))
        self.add_line('sym-e6', (29, 44), (40, 44))
        self.add_line('sym-e7', (40, 44), (21, 25))
        self.add_arc('sym-e8', (21, 25), (21, 24), radius_x=1, sweep=False)
        self.add_arc('sym-e9', (21, 24), (21, 23), radius_x=1, sweep=False)
        self.add_line('sym-e10', (21, 23), (40, 4))
        self.add_line('sym-e11', (40, 4), (29, 4))
        self.add_line('sym-e12', (29, 4), (28, 4))
        self.add_line('sym-e13', (28, 4), (27, 4))
        self.add_line('sym-e14', (27, 4), (26, 5))
        self.add_line('sym-e15', (26, 5), (10, 21))
        self.add_arc('sym-e16', (10, 21), (8, 24), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
