"""Decision (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d2412b5-287b-4962-8979-8680db7f486f'
SOURCE_PATH = 'pictographic-primitives/design/decision_3d2412b5-287b-4962-8979-8680db7f486f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Decision(Solo48):
    icon_id = 'decision'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('decision', 'design')

    def build(self):
        self.add_line('sym-e0', (44, 24), (24, 40))
        self.add_arc('sym-e1', (24, 40), (23, 40), radius_x=26, sweep=False)
        self.add_line('sym-e2', (23, 40), (4, 24))
        self.add_line('sym-e3', (4, 24), (23, 8))
        self.add_arc('sym-e4', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_line('sym-e5', (24, 8), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
