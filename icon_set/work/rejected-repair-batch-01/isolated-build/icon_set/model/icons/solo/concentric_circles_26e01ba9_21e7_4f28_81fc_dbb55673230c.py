"""Concentric circles (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26e01ba9-21e7-4f28-81fc-dbb55673230c'
SOURCE_PATH = 'pictographic-primitives/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ConcentricCircles(Solo48):
    icon_id = 'concentric-circles'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('concentric', 'circles', 'symbol')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (13, 24), (35, 24), radius_x=11)
        self.add_arc('e1-bottom', (35, 24), (13, 24), radius_x=11)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
