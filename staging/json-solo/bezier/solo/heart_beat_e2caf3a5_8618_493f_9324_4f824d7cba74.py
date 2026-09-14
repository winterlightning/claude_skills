"""Heart beat (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2caf3a5-8618-493f-9324-4f824d7cba74'
SOURCE_PATH = 'icons-json/symbol/heart beat_e2caf3a5-8618-493f-9324-4f824d7cba74.json'
AUTHOR = 'json_to_solo'

class HeartBeatSymbol(Solo48):
    icon_id = 'heart-beat-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('heart', 'beat', 'symbol')

    def build(self):
        self.add_line('e0', (4, 26), (10, 26))
        self.add_line('e1', (10, 26), (15, 8))
        self.add_line('e2', (15, 8), (24, 40))
        self.add_line('e3', (24, 40), (29, 14))
        self.add_line('e4', (29, 14), (34, 30))
        self.add_line('e5', (39, 26), (44, 26))
        self.add_bezier('e6', (34, 30), ((34.3, 29.488), (36.409, 25.744), (36.818, 25.6)), ((37.627, 25.296), (38.182, 26), (39, 26)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e6', 'e5')
