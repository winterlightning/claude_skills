"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b3f0354-37e2-43cd-8d22-c16e75131b34'
SOURCE_PATH = 'icons-json/arrows/down_3b3f0354-37e2-43cd-8d22-c16e75131b34.json'
AUTHOR = 'json_to_solo'

class Down3b3f0354(Solo48):
    icon_id = 'down-3b3f0354'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (39, 38), (42, 38))
        self.add_line('e1', (39, 42), (42, 38))
        self.add_line('e2', (39, 34), (42, 38))
        self.add_arc('e3', (6, 6), (39, 38), radius_x=33, sweep=False)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
