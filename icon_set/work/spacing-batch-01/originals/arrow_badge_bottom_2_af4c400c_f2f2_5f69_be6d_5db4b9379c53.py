"""Arrow badge bottom 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af4c400c-f2f2-5f69-be6d-5db4b9379c53'
SOURCE_PATH = 'icons-json/arrows/arrow badge bottom 2_af4c400c-f2f2-5f69-be6d-5db4b9379c53.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeBottom2(Solo48):
    icon_id = 'arrow-badge-bottom-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (16, 24), (24, 31))
        self.add_line('sym-e1', (24, 31), (32, 24))
        self.add_arc('sym-e3', (24, 44), (28, 42), radius_x=5, sweep=False)
        self.add_line('sym-e4', (28, 42), (39, 31))
        self.add_line('sym-e5', (39, 31), (40, 29))
        self.add_line('sym-e6', (40, 29), (40, 6))
        self.add_line('sym-e7', (40, 6), (39, 4))
        self.add_line('sym-e8', (39, 4), (38, 4))
        self.add_line('sym-e9', (38, 4), (24, 4))
        self.add_line('sym-e10', (24, 4), (10, 4))
        self.add_line('sym-e11', (10, 4), (9, 4))
        self.add_arc('sym-e12', (9, 4), (8, 6), radius_x=3, sweep=False)
        self.add_line('sym-e13', (8, 6), (8, 29))
        self.add_line('sym-e14', (8, 29), (9, 31))
        self.add_line('sym-e15', (9, 31), (20, 42))
        self.add_arc('sym-e16', (20, 42), (24, 44), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
