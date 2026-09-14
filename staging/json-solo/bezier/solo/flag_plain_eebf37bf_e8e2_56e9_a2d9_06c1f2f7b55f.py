"""Flag plain (social), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eebf37bf-e8e2-56e9-a2d9-06c1f2f7b55f'
SOURCE_PATH = 'icons-json/social/flag plain_eebf37bf-e8e2-56e9-a2d9-06c1f2f7b55f.json'
AUTHOR = 'json_to_solo'

class FlagPlain(Solo48):
    icon_id = 'flag-plain'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'plain', 'social')

    def build(self):
        self.add_line('e0', (8, 9), (40, 9))
        self.add_line('e1', (40, 9), (40, 29))
        self.add_line('e2', (40, 29), (8, 29))
        self.add_line('e3', (8, 44), (8, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
