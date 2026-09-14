"""Lines (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70edbe92-e5a7-4163-82c3-c5891c1950fd'
SOURCE_PATH = 'icons-json/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.json'
AUTHOR = 'json_to_solo'

class LinesSymbol(Solo48):
    icon_id = 'lines-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lines', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (16, 8))
        self.add_line('e1', (19, 13), (33, 38))
        self.add_line('e2', (36, 40), (44, 40))
        self.add_bezier('e3', (16, 8), ((16.182, 8.096), (16.2, 8.064), (16.391, 8.176)), ((17.518, 8.88), (18.218, 11.624), (19, 13)))
        self.add_bezier('e4', (33, 38), ((33.827, 38.896), (34.973, 40), (36, 40)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
