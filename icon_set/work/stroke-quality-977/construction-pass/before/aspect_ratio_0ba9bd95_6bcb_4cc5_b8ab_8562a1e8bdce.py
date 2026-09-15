"""Aspect ratio (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ba9bd95-6bcb-4cc5-b8ab-8562a1e8bdce'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/aspect ratio_0ba9bd95-6bcb-4cc5-b8ab-8562a1e8bdce.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AspectRatio(Solo48):
    icon_id = 'aspect-ratio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('aspect', 'ratio', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (6, 25), (22, 25))
        self.add_line('e1', (23, 26), (23, 42))
        self.add_line('e2', (6, 25), (6, 41))
        self.add_line('e3', (7, 42), (23, 42))
        self.add_line('e4', (6, 25), (6, 16))
        self.add_line('e5', (23, 42), (32, 42))
        self.add_line('e6', (6, 16), (31, 16))
        self.add_line('e7', (32, 17), (32, 42))
        self.add_line('e8', (6, 16), (6, 7))
        self.add_line('e9', (7, 6), (41, 6))
        self.add_line('e10', (42, 7), (42, 41))
        self.add_line('e11', (41, 42), (32, 42))
        self.add_line('e12', (22, 25), (23, 26))
        self.add_arc('e13', (6, 41), (7, 42), radius_x=1, sweep=False)
        self.add_line('e14', (31, 16), (32, 17))
        self.add_arc('e15', (6, 7), (7, 6), radius_x=1)
        self.add_arc('e16', (41, 6), (42, 7), radius_x=1)
        self.add_arc('e17', (42, 41), (41, 42), radius_x=1)
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e14', 'e7')
        self.add_contour('c5', 'e8', 'e15', 'e9', 'e16', 'e10', 'e17', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
