"""Hill 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (44, 9), ((43.873, 8.643), (43.9, 8), (43.409, 8)), ((43, 8), (42.409, 8), (42, 8)))
        self.add_bezier('e4', (5, 38), ((4.669, 38.254), (4, 38.181), (4, 38.777)), ((4, 38.787), (4, 38.796), (4, 38.806)), ((4, 39.557), (4.682, 39.68), (5, 40)))
        self.add_bezier('e5', (43, 40), ((43.055, 40), (43.209, 39.988), (43.264, 39.988)), ((43.845, 39.988), (43.818, 39.455), (44, 39)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
