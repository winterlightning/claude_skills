"""Person (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'pictographic-primitives/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Person(Solo48):
    icon_id = 'person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('person', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 33))
        self.add_arc('sym-e2', (24, 33), (11, 28), radius_x=19)
        self.add_arc('sym-e3', (11, 28), (8, 25), radius_x=40, sweep=False)
        self.add_arc('sym-e5', (16, 12), (32, 12), radius_x=8)
        self.add_arc('sym-e6', (32, 12), (16, 12), radius_x=8)
        self.add_arc('sym-e8', (24, 33), (37, 28), radius_x=19, sweep=False)
        self.add_arc('sym-e9', (37, 28), (40, 25), radius_x=40, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
