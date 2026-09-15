"""Star (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b255daf0-3adf-4238-9c62-9622160eca5c'
SOURCE_PATH = 'pictographic-primitives/holidays/star_b255daf0-3adf-4238-9c62-9622160eca5c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Star(Solo48):
    icon_id = 'star-b255daf0'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('star', 'holidays')

    def build(self):
        self.add_line('e0', (33, 33), (35, 42))
        self.add_line('e1', (35, 42), (24, 35))
        self.add_line('e2', (24, 35), (13, 42))
        self.add_line('e3', (13, 42), (16, 29))
        self.add_line('e4', (16, 29), (6, 19))
        self.add_line('e5', (6, 19), (19, 19))
        self.add_line('e6', (19, 19), (24, 6))
        self.add_line('e7', (24, 6), (29, 19))
        self.add_line('e8', (29, 19), (42, 19))
        self.add_line('e9', (42, 19), (33, 28))
        self.add_arc('e10', (33, 28), (33, 33), radius_x=7, sweep=False)
        self.add_contour('c0', 'e10', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', closed=True)
