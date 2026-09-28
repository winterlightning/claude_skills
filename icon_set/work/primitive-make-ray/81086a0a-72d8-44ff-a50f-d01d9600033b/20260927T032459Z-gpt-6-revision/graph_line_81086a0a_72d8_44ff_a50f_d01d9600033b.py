"""Graph line (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '81086a0a-72d8-44ff-a50f-d01d9600033b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__graph-line/20260927T032104Z-thuan-mac-1/reference/graph line_81086a0a-72d8-44ff-a50f-d01d9600033b.svg'
AUTHOR = "gpt-6"
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GraphLine(Solo48):
    icon_id = 'graph-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('graph', 'line', 'business')

    def build(self):
        # One continuous trend with a broad, clearly open arrowhead.
        self.add_polyline('trend', (4, 40), (19, 20), (28, 29), (44, 8))
        self.add_line('arrow-top', (34, 8), (44, 8))
        self.add_line('arrow-right', (44, 8), (44, 22))
        self.relate('connect', 'trend', 'arrow-top')
        self.relate('connect', 'trend', 'arrow-right')
        self.relate('connect', 'arrow-top', 'arrow-right')
