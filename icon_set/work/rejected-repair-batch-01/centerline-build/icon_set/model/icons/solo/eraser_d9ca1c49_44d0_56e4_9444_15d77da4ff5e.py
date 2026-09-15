"""Eraser (school-learning), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9ca1c49-44d0-56e4-9444-15d77da4ff5e'
SOURCE_PATH = 'pictographic-primitives/school-learning/eraser_d9ca1c49-44d0-56e4-9444-15d77da4ff5e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EraserSchoolLearning(Solo48):
    icon_id = 'eraser-school-learning'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'school-learning'
    aliases = ()
    keywords = ('eraser', 'school-learning')

    def build(self):
        self.add_line('e0', (30, 32), (16, 20))
        self.add_line('e1', (19, 40), (9, 32))
        self.add_line('e2', (9, 26), (28, 10))
        self.add_line('e3', (34, 9), (42, 16))
        self.add_line('e4', (43, 21), (22, 40))
        self.add_line('e5', (40, 40), (4, 40))
        self.add_arc('e6', (9, 32), (9, 26), radius_x=4)
        self.add_arc('e7-1', (28, 10), (31, 8), radius_x=5)
        self.add_line('e7-2', (31, 8), (34, 9))
        self.add_line('e8-1', (42, 16), (44, 19))
        self.add_arc('e8-2', (44, 19), (43, 21), radius_x=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6', 'e2', 'e7-1', 'e7-2', 'e3', 'e8-1', 'e8-2', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
