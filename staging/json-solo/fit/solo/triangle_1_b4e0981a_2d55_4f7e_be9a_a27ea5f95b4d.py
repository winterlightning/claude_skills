"""Triangle 1 (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4e0981a-2d55-4f7e-be9a-a27ea5f95b4d'
SOURCE_PATH = 'icons-json/other/triangle 1_b4e0981a-2d55-4f7e-be9a-a27ea5f95b4d.json'
AUTHOR = 'json_to_solo'

class Triangle1B4e0981a(Solo48):
    icon_id = 'triangle-1-b4e0981a'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('triangle', 'other')

    def build(self):
        self.add_line('e0', (24, 6), (6, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_line('e2', (42, 42), (24, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
