"""Image (images), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e83bac9c-f640-4df4-9864-e5c93655f156'
SOURCE_PATH = 'pictographic-primitives/images/image_e83bac9c-f640-4df4-9864-e5c93655f156.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Image(Solo48):
    icon_id = 'image'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'images'
    aliases = ()
    keywords = ('image', 'images')

    def build(self):
        self.add_line('e0', (29, 32), (19, 21))
        self.add_line('e1', (19, 21), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_line('e3', (44, 40), (33, 28))
        self.add_line('e4', (33, 28), (29, 32))
        self.add_arc('e5-top', (32, 14), (44, 14), radius_x=6)
        self.add_arc('e5-bottom', (44, 14), (32, 14), radius_x=6)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
