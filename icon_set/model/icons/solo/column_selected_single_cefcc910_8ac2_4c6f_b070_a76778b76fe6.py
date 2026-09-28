"""Column selected single (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefcc910-8ac2-4c6f-b070-a76778b76fe6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/column selected single_cefcc910-8ac2-4c6f-b070-a76778b76fe6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ColumnSelectedSingleInterfaceEssential(Solo48):
    icon_id = 'column-selected-single-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    aliases = ()
    keywords = ('column', 'selected', 'single', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 30), (40, 30))
        self.add_line('e1', (8, 30), (8, 44))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_line('e3', (40, 44), (40, 30))
        self.add_line('e4', (8, 30), (8, 18))
        self.add_line('e5', (40, 30), (40, 18))
        self.add_line('e6', (8, 18), (40, 18))
        self.add_line('e7', (8, 18), (8, 4))
        self.add_line('e8', (8, 4), (40, 4))
        self.add_line('e9', (40, 4), (40, 18))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7', 'e8', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
