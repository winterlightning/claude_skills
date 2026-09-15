"""Glass (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204d4784-13d7-4489-a1d4-d6364d2329c7'
SOURCE_PATH = 'pictographic-primitives/drinks/glass_204d4784-13d7-4489-a1d4-d6364d2329c7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Glass(Solo48):
    icon_id = 'glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('glass', 'drinks')

    def build(self):
        self.add_line('e0', (24, 44), (24, 29))
        self.add_line('e1', (14, 44), (34, 44))
        self.add_line('e2', (8, 14), (8, 4))
        self.add_line('e3', (8, 4), (40, 4))
        self.add_line('e4', (40, 4), (40, 16))
        self.add_arc('e5-1', (40, 16), (20, 28), radius_x=16)
        self.add_arc('e5-2', (20, 28), (8, 14), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5-1', 'e5-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
