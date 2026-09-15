"""Video (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86847067-8fdd-411e-9dcf-21637870d1dc'
SOURCE_PATH = 'pictographic-primitives/symbol/video_86847067-8fdd-411e-9dcf-21637870d1dc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Video86847067(Solo48):
    icon_id = 'video-86847067'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')

    def build(self):
        self.add_line('e0', (32, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (32, 40))
        self.add_line('e3', (32, 40), (32, 28))
        self.add_line('e4', (32, 28), (44, 36))
        self.add_line('e5', (44, 36), (44, 12))
        self.add_line('e6', (44, 12), (32, 20))
        self.add_line('e7', (32, 20), (32, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
