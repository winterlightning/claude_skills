"""Angle 90 (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a225a826-480a-482a-a467-0ffbda56470c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle 90_a225a826-480a-482a-a467-0ffbda56470c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Angle90(Solo48):
    icon_id = 'angle-90'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (4, 8), (4, 31))
        self.add_line('e1', (44, 40), (15, 40))
        self.add_line('e2', (4, 31), (15, 31))
        self.add_line('e3', (15, 31), (15, 40))
        self.add_line('e4', (4, 31), (4, 40))
        self.add_line('e5', (4, 40), (15, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
