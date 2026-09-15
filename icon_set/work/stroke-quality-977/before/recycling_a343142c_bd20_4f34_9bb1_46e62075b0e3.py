"""recycling-symbol: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a343142c-bd20-4f34-9bb1-46e62075b0e3'
SOURCE_PATH = 'pictographic-primitives/symbol/recycling_a343142c-bd20-4f34-9bb1-46e62075b0e3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class RecyclingSymbol(Solo48):
    icon_id = 'recycling-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('recycling', 'symbol')

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
