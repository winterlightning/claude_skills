"""Cross (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba33e583-6275-4725-8f1d-e81b2325332c'
SOURCE_PATH = 'icons-json/health/cross_ba33e583-6275-4725-8f1d-e81b2325332c.json'
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
        self.add_line('e0', (18, 6), (30, 6))
        self.add_line('e1', (30, 6), (30, 18))
        self.add_line('e2', (30, 18), (42, 18))
        self.add_line('e3', (42, 18), (42, 30))
        self.add_line('e4', (42, 30), (30, 30))
        self.add_line('e5', (30, 30), (30, 42))
        self.add_line('e6', (30, 42), (18, 42))
        self.add_line('e7', (18, 42), (18, 30))
        self.add_line('e8', (18, 30), (6, 30))
        self.add_line('e9', (6, 30), (6, 18))
        self.add_line('e10', (6, 18), (18, 18))
        self.add_line('e11', (18, 18), (18, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
