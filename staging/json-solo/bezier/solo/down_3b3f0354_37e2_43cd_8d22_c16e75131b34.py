"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (6, 6), ((6, 6.098), (6.008, 6.205), (6.008, 6.311)), ((6.008, 8.716), (6.54, 11.228), (7.145, 13.552)), ((10.795, 27.559), (24.526, 38), (39, 38)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
