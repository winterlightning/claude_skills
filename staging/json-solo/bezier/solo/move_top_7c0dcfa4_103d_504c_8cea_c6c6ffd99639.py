"""Move top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c0dcfa4-103d-504c-8cea-c6c6ffd99639'
SOURCE_PATH = 'icons-json/arrows/move top_7c0dcfa4-103d-504c-8cea-c6c6ffd99639.json'
AUTHOR = 'json_to_solo'

class MoveTopArrows(Solo48):
    icon_id = 'move-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('move', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 24))
        self.add_line('sym-e1', (16, 11), (24, 4))
        self.add_line('sym-e2', (24, 4), (32, 11))
        self.add_line('sym-e3', (8, 41), (8, 36))
        self.add_bezier('sym-e4', (8, 36), ((8, 35.864), (8, 35.136), (8, 35)))
        self.add_bezier('sym-e5', (8, 35), ((8, 33.555), (9.22, 32), (11, 32)))
        self.add_line('sym-e6', (11, 32), (24, 32))
        self.add_line('sym-e7', (24, 32), (37, 32))
        self.add_bezier('sym-e8', (37, 32), ((38.78, 32), (40, 33.555), (40, 35)))
        self.add_bezier('sym-e9', (40, 35), ((40, 35.136), (40, 35.864), (40, 36)))
        self.add_line('sym-e10', (40, 36), (40, 41))
        self.add_bezier('sym-e11', (40, 41), ((40, 42.3), (38.4, 44), (37, 44)))
        self.add_line('sym-e12', (37, 44), (24, 44))
        self.add_line('sym-e13', (24, 44), (11, 44))
        self.add_bezier('sym-e14', (11, 44), ((9.6, 44), (8, 42.3), (8, 41)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
