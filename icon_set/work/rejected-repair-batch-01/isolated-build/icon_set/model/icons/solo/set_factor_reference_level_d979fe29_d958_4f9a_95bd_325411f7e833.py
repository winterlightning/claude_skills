"""Set factor reference level (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd979fe29-d958-4f9a-95bd-325411f7e833'
SOURCE_PATH = 'pictographic-primitives/interface-essential/set factor reference level_d979fe29-d958-4f9a-95bd-325411f7e833.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SetFactorReferenceLevel(Solo48):
    icon_id = 'set-factor-reference-level'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('set', 'factor', 'reference', 'level', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 26), (16, 26))
        self.add_line('e2', (40, 39), (16, 39))
        self.add_line('e3', (28, 11), (16, 11))
        self.add_line('e4', (40, 11), (36, 11))
        self.add_arc('e5-top', (28, 11), (36, 11), radius_x=4)
        self.add_arc('e5-bottom', (36, 11), (28, 11), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c4', 'e5')
