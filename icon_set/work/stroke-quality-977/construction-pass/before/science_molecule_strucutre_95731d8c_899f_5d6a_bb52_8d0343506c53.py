"""Science molecule strucutre (science), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95731d8c-899f-5d6a-bb52-8d0343506c53'
SOURCE_PATH = 'pictographic-primitives/science/science molecule strucutre_95731d8c-899f-5d6a-bb52-8d0343506c53.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ScienceMoleculeStrucutre(Solo48):
    icon_id = 'science-molecule-strucutre'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('science', 'molecule', 'strucutre')

    def build(self):
        self.add_line('e0', (24, 28), (24, 16))
        self.add_line('e1', (24, 28), (15, 34))
        self.add_line('e2', (24, 28), (31, 33))
        self.add_arc('e3-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e3-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e4-top', (30, 36), (42, 36), radius_x=6)
        self.add_arc('e4-bottom', (42, 36), (30, 36), radius_x=6)
        self.add_arc('e5-top', (19, 11), (29, 11), radius_x=5)
        self.add_arc('e5-bottom', (29, 11), (19, 11), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c2', 'e4')
