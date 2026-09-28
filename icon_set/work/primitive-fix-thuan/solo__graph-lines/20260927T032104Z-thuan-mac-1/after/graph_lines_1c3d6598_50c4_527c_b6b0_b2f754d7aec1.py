"""Graph lines (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1c3d6598-50c4-527c-b6b0-b2f754d7aec1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__graph-lines/20260927T032104Z-thuan-mac-1/reference/graph lines_1c3d6598-50c4-527c-b6b0-b2f754d7aec1.svg'
AUTHOR = "gpt-6"
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GraphLines(Solo48):
    icon_id = 'graph-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('graph', 'lines', 'business')

    def build(self):
        # Two trends share axes while their bands remain separately readable.
        self.add_polyline('axes', (4, 8), (4, 40), (44, 40))
        self.add_polyline('upper-trend', (4, 18), (19, 10), (29, 20), (44, 8))
        self.add_polyline('lower-trend', (4, 32), (19, 24), (29, 32), (44, 22))
        self.relate('connect', 'axes', 'upper-trend')
        self.relate('connect', 'axes', 'lower-trend')
