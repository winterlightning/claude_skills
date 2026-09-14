"""Hash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95238ad5-8201-525e-995f-830ec837898f'
SOURCE_PATH = 'icons-json/interface-essential/hash_95238ad5-8201-525e-995f-830ec837898f.json'
AUTHOR = 'json_to_solo'

class Hash95238ad5(Solo48):
    icon_id = 'hash-95238ad5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('hash', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 18), (7, 18))
        self.add_line('e1', (35, 8), (29, 40))
        self.add_line('e2', (41, 30), (4, 30))
        self.add_line('e3', (19, 8), (12, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
