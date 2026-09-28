"""End point triangle arrow 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c1f6ea2-97f0-41eb-96d5-43b4feacf58b'
SOURCE_PATH = 'pictographic-primitives/arrows/end point triangle arrow 1_9c1f6ea2-97f0-41eb-96d5-43b4feacf58b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EndPointTriangleArrow1(Solo48):
    icon_id = 'end-point-triangle-arrow-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('end', 'point', 'triangle', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (32, 40))
        self.add_line('e1', (44, 40), (32, 8))
        self.add_line('e2', (32, 8), (32, 40))
        self.add_line('e3', (32, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
