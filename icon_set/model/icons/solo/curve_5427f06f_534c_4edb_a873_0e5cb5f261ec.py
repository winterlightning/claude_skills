"""Curve (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5427f06f-534c-4edb-a873-0e5cb5f261ec'
SOURCE_PATH = 'pictographic-primitives/diagrams/curve_5427f06f-534c-4edb-a873-0e5cb5f261ec.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Curve(Solo48):
    icon_id = 'curve'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('curve', 'diagrams')

    def build(self):
        self.add_line('sym-e0', (6, 42), (6, 41))
        self.add_arc('sym-e1', (6, 41), (17, 17), radius_x=33)
        self.add_arc('sym-e2', (17, 17), (41, 6), radius_x=33)
        self.add_line('sym-e3', (41, 6), (42, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
