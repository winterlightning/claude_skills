"""Hospital 1 (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '660db5e2-989b-5f3b-8523-8fa0624ca343'
SOURCE_PATH = 'icons-json/health/hospital 1_660db5e2-989b-5f3b-8523-8fa0624ca343.json'
AUTHOR = 'json_to_solo'

class Hospital1Health(Solo48):
    icon_id = 'hospital-1-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('hospital', 'health')

    def build(self):
        self.add_line('e0', (28, 6), (20, 6))
        self.add_line('e1', (20, 6), (20, 17))
        self.add_line('e2', (20, 17), (10, 12))
        self.add_line('e3', (10, 12), (6, 19))
        self.add_line('e4', (6, 19), (15, 24))
        self.add_line('e5', (15, 24), (6, 30))
        self.add_line('e6', (6, 30), (10, 37))
        self.add_line('e7', (10, 37), (20, 31))
        self.add_line('e8', (20, 31), (20, 42))
        self.add_line('e9', (20, 42), (28, 42))
        self.add_line('e10', (28, 42), (28, 31))
        self.add_line('e11', (28, 31), (38, 37))
        self.add_line('e12', (38, 37), (42, 30))
        self.add_line('e13', (42, 30), (33, 24))
        self.add_line('e14', (33, 24), (42, 19))
        self.add_line('e15', (42, 19), (38, 12))
        self.add_line('e16', (38, 12), (28, 17))
        self.add_line('e17', (28, 17), (28, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', closed=True)
