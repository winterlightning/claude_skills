"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40e40a80-6888-5bfe-8fb4-b868fde81a0e'
SOURCE_PATH = 'icons-json/social/flag_40e40a80-6888-5bfe-8fb4-b868fde81a0e.json'
AUTHOR = 'json_to_solo'

class Flag40e40a80(Solo48):
    icon_id = 'flag-40e40a80'
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
