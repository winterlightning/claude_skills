"""Circle pound (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd00222dd-fe8c-4806-ad6b-9c8ece57b642'
SOURCE_PATH = 'pictographic-primitives/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CirclePound(Solo48):
    icon_id = 'circle-pound'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'pound', 'state')

    def build(self):
        self.add_line('e0', (21, 18), (21, 24))
        self.add_line('e1', (21, 24), (18, 24))
        self.add_line('e2', (21, 24), (27, 24))
        self.add_line('e3', (30, 34), (18, 34))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-1', (30, 18), (24, 14), radius_x=4, sweep=False)
        self.add_arc('e5-2', (24, 14), (21, 18), radius_x=4, sweep=False)
        self.add_arc('e6', (18, 34), (21, 24), radius_x=9, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e1')
        self.add_contour('c1', 'e6', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
