"""Download arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58683514-619a-4591-ab3b-7d4cfa512a2d'
SOURCE_PATH = 'icons-json/arrows/download arrow_58683514-619a-4591-ab3b-7d4cfa512a2d.json'
AUTHOR = 'json_to_solo'

class DownloadArrow58683514(Solo48):
    icon_id = 'download-arrow-58683514'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (44, 40))
        self.add_line('e1', (10, 8), (38, 8))
        self.add_line('e2', (39, 10), (25, 29))
        self.add_line('e3', (23, 28), (9, 10))
        self.add_line('e4', (38, 8), (39, 10))
        self.add_line('e5', (25, 29), (23, 28))
        self.add_line('e6', (9, 10), (10, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2', 'e5', 'e3', 'e6', closed=True)
