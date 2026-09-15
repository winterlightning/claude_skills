"""Navigation up 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39e474c5-3c80-4479-9890-eef2faf5d88e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation up 2_39e474c5-3c80-4479-9890-eef2faf5d88e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NavigationUp2(Solo48):
    icon_id = 'navigation-up-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'up', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 44))
        self.add_line('sym-e1', (24, 44), (8, 44))
        self.add_line('sym-e2', (9, 13), (24, 4))
        self.add_line('sym-e3', (24, 4), (39, 13))
        self.add_line('sym-e4', (40, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
