"""Vectors pen subtract (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76fe6a8d-bf50-4303-9115-ace751b1411d'
SOURCE_PATH = 'pictographic-primitives/design/vectors pen subtract_76fe6a8d-bf50-4303-9115-ace751b1411d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VectorsPenSubtract(Solo48):
    icon_id = 'vectors-pen-subtract'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vectors', 'pen', 'subtract', 'design')

    def build(self):
        self.add_line('e0', (25, 26), (9, 40))
        self.add_line('e1', (37, 21), (30, 15))
        self.add_line('e2', (30, 15), (16, 21))
        self.add_line('e3', (15, 21), (9, 40))
        self.add_line('e4', (37, 21), (31, 34))
        self.add_line('e5', (30, 35), (9, 40))
        self.add_line('e6', (39, 21), (44, 16))
        self.add_line('e7', (44, 15), (38, 8))
        self.add_line('e8', (36, 8), (29, 14))
        self.add_line('e9', (4, 10), (14, 10))
        self.add_line('e10', (16, 21), (15, 21))
        self.add_arc('e11', (31, 34), (30, 35), radius_x=20, sweep=False)
        self.add_line('e12', (37, 21), (39, 21))
        self.add_line('e13', (44, 16), (44, 15))
        self.add_line('e14', (38, 8), (36, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5')
        self.add_contour('c3', 'e12', 'e6', 'e13', 'e7', 'e14', 'e8')
        self.add_contour('c4', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
