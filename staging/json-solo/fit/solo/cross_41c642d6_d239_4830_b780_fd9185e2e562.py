"""Cross (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41c642d6-d239-4830-b780-fd9185e2e562'
SOURCE_PATH = 'icons-json/health/cross_41c642d6-d239-4830-b780-fd9185e2e562.json'
AUTHOR = 'json_to_solo'

class Cross41c642d6(Solo48):
    icon_id = 'cross-41c642d6'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cross', 'health')

    def build(self):
        self.add_line('e0', (30, 6), (18, 6))
        self.add_line('e1', (18, 6), (18, 18))
        self.add_line('e2', (18, 18), (6, 18))
        self.add_line('e3', (6, 18), (6, 30))
        self.add_line('e4', (6, 30), (18, 30))
        self.add_line('e5', (18, 30), (18, 42))
        self.add_line('e6', (18, 42), (30, 42))
        self.add_line('e7', (30, 42), (30, 30))
        self.add_line('e8', (30, 30), (42, 30))
        self.add_line('e9', (42, 30), (42, 18))
        self.add_line('e10', (42, 18), (30, 18))
        self.add_line('e11', (30, 18), (30, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
