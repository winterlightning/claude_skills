"""Arrow right curved (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41da0587-488f-4ac3-b56e-fe0df61a4fa4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow right curved_41da0587-488f-4ac3-b56e-fe0df61a4fa4.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowRightCurved(Solo48):
    icon_id = 'arrow-right-curved'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'right', 'curved', 'symbol')

    def build(self):
        self.add_line('e0', (33, 8), (44, 18))
        self.add_line('e1', (27, 18), (44, 18))
        self.add_line('e2', (33, 27), (44, 18))
        self.add_bezier('e3', (4, 40), ((4, 39.427), (4, 38.863), (4, 38.291)), ((4, 30.703), (9.6, 22.914), (17.009, 19.781)), ((19.973, 18.535), (23.764, 18), (27, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
