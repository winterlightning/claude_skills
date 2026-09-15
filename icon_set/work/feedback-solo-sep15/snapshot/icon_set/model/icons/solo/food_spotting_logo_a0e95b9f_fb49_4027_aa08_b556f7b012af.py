"""Food spotting logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e95b9f-fb49-4027-aa08-b556f7b012af'
SOURCE_PATH = 'pictographic-primitives/logos/food spotting logo_a0e95b9f-fb49-4027-aa08-b556f7b012af.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FoodSpottingLogo(Solo48):
    icon_id = 'food-spotting-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('food', 'spotting', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (22, 13), (13, 23), radius_x=11, sweep=False)
        self.add_arc('e1-2', (13, 23), (22, 35), radius_x=12, sweep=False)
        self.add_arc('e1-3', (22, 35), (35, 25), radius_x=11, sweep=False)
        self.add_arc('e1-4', (35, 25), (35, 24), radius_x=15, sweep=False)
        self.add_arc('e1-5', (35, 24), (27, 23), radius_x=10)
        self.add_arc('e1-6', (27, 23), (24, 13), radius_x=8)
        self.add_arc('e1-7', (24, 13), (22, 13), radius_x=3, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
