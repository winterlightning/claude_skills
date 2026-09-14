"""Arrow badge top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b87ef464-cfcd-5597-91f4-7870e5e7f05f'
SOURCE_PATH = 'icons-json/arrows/arrow badge top 2_b87ef464-cfcd-5597-91f4-7870e5e7f05f.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeTop2(Solo48):
    icon_id = 'arrow-badge-top-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (32, 24), (24, 17))
        self.add_line('sym-e1', (24, 17), (16, 24))
        self.add_arc('sym-e3', (24, 4), (20, 6), radius_x=5, sweep=False)
        self.add_line('sym-e4', (20, 6), (9, 17))
        self.add_line('sym-e5', (9, 17), (8, 19))
        self.add_line('sym-e6', (8, 19), (8, 42))
        self.add_line('sym-e7', (8, 42), (9, 44))
        self.add_arc('sym-e8', (9, 44), (10, 44), radius_x=1)
        self.add_line('sym-e9', (10, 44), (24, 44))
        self.add_line('sym-e10', (24, 44), (38, 44))
        self.add_line('sym-e11', (38, 44), (39, 44))
        self.add_line('sym-e12', (39, 44), (40, 42))
        self.add_line('sym-e13', (40, 42), (40, 19))
        self.add_line('sym-e14', (40, 19), (39, 17))
        self.add_line('sym-e15', (39, 17), (28, 6))
        self.add_arc('sym-e16', (28, 6), (24, 4), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
