"""At (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fbe570f-6495-4b09-a326-af8a6324ecf7'
SOURCE_PATH = 'icons-json/symbol/at (text u)_7fbe570f-6495-4b09-a326-af8a6324ecf7.json'
AUTHOR = 'json_to_solo'

class AtTextUSymbol(Solo48):
    icon_id = 'at-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('at', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (23, 27), (17, 6))
        self.add_line('e1', (14, 5), (8, 27))
        self.add_line('e2', (11, 19), (21, 19))
        self.add_line('e3', (34, 4), (34, 20))
        self.add_line('e4', (31, 10), (38, 10))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (17, 6), ((16.714, 4.982), (16.488, 4.018), (15.419, 4.018)), ((15.309, 4.009), (15.208, 4.009), (15.099, 4)), ((14.333, 4), (14.404, 4.473), (14, 5)))
        self.add_bezier('e7', (34, 20), ((34, 22.273), (34.914, 25.564), (37.069, 26.482)), ((38.038, 26.891), (38.998, 27.109), (40, 27)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
