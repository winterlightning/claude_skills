"""Upload thick bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48397ea5-70c8-4ace-a246-7c4feefd4a32'
SOURCE_PATH = 'icons-json/arrows/upload thick bottom_48397ea5-70c8-4ace-a246-7c4feefd4a32.json'
AUTHOR = 'json_to_solo'

class UploadThickBottomArrows(Solo48):
    icon_id = 'upload-thick-bottom-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'thick', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 33), (4, 38))
        self.add_line('sym-e1', (4, 38), (4, 39))
        self.add_line('sym-e2', (4, 39), (6, 40))
        self.add_line('sym-e3', (6, 40), (24, 40))
        self.add_line('sym-e4', (24, 40), (42, 40))
        self.add_line('sym-e5', (42, 40), (44, 39))
        self.add_line('sym-e6', (44, 39), (44, 38))
        self.add_line('sym-e7', (44, 38), (44, 33))
        self.add_line('sym-e8', (12, 19), (24, 8))
        self.add_line('sym-e9', (24, 8), (36, 19))
        self.add_line('sym-e10', (36, 19), (30, 19))
        self.add_line('sym-e11', (30, 19), (30, 32))
        self.add_arc('sym-e12', (30, 32), (29, 33), radius_x=3, sweep=False)
        self.add_line('sym-e13', (29, 33), (24, 33))
        self.add_line('sym-e14', (24, 33), (19, 33))
        self.add_line('sym-e15', (19, 33), (18, 32))
        self.add_line('sym-e16', (18, 32), (18, 19))
        self.add_line('sym-e17', (18, 19), (12, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
