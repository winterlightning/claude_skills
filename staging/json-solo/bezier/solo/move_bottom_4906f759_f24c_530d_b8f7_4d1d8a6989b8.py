"""Move bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4906f759-f24c-530d-b8f7-4d1d8a6989b8'
SOURCE_PATH = 'icons-json/arrows/move bottom_4906f759-f24c-530d-b8f7-4d1d8a6989b8.json'
AUTHOR = 'json_to_solo'

class MoveBottomArrows(Solo48):
    icon_id = 'move-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('move', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 24))
        self.add_line('sym-e1', (32, 37), (24, 44))
        self.add_line('sym-e2', (24, 44), (16, 37))
        self.add_line('sym-e3', (40, 7), (40, 12))
        self.add_bezier('sym-e4', (40, 12), ((40, 12.136), (40, 12.864), (40, 13)))
        self.add_bezier('sym-e5', (40, 13), ((40, 14.445), (38.78, 16), (37, 16)))
        self.add_line('sym-e6', (37, 16), (24, 16))
        self.add_line('sym-e7', (24, 16), (11, 16))
        self.add_bezier('sym-e8', (11, 16), ((9.22, 16), (8, 14.445), (8, 13)))
        self.add_bezier('sym-e9', (8, 13), ((8, 12.864), (8, 12.136), (8, 12)))
        self.add_line('sym-e10', (8, 12), (8, 7))
        self.add_bezier('sym-e11', (8, 7), ((8, 5.7), (9.6, 4), (11, 4)))
        self.add_line('sym-e12', (11, 4), (24, 4))
        self.add_line('sym-e13', (24, 4), (37, 4))
        self.add_bezier('sym-e14', (37, 4), ((38.4, 4), (40, 5.7), (40, 7)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
