"""Arrow thin double left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb6bfc29-bfb0-54e0-aa76-b62efe9d2197'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thin double left_eb6bfc29-bfb0-54e0-aa76-b62efe9d2197.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThinDoubleLeft(Solo48):
    icon_id = 'arrow-thin-double-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'double', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (19, 40), (4, 24))
        self.add_line('sym-e1', (4, 24), (19, 8))
        self.add_line('sym-e2', (19, 24), (44, 24))
        self.add_line('sym-e3', (19, 24), (34, 8))
        self.add_line('sym-e4', (19, 24), (34, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
