"""Lines (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70edbe92-e5a7-4163-82c3-c5891c1950fd'
SOURCE_PATH = 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Lines(Solo48):
    icon_id = 'lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lines', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (16, 8))
        self.add_line('e1', (19, 13), (33, 38))
        self.add_line('e2', (36, 40), (44, 40))
        self.add_line('e3', (16, 8), (19, 13))
        self.add_arc('e4', (33, 38), (36, 40), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
