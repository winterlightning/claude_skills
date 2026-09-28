"""Process (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0731e33b-404d-4405-92c6-fb790f898a3a'
SOURCE_PATH = 'pictographic-primitives/diagrams/process_0731e33b-404d-4405-92c6-fb790f898a3a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Process(Solo48):
    icon_id = 'process'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('process', 'diagrams')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_line('e1', (44, 40), (4, 40))
        self.add_line('e2', (4, 40), (4, 8))
        self.add_line('e3', (4, 8), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
