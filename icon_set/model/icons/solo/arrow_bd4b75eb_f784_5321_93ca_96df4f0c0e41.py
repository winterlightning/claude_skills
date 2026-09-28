"""Arrow (war), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd4b75eb-f784-5321-93ca-96df4f0c0e41'
SOURCE_PATH = 'pictographic-primitives/war/arrow_bd4b75eb-f784-5321-93ca-96df4f0c0e41.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Arrow(Solo48):
    icon_id = 'arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('arrow', 'war')

    def build(self):
        self.add_line('sym-e0', (8, 19), (24, 4))
        self.add_line('sym-e1', (24, 4), (40, 19))
        self.add_line('sym-e2', (24, 19), (24, 44))
        self.add_line('sym-e3', (24, 19), (40, 34))
        self.add_line('sym-e4', (24, 19), (8, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
