"""Card (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '006f0542-de8b-4cfd-9623-f45ac4159bfd'
SOURCE_PATH = 'icons-json/business/card_006f0542-de8b-4cfd-9623-f45ac4159bfd.json'
AUTHOR = 'json_to_solo'

class Card006f0542(Solo48):
    icon_id = 'card-006f0542'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('e0', (4, 15), (4, 36))
        self.add_line('e1', (7, 40), (41, 40))
        self.add_line('e2', (44, 36), (44, 19))
        self.add_line('e3', (44, 19), (44, 12))
        self.add_line('e4', (41, 8), (7, 8))
        self.add_line('e5', (4, 12), (4, 20))
        self.add_line('e6', (12, 29), (17, 29))
        self.add_bezier('e7', (4, 36), ((4.445, 37.563), (5.509, 40), (7, 40)))
        self.add_bezier('e8', (41, 40), ((42.227, 40), (44, 37.674), (44, 36)))
        self.add_bezier('e9', (44, 12), ((43.564, 10.4), (42.527, 8), (41, 8)))
        self.add_bezier('e10', (7, 8), ((6.945, 8), (6.627, 8.012), (6.573, 8.012)), ((5.4, 8.012), (4, 10.449), (4, 12)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c1', 'e6')
