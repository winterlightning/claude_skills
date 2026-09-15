"""Parallelogram shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea68f06b-a349-5aaf-8f07-33d82126dc42'
SOURCE_PATH = 'pictographic-primitives/design/parallelogram shape_ea68f06b-a349-5aaf-8f07-33d82126dc42.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ParallelogramShape(Solo48):
    icon_id = 'parallelogram-shape'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('parallelogram', 'shape', 'design')

    def build(self):
        self.add_line('e0', (13, 12), (4, 40))
        self.add_line('e1', (4, 40), (34, 40))
        self.add_line('e2', (34, 40), (44, 8))
        self.add_line('e3', (44, 8), (15, 8))
        self.add_arc('e4', (15, 8), (13, 12), radius_x=4, sweep=False)
        self.add_contour('c0', 'e4', 'e0', 'e1', 'e2', 'e3', closed=True)
