"""Hill 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bbed91c-30b7-45ad-ae98-8eb34d66c53b'
SOURCE_PATH = 'icons-json/symbol/hill 1_6bbed91c-30b7-45ad-ae98-8eb34d66c53b.json'
AUTHOR = 'json_to_solo'

class Hill1Symbol(Solo48):
    icon_id = 'hill-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hill', 'symbol')

    def build(self):
        self.add_line('e0', (44, 39), (44, 9))
        self.add_line('e1', (42, 8), (5, 38))
        self.add_line('e2', (5, 40), (43, 40))
        self.add_line('e3', (44, 9), (42, 8))
        self.add_arc('e4-1', (5, 38), (4, 39), radius_x=2, sweep=False)
        self.add_arc('e4-2', (4, 39), (5, 40), radius_x=1, sweep=False)
        self.add_arc('e5', (43, 40), (44, 39), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4-1', 'e4-2', 'e2', 'e5', closed=True)
