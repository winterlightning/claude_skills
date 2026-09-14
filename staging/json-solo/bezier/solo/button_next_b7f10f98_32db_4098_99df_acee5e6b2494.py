"""Button next (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7f10f98-32db-4098-99df-acee5e6b2494'
SOURCE_PATH = 'icons-json/interface-essential/button next_b7f10f98-32db-4098-99df-acee5e6b2494.json'
AUTHOR = 'json_to_solo'

class ButtonNextInterfaceEssential(Solo48):
    icon_id = 'button-next-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'next', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 41), (42, 6))
        self.add_line('e1', (31, 24), (6, 6))
        self.add_line('e2', (6, 6), (6, 42))
        self.add_line('e3', (6, 42), (31, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
