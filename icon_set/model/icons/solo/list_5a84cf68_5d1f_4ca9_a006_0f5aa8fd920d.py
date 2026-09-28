"""List (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d'
SOURCE_PATH = 'pictographic-primitives/content/list_5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class List(Solo48):
    icon_id = 'list'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('list', 'content')

    def build(self):
        self.add_line('e0', (20, 8), (9, 20))
        self.add_line('e1', (9, 20), (4, 15))
        self.add_line('e2', (28, 17), (44, 17))
        self.add_line('e3', (20, 28), (9, 40))
        self.add_line('e4', (9, 40), (4, 35))
        self.add_line('e5', (28, 37), (44, 37))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
