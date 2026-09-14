"""Arrow badge top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b87ef464-cfcd-5597-91f4-7870e5e7f05f'
SOURCE_PATH = 'icons-json/arrows/arrow badge top 2_b87ef464-cfcd-5597-91f4-7870e5e7f05f.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeTop2Arrows(Solo48):
    icon_id = 'arrow-badge-top-2-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (32, 24), (24, 17))
        self.add_line('sym-e1', (24, 17), (16, 24))
        self.add_bezier('sym-e2', (24, 4), ((23.99, 4), (24.01, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((22.25, 4), (21.16, 4.845), (20, 6)))
        self.add_line('sym-e4', (20, 6), (9, 17))
        self.add_bezier('sym-e5', (9, 17), ((8.53, 17.464), (8, 18.336), (8, 19)))
        self.add_line('sym-e6', (8, 19), (8, 42))
        self.add_bezier('sym-e7', (8, 42), ((8.3, 42.691), (8.23, 43.591), (9, 44)))
        self.add_bezier('sym-e8', (9, 44), ((9.22, 44), (9.77, 43.9), (10, 44)))
        self.add_line('sym-e9', (10, 44), (24, 44))
        self.add_line('sym-e10', (24, 44), (38, 44))
        self.add_bezier('sym-e11', (38, 44), ((38.23, 43.9), (38.78, 44), (39, 44)))
        self.add_bezier('sym-e12', (39, 44), ((39.77, 43.591), (39.7, 42.691), (40, 42)))
        self.add_line('sym-e13', (40, 42), (40, 19))
        self.add_bezier('sym-e14', (40, 19), ((40, 18.336), (39.47, 17.464), (39, 17)))
        self.add_line('sym-e15', (39, 17), (28, 6))
        self.add_bezier('sym-e16', (28, 6), ((26.84, 4.845), (25.75, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((23.99, 4), (24.01, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
