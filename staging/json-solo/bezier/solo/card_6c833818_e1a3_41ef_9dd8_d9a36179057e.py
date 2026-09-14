"""Card (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c833818-e1a3-41ef-9dd8-d9a36179057e'
SOURCE_PATH = 'icons-json/business/card_6c833818-e1a3-41ef-9dd8-d9a36179057e.json'
AUTHOR = 'json_to_solo'

class Card(Solo48):
    icon_id = 'card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('sym-e0', (4, 18), (44, 18))
        self.add_line('sym-e1', (44, 18), (44, 36))
        self.add_bezier('sym-e2', (44, 36), ((44, 37.822), (42.345, 40), (41, 40)))
        self.add_line('sym-e3', (41, 40), (24, 40))
        self.add_line('sym-e4', (24, 40), (7, 40))
        self.add_bezier('sym-e5', (7, 40), ((5.655, 40), (4, 37.822), (4, 36)))
        self.add_line('sym-e6', (4, 36), (4, 18))
        self.add_bezier('sym-e7', (4, 18), ((4, 16.08), (4, 13.92), (4, 12)))
        self.add_bezier('sym-e8', (4, 12), ((4, 9.969), (5.4, 8), (7, 8)))
        self.add_line('sym-e9', (7, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (41, 8))
        self.add_bezier('sym-e11', (41, 8), ((42.6, 8), (44, 9.969), (44, 12)))
        self.add_bezier('sym-e12', (44, 12), ((44, 13.92), (44, 16.08), (44, 18)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
