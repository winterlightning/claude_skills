"""Download (emails), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b452f6dc-091e-4314-a34a-bc3ee182e314'
SOURCE_PATH = 'pictographic-primitives/emails/download_b452f6dc-091e-4314-a34a-bc3ee182e314.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DownloadB452f6dc(Solo48):
    icon_id = 'download-b452f6dc'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('download', 'emails')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 31))
        self.add_line('sym-e1', (24, 31), (32, 22))
        self.add_line('sym-e2', (24, 44), (37, 44))
        self.add_line('sym-e4-1', (37, 44), (39, 43))
        self.add_arc('sym-e4-2', (39, 43), (40, 40), radius_x=5, sweep=False)
        self.add_line('sym-e6', (40, 40), (40, 39))
        self.add_line('sym-e7', (24, 31), (16, 22))
        self.add_line('sym-e8', (24, 44), (11, 44))
        self.add_line('sym-e10-1', (11, 44), (9, 43))
        self.add_arc('sym-e10-2', (9, 43), (8, 40), radius_x=5)
        self.add_line('sym-e12', (8, 40), (8, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e4-1', 'sym-e4-2', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e10-1', 'sym-e10-2', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
