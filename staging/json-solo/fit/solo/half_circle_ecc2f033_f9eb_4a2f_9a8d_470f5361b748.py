"""Half circle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecc2f033-f9eb-4a2f-9a8d-470f5361b748'
SOURCE_PATH = 'icons-json/symbol/half circle_ecc2f033-f9eb-4a2f-9a8d-470f5361b748.json'
AUTHOR = 'json_to_solo'

class HalfCircleSymbol(Solo48):
    icon_id = 'half-circle-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('half', 'circle', 'symbol')

    def build(self):
        self.add_line('e0', (14, 36), (14, 40))
        self.add_line('e1', (14, 40), (4, 40))
        self.add_line('e2', (4, 40), (4, 26))
        self.add_line('e3', (44, 25), (44, 40))
        self.add_line('e4', (44, 40), (34, 40))
        self.add_arc('e5-1', (34, 40), (26, 27), radius_x=11, sweep=False)
        self.add_arc('e5-2', (26, 27), (14, 36), radius_x=10, sweep=False)
        self.add_arc('e6-1', (4, 26), (6, 19), radius_x=17)
        self.add_arc('e6-2', (6, 19), (13, 11), radius_x=21)
        self.add_line('e6-3', (13, 11), (17, 9))
        self.add_line('e6-4', (17, 9), (24, 8))
        self.add_arc('e6-5', (24, 8), (44, 25), radius_x=21)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e3', 'e4', closed=True)
