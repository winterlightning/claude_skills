"""Focus circle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '194127a0-095c-4aa9-bd19-038532bd3355'
SOURCE_PATH = 'pictographic-primitives/symbol/focus circle_194127a0-095c-4aa9-bd19-038532bd3355.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FocusCircle(Solo48):
    icon_id = 'focus-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('focus', 'circle', 'symbol')

    def build(self):
        self.add_line('e0', (15, 6), (6, 6))
        self.add_line('e1', (6, 6), (6, 15))
        self.add_line('e2', (33, 6), (42, 6))
        self.add_line('e3', (42, 6), (42, 15))
        self.add_line('e4', (6, 33), (6, 42))
        self.add_line('e5', (6, 42), (15, 42))
        self.add_line('e6', (42, 33), (42, 42))
        self.add_line('e7', (42, 42), (33, 42))
        self.add_arc('e8-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e8-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e5')
        self.add_contour('c3', 'e6', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
