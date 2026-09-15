"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40e40a80-6888-5bfe-8fb4-b868fde81a0e'
SOURCE_PATH = 'pictographic-primitives/social/flag_40e40a80-6888-5bfe-8fb4-b868fde81a0e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FlagSocial(Solo48):
    icon_id = 'flag-social'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (8, 5), (40, 19))
        self.add_line('e1', (40, 19), (8, 31))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
