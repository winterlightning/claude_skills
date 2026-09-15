"""Phone merge (phones), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1171bcf4-d88f-401f-86a0-fd93af09bc27'
SOURCE_PATH = 'pictographic-primitives/phones/phone merge_1171bcf4-d88f-401f-86a0-fd93af09bc27.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PhoneMerge(Solo48):
    icon_id = 'phone-merge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('phone', 'merge', 'phones')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 29))
        self.add_arc('sym-e1', (24, 29), (26, 35), radius_x=27, sweep=False)
        self.add_arc('sym-e2', (26, 35), (37, 43), radius_x=18, sweep=False)
        self.add_line('sym-e3', (37, 43), (40, 44))
        self.add_line('sym-e5', (33, 14), (24, 4))
        self.add_line('sym-e6', (24, 4), (15, 14))
        self.add_arc('sym-e8', (8, 44), (11, 43), radius_x=11, sweep=False)
        self.add_arc('sym-e9', (11, 43), (22, 35), radius_x=18, sweep=False)
        self.add_arc('sym-e10', (22, 35), (24, 29), radius_x=28)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
