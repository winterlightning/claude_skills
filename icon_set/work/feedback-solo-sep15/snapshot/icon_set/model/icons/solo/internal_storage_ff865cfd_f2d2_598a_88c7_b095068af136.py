"""Internal storage (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff865cfd-f2d2-598a-88c7-b095068af136'
SOURCE_PATH = 'pictographic-primitives/design/internal storage_ff865cfd-f2d2-598a-88c7-b095068af136.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class InternalStorage(Solo48):
    icon_id = 'internal-storage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('internal', 'storage', 'design')

    def build(self):
        self.add_line('e0', (42, 14), (6, 14))
        self.add_line('e1', (15, 6), (15, 42))
        self.add_line('e2', (42, 6), (42, 42))
        self.add_line('e3', (42, 42), (6, 42))
        self.add_line('e4', (6, 42), (6, 6))
        self.add_line('e5', (6, 6), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
