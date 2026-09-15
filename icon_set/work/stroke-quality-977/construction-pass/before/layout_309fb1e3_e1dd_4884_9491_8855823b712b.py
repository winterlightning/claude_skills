"""Layout (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '309fb1e3-e1dd-4884-9491-8855823b712b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout_309fb1e3-e1dd-4884-9491-8855823b712b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Layout(Solo48):
    icon_id = 'layout'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 25), (42, 25))
        self.add_line('e1', (24, 25), (24, 42))
        self.add_line('e2', (24, 25), (24, 6))
        self.add_line('e3', (42, 25), (42, 40))
        self.add_line('e4', (40, 42), (24, 42))
        self.add_line('e5', (42, 25), (42, 8))
        self.add_line('e6', (40, 6), (24, 6))
        self.add_line('e7', (24, 42), (8, 42))
        self.add_line('e8', (6, 40), (6, 9))
        self.add_line('e9', (8, 6), (24, 6))
        self.add_line('e10', (42, 40), (40, 42))
        self.add_line('e11', (42, 8), (40, 6))
        self.add_arc('e12', (8, 42), (6, 40), radius_x=4)
        self.add_line('e13', (6, 9), (8, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e10', 'e4')
        self.add_contour('c4', 'e5', 'e11', 'e6')
        self.add_contour('c5', 'e7', 'e12', 'e8', 'e13', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
