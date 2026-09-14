"""Cross over (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be548f8b-b02f-5ec6-8878-dd9506f0fb2e'
SOURCE_PATH = 'icons-json/interface-essential/cross over_be548f8b-b02f-5ec6-8878-dd9506f0fb2e.json'
AUTHOR = 'json_to_solo'

class CrossOver(Solo48):
    icon_id = 'cross-over'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cross', 'over', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 6), (42, 6))
        self.add_line('e1', (42, 6), (24, 24))
        self.add_line('e2', (24, 24), (6, 6))
        self.add_line('e3', (6, 42), (24, 24))
        self.add_line('e4', (24, 24), (42, 42))
        self.add_line('e5', (42, 42), (32, 42))
        self.add_line('e6', (42, 42), (42, 32))
        self.add_line('e7', (42, 6), (42, 16))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
