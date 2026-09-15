"""recycling: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb'
SOURCE_PATH = 'pictographic-primitives/state/recycling_04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Recycling(Solo48):
    icon_id = 'recycling'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('recycling', 'state')

    def build(self):
        # SQUARE (6,6)-(42,42); opposite turns with ten-unit end separation.
        # Construction reference: Lucide refresh-cw: smooth circular turns and coherent arrowheads
        # Equal elliptical half-turns; arrowheads point along each local tangent.
        self.add_arc('upper',(6,19),(42,19),radius_x=18,radius_y=13)
        self.add_polyline('upper-head',(36,13),(42,19),(42,11))
        self.add_arc('lower',(42,29),(6,29),radius_x=18,radius_y=13)
        self.add_polyline('lower-head',(12,35),(6,29),(6,37))
        self.relate('connect','upper','upper-head')
        self.relate('connect','lower','lower-head')
