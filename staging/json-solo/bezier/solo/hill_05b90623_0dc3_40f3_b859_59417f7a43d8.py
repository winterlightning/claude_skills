"""Hill (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05b90623-0dc3-40f3-b859-59417f7a43d8'
SOURCE_PATH = 'icons-json/transportation/hill_05b90623-0dc3-40f3-b859-59417f7a43d8.json'
AUTHOR = 'json_to_solo'

class HillTransportation(Solo48):
    icon_id = 'hill-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('hill', 'transportation')

    def build(self):
        self.add_line('e0', (4, 39), (4, 9))
        self.add_line('e1', (6, 8), (43, 38))
        self.add_line('e2', (43, 40), (5, 40))
        self.add_bezier('e3', (4, 9), ((4.127, 8.643), (4.1, 8), (4.591, 8)), ((5, 8), (5.591, 8), (6, 8)))
        self.add_bezier('e4', (43, 38), ((43.331, 38.254), (44, 38.181), (44, 38.777)), ((44, 38.787), (44, 38.796), (44, 38.806)), ((44, 39.557), (43.318, 39.68), (43, 40)))
        self.add_bezier('e5', (5, 40), ((4.945, 40), (4.791, 39.988), (4.736, 39.988)), ((4.155, 39.988), (4.182, 39.455), (4, 39)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
