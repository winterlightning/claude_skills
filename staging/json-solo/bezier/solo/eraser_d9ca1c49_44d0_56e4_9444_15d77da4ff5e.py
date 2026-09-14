"""Eraser (school-learning), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9ca1c49-44d0-56e4-9444-15d77da4ff5e'
SOURCE_PATH = 'icons-json/school-learning/eraser_d9ca1c49-44d0-56e4-9444-15d77da4ff5e.json'
AUTHOR = 'json_to_solo'

class EraserD9ca1c49(Solo48):
    icon_id = 'eraser-d9ca1c49'
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
        self.add_bezier('e6', (9, 32), ((6.945, 30.265), (7.018, 27.743), (9, 26)))
        self.add_bezier('e7', (28, 10), ((28.955, 9.158), (29.691, 8), (31.1, 8)), ((31.104, 8), (31.107, 8), (31.111, 8)), ((31.335, 8), (31.567, 8.017), (31.8, 8.017)), ((32.564, 8.017), (33.455, 8.495), (34, 9)))
        self.add_bezier('e8', (42, 16), ((42.773, 16.716), (44, 18.198), (44, 19.276)), ((44, 19.277), (44, 19.278), (44, 19.279)), ((44, 19.345), (44, 19.411), (44, 19.469)), ((44, 19.537), (43.991, 19.604), (43.991, 19.663)), ((43.991, 20.278), (43.473, 20.579), (43, 21)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
