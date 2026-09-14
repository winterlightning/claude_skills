"""Election tall hat (school-learning), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3babae3c-79d9-4dd4-88a4-d7c89f6a58bf'
SOURCE_PATH = 'icons-json/school-learning/election tall hat_3babae3c-79d9-4dd4-88a4-d7c89f6a58bf.json'
AUTHOR = 'json_to_solo'

class ElectionTallHatSchoolLearning(Solo48):
    icon_id = 'election-tall-hat-school-learning'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'school-learning'
    aliases = ()
    keywords = ('election', 'tall', 'hat', 'school-learning')

    def build(self):
        self.add_line('e0', (38, 32), (29, 32))
        self.add_line('e1', (38, 32), (37, 40))
        self.add_line('e2', (38, 32), (39, 8))
        self.add_line('e3', (39, 8), (29, 8))
        self.add_line('e4', (37, 40), (11, 40))
        self.add_line('e5', (11, 40), (10, 32))
        self.add_line('e6', (10, 32), (19, 32))
        self.add_line('e7', (10, 32), (9, 8))
        self.add_line('e8', (9, 8), (19, 8))
        self.add_line('e9', (29, 32), (29, 8))
        self.add_line('e10', (29, 32), (19, 32))
        self.add_line('e11', (29, 8), (19, 8))
        self.add_line('e12', (19, 8), (19, 32))
        self.add_bezier('e13', (4, 37), ((5.564, 38.364), (7.573, 39.992), (9.809, 39.992)), ((10.164, 39.992), (10.518, 40), (10.873, 40)), ((11.009, 40), (10.864, 40), (11, 40)))
        self.add_bezier('e14', (44, 37), ((42.418, 38.305), (40.445, 39.983), (38.209, 39.983)), ((37.964, 39.983), (37.718, 40), (37.473, 40)), ((37.218, 40), (37.245, 40), (37, 40)))
        self.add_contour('c0', 'e13')
        self.add_contour('c1', 'e14')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e3')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e6')
        self.add_contour('c8', 'e7', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.add_contour('c11', 'e11')
        self.add_contour('c12', 'e12')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c11', 'c4')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c12')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c12', 'c7')
        self.relate('connect', 'c11', 'c12')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c12', 'c8')
