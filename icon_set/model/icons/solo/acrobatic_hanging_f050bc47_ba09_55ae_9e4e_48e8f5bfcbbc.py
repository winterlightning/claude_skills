"""Acrobatic hanging (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f050bc47-ba09-55ae-9e4e-48e8f5bfcbbc'
SOURCE_PATH = 'pictographic-primitives/sports/acrobatic hanging_f050bc47-ba09-55ae-9e4e-48e8f5bfcbbc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AcrobaticHangingSports(Solo48):
    icon_id = 'acrobatic-hanging-sports'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('acrobatic', 'hanging', 'sports')

    def build(self):
        self.add_line('e0', (13, 28), (13, 8))
        self.add_line('e1', (4, 8), (44, 8))
        self.add_line('e2', (35, 28), (35, 8))
        self.add_arc('e3-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e3-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e4-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e4-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'c1')
