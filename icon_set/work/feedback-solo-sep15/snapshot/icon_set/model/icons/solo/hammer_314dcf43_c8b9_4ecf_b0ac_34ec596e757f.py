"""Hammer (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '314dcf43-c8b9-4ecf-b0ac-34ec596e757f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hammer_314dcf43-c8b9-4ecf-b0ac-34ec596e757f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Hammer(Solo48):
    icon_id = 'hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('hammer', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (24, 25))
        self.add_line('e1', (32, 17), (18, 31))
        self.add_line('e2', (18, 31), (6, 19))
        self.add_line('e3', (6, 19), (19, 6))
        self.add_line('e4', (20, 6), (32, 17))
        self.add_arc('e5', (19, 6), (20, 6), radius_x=35, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e5', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
