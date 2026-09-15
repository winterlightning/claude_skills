"""Photo texture pattern (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eabbb109-e0f4-5fbb-8bfe-85169bc3b63b'
SOURCE_PATH = 'pictographic-primitives/design/photo texture pattern_eabbb109-e0f4-5fbb-8bfe-85169bc3b63b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PhotoTexturePattern(Solo48):
    icon_id = 'photo-texture-pattern'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('photo', 'texture', 'pattern', 'design')

    def build(self):
        self.add_line('e0', (6, 24), (42, 24))
        self.add_line('e1', (34, 42), (34, 6))
        self.add_line('e2', (42, 34), (6, 34))
        self.add_line('e3', (24, 42), (24, 6))
        self.add_line('e4', (14, 6), (14, 42))
        self.add_line('e5', (42, 14), (6, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
