"""Download arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dccb50e-2f6e-4a5e-807f-29ce484bf7e1'
SOURCE_PATH = 'pictographic-primitives/arrows/download arrow_6dccb50e-2f6e-4a5e-807f-29ce484bf7e1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DownloadArrow6dccb50e(Solo48):
    icon_id = 'download-arrow-6dccb50e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('download', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (9, 8), (24, 32))
        self.add_line('e1', (24, 32), (39, 8))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
