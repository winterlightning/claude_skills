"""Column selected single (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9e567b-f670-5e72-810e-80ed576fefb7'
SOURCE_PATH = 'icons-json/interface-essential/column selected single_cd9e567b-f670-5e72-810e-80ed576fefb7.json'
AUTHOR = 'json_to_solo'

class ColumnSelectedSingleCd9e567b(Solo48):
    icon_id = 'column-selected-single-cd9e567b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('column', 'selected', 'single', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 30), (8, 30))
        self.add_line('e1', (40, 18), (8, 18))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (8, 44), (8, 4))
        self.add_line('e4', (8, 4), (40, 4))
        self.add_line('e5', (40, 4), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
