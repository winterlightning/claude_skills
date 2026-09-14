"""Upload bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e2', (4, 32), (4, 33))
        self.add_line('sym-e3-1', (4, 33), (5, 38))
        self.add_line('sym-e3-2', (5, 38), (7, 39))
        self.add_arc('sym-e4', (7, 39), (9, 40), radius_x=4, sweep=False)
        self.add_line('sym-e5', (9, 40), (24, 40))
        self.add_line('sym-e6', (24, 40), (39, 40))
        self.add_arc('sym-e7', (39, 40), (41, 39), radius_x=4, sweep=False)
        self.add_line('sym-e8-1', (41, 39), (43, 38))
        self.add_line('sym-e8-2', (43, 38), (44, 33))
        self.add_line('sym-e9', (44, 33), (44, 32))
        self.add_line('sym-e10', (34, 17), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
