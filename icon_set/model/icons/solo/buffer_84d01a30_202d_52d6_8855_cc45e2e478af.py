"""Buffer (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84d01a30-202d-52d6-8855-cc45e2e478af'
SOURCE_PATH = 'pictographic-primitives/diagrams/buffer_84d01a30-202d-52d6-8855-cc45e2e478af.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Buffer(Solo48):
    icon_id = 'buffer'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('buffer', 'diagrams')

    def build(self):
        self.add_line('e0', (35, 24), (15, 8))
        self.add_line('e1', (15, 8), (15, 40))
        self.add_line('e2', (15, 40), (35, 24))
        self.add_line('e3', (35, 24), (44, 24))
        self.add_line('e4', (4, 24), (15, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
