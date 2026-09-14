"""Number seven (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9989645-b0d3-5712-b978-9fe015d8d19b'
SOURCE_PATH = 'icons-json/interface-essential/number seven_d9989645-b0d3-5712-b978-9fe015d8d19b.json'
AUTHOR = 'json_to_solo'

class NumberSevenInterfaceEssential(Solo48):
    icon_id = 'number-seven-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'seven', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (40, 4), (18, 44))
        self.add_contour('c0', 'e0', 'e1')
