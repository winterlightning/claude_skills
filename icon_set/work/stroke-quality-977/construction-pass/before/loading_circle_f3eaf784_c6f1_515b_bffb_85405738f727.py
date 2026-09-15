"""Loading circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3eaf784-c6f1-515b-bffb-85405738f727'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading circle_f3eaf784-c6f1-515b-bffb-85405738f727.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LoadingCircle(Solo48):
    icon_id = 'loading-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'circle', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (37, 24), (42, 24))
        self.add_line('sym-e1', (11, 24), (6, 24))
        self.add_line('sym-e2', (24, 42), (24, 37))
        self.add_line('sym-e3', (34, 34), (36, 36))
        self.add_line('sym-e4', (14, 34), (12, 36))
        self.add_line('sym-e5', (24, 6), (24, 11))
        self.add_line('sym-e6', (34, 14), (36, 12))
        self.add_line('sym-e7', (14, 14), (12, 12))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
        self.add_contour('sym-c6', 'sym-e6')
        self.add_contour('sym-c7', 'sym-e7')
