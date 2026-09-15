"""3 three squares (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9b057d5-e3a1-46b4-aa87-bcc44d4860f2'
SOURCE_PATH = 'pictographic-primitives/state/3 three squares_a9b057d5-e3a1-46b4-aa87-bcc44d4860f2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Icon3ThreeSquares(Solo48):
    icon_id = 'icon-3-three-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'squares', 'state')

    def build(self):
        self.add_line('e0', (31, 6), (31, 20))
        self.add_line('e1', (31, 20), (17, 20))
        self.add_line('e2', (17, 20), (17, 6))
        self.add_line('e3', (17, 6), (31, 6))
        self.add_line('e4', (20, 42), (6, 42))
        self.add_line('e5', (6, 42), (6, 28))
        self.add_line('e6', (6, 28), (20, 28))
        self.add_line('e7', (20, 28), (20, 42))
        self.add_line('e8', (42, 42), (28, 42))
        self.add_line('e9', (28, 42), (28, 28))
        self.add_line('e10', (28, 28), (42, 28))
        self.add_line('e11', (42, 28), (42, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.add_contour('c2', 'e8', 'e9', 'e10', 'e11', closed=True)
