"""Search (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0eeffb06-d42b-5b45-8d51-5928144c3e27'
SOURCE_PATH = 'icons-json/interface-essential/search_0eeffb06-d42b-5b45-8d51-5928144c3e27.json'
AUTHOR = 'json_to_solo'

class SearchInterfaceEssential(Solo48):
    icon_id = 'search-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('search', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (29, 31))
        self.add_arc('e1-top', (6, 20), (34, 20), radius_x=14)
        self.add_arc('e1-bottom', (34, 20), (6, 20), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
