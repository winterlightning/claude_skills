"""Download (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fe422c3-4803-4575-8eb7-78ff267e78a3'
SOURCE_PATH = 'pictographic-primitives/emails/download_5fe422c3-4803-4575-8eb7-78ff267e78a3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DownloadEmails(Solo48):
    icon_id = 'download-emails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('download', 'emails')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 31))
        self.add_line('sym-e1', (24, 31), (34, 23))
        self.add_line('sym-e2', (24, 40), (40, 40))
        self.add_arc('sym-e3', (40, 40), (44, 37), radius_x=5, sweep=False)
        self.add_line('sym-e4', (44, 37), (44, 32))
        self.add_line('sym-e5', (14, 23), (24, 31))
        self.add_line('sym-e6', (24, 40), (8, 40))
        self.add_arc('sym-e7', (8, 40), (4, 37), radius_x=5)
        self.add_line('sym-e8', (4, 37), (4, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
