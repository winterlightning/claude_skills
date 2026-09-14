"""Download arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dccb50e-2f6e-4a5e-807f-29ce484bf7e1'
SOURCE_PATH = 'icons-json/arrows/download arrow_6dccb50e-2f6e-4a5e-807f-29ce484bf7e1.json'
AUTHOR = 'json_to_solo'

class DownloadArrow6dccb50e(Solo48):
    icon_id = 'download-arrow-6dccb50e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (9, 8), (24, 32))
        self.add_line('e1', (24, 32), (39, 8))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
