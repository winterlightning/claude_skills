"""Hardware nut round (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02b478af-5b99-47a4-ae75-a676ec999762'
SOURCE_PATH = 'pictographic-primitives/furnitures/hardware nut round_02b478af-5b99-47a4-ae75-a676ec999762.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HardwareNutRound(Solo48):
    icon_id = 'hardware-nut-round'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('hardware', 'nut', 'round', 'furnitures')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (14, 24), (34, 24), radius_x=10)
        self.add_arc('e1-bottom', (34, 24), (14, 24), radius_x=10)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
