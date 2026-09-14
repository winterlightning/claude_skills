"""Flags (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f3d01e4-e77c-50b4-8411-71fbfa4ca92d'
SOURCE_PATH = 'icons-json/social/flags_9f3d01e4-e77c-50b4-8411-71fbfa4ca92d.json'
AUTHOR = 'json_to_solo'

class Flags(Solo48):
    icon_id = 'flags'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flags', 'social')

    def build(self):
        self.add_line('e0', (29, 13), (40, 13))
        self.add_line('e1', (40, 13), (36, 22))
        self.add_line('e2', (36, 22), (40, 31))
        self.add_line('e3', (40, 31), (21, 31))
        self.add_line('e4', (21, 31), (21, 25))
        self.add_line('e5', (8, 25), (29, 25))
        self.add_line('e6', (29, 25), (29, 8))
        self.add_line('e7', (29, 8), (8, 8))
        self.add_line('e8', (8, 44), (8, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
