"""Flag plain (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ad95391-79e3-5fe0-a43b-37633f9875f9'
SOURCE_PATH = 'icons-json/social/flag plain_8ad95391-79e3-5fe0-a43b-37633f9875f9.json'
AUTHOR = 'json_to_solo'

class FlagPlain8ad95391(Solo48):
    icon_id = 'flag-plain-8ad95391'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'plain', 'social')

    def build(self):
        self.add_line('e0', (8, 7), (40, 7))
        self.add_line('e1', (40, 7), (40, 28))
        self.add_line('e2', (40, 28), (8, 28))
        self.add_line('e3', (8, 44), (8, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
