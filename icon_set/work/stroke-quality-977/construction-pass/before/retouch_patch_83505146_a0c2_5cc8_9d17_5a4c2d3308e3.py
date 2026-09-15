"""Retouch patch (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83505146-a0c2-5cc8-9d17-5a4c2d3308e3'
SOURCE_PATH = 'pictographic-primitives/photography/retouch patch_83505146-a0c2-5cc8-9d17-5a4c2d3308e3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RetouchPatch(Solo48):
    icon_id = 'retouch-patch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('retouch', 'patch', 'photography')

    def build(self):
        self.add_line('e0', (29, 14), (29, 6))
        self.add_line('e1', (35, 19), (42, 19))
        self.add_line('e2', (35, 28), (42, 28))
        self.add_line('e3', (29, 34), (29, 42))
        self.add_line('e4', (19, 34), (19, 42))
        self.add_line('e5', (14, 28), (10, 28))
        self.add_line('e6', (10, 28), (10, 34))
        self.add_line('e7', (13, 38), (34, 38))
        self.add_line('e8', (38, 32), (38, 13))
        self.add_line('e9', (34, 10), (14, 10))
        self.add_line('e10', (10, 13), (10, 28))
        self.add_line('e11', (10, 28), (6, 28))
        self.add_line('e12', (13, 19), (6, 19))
        self.add_line('e13', (19, 14), (19, 6))
        self.add_arc('e14', (10, 34), (13, 38), radius_x=4, sweep=False)
        self.add_arc('e15', (34, 38), (38, 32), radius_x=5, sweep=False)
        self.add_arc('e16', (38, 13), (34, 10), radius_x=3, sweep=False)
        self.add_arc('e17', (14, 10), (10, 13), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9', 'e17', 'e10', 'e11')
        self.add_contour('c6', 'e12')
        self.add_contour('c7', 'e13')
