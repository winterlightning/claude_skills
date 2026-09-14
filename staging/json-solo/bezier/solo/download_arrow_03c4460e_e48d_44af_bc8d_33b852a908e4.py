"""Download arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03c4460e-e48d-44af-bc8d-33b852a908e4'
SOURCE_PATH = 'icons-json/arrows/download arrow_03c4460e-e48d-44af-bc8d-33b852a908e4.json'
AUTHOR = 'json_to_solo'

class DownloadArrow03c4460e(Solo48):
    icon_id = 'download-arrow-03c4460e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (9, 8), (24, 29))
        self.add_line('e1', (24, 29), (39, 8))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
