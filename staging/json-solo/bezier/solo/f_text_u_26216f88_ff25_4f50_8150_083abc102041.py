"""F (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26216f88-ff25-4f50-8150-083abc102041'
SOURCE_PATH = 'icons-json/symbol/f (text u)_26216f88-ff25-4f50-8150-083abc102041.json'
AUTHOR = 'json_to_solo'

class FTextUSymbol(Solo48):
    icon_id = 'f-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('f', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (34, 16))
        self.add_line('e1', (8, 33), (8, 5))
        self.add_line('e2', (10, 4), (40, 4))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (8, 5), ((8.44, 4.673), (8.12, 4.273), (9.12, 4.073)), ((9.42, 4.045), (9.7, 4.027), (10, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
