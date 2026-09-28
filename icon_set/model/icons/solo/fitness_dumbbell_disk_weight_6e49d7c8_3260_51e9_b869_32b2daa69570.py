"""Fitness dumbbell disk weight (sports), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e49d7c8-3260-51e9-b869-32b2daa69570'
SOURCE_PATH = 'pictographic-primitives/sports/fitness dumbbell disk weight_6e49d7c8-3260-51e9-b869-32b2daa69570.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FitnessDumbbellDiskWeight(Solo48):
    icon_id = 'fitness-dumbbell-disk-weight'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('fitness', 'dumbbell', 'disk', 'weight', 'sports')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e1-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
