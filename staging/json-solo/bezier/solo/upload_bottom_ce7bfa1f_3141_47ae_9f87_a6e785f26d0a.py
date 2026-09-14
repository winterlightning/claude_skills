"""Upload bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce7bfa1f-3141-47ae-9f87-a6e785f26d0a'
SOURCE_PATH = 'icons-json/arrows/upload bottom_ce7bfa1f-3141-47ae-9f87-a6e785f26d0a.json'
AUTHOR = 'json_to_solo'

class UploadBottomArrows(Solo48):
    icon_id = 'upload-bottom-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 34), (24, 8))
        self.add_line('sym-e1', (24, 8), (14, 17))
        self.add_bezier('sym-e2', (4, 32), ((4, 32.32), (4, 32.68), (4, 33)))
        self.add_bezier('sym-e3', (4, 33), ((4, 35.568), (4.309, 37.552), (7, 39)))
        self.add_bezier('sym-e4', (7, 39), ((7.527, 39.278), (8.382, 40), (9, 40)))
        self.add_line('sym-e5', (9, 40), (24, 40))
        self.add_line('sym-e6', (24, 40), (39, 40))
        self.add_bezier('sym-e7', (39, 40), ((39.618, 40), (40.473, 39.278), (41, 39)))
        self.add_bezier('sym-e8', (41, 39), ((43.691, 37.552), (44, 35.568), (44, 33)))
        self.add_bezier('sym-e9', (44, 33), ((44, 32.68), (44, 32.32), (44, 32)))
        self.add_line('sym-e10', (34, 17), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
