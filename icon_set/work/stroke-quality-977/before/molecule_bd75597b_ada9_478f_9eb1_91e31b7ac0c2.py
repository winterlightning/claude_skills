"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd75597b-ada9-478f-9eb1-91e31b7ac0c2'
SOURCE_PATH = 'pictographic-primitives/science/molecule_bd75597b-ada9-478f-9eb1-91e31b7ac0c2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoleculeBd75597b(Solo48):
    icon_id = 'molecule-bd75597b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        self.add_line('e0', (35, 29), (29, 21))
        self.add_line('e1', (19, 21), (14, 29))
        self.add_arc('e2-top', (16, 16), (32, 16), radius_x=8)
        self.add_arc('e2-bottom', (32, 16), (16, 16), radius_x=8)
        self.add_arc('e3-top', (4, 34), (16, 34), radius_x=6)
        self.add_arc('e3-bottom', (16, 34), (4, 34), radius_x=6)
        self.add_arc('e4-1', (35, 29), (44, 34), radius_x=6)
        self.add_arc('e4-2', (44, 34), (38, 40), radius_x=6)
        self.add_arc('e4-3', (38, 40), (35, 29), radius_x=6)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', closed=True)
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e2')
        self.relate('connect', 'c2', 'e3')
