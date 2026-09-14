"""Cross (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69e6b27c-e2b2-5fff-850b-0613057ead61'
SOURCE_PATH = 'icons-json/health/cross_69e6b27c-e2b2-5fff-850b-0613057ead61.json'
AUTHOR = 'json_to_solo'

class Cross(Solo48):
    icon_id = 'cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cross', 'health')

    def build(self):
        self.add_line('e0', (31, 6), (17, 6))
        self.add_line('e1', (17, 6), (17, 17))
        self.add_line('e2', (17, 17), (6, 17))
        self.add_line('e3', (6, 17), (6, 31))
        self.add_line('e4', (6, 31), (17, 31))
        self.add_line('e5', (17, 31), (17, 42))
        self.add_line('e6', (17, 42), (31, 42))
        self.add_line('e7', (31, 42), (31, 31))
        self.add_line('e8', (31, 31), (42, 31))
        self.add_line('e9', (42, 31), (42, 17))
        self.add_line('e10', (42, 17), (31, 17))
        self.add_line('e11', (31, 17), (31, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
