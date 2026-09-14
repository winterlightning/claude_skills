"""Card (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea0b88fe-d35a-445a-9011-2bdc59c40a03'
SOURCE_PATH = 'icons-json/business/card_ea0b88fe-d35a-445a-9011-2bdc59c40a03.json'
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
        self.add_line('e0', (4, 20), (4, 15))
        self.add_line('e1', (4, 20), (4, 36))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 36), (44, 19))
        self.add_line('e4', (44, 19), (44, 12))
        self.add_line('e5', (41, 8), (7, 8))
        self.add_line('e6', (4, 12), (4, 15))
        self.add_line('e7', (31, 29), (36, 29))
        self.add_bezier('e8', (4, 36), ((4.445, 37.551), (5.509, 40), (7, 40)))
        self.add_bezier('e9', (41, 40), ((42.227, 40), (44, 37.674), (44, 36)))
        self.add_bezier('e10', (44, 12), ((43.564, 10.4), (42.527, 8), (41, 8)))
        self.add_bezier('e11', (7, 8), ((6.945, 8), (6.627, 8.012), (6.573, 8.012)), ((5.445, 8.012), (4.018, 10.006), (4.018, 11.545)), ((4.009, 11.594), (4.009, 11.951), (4, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', 'e11', 'e6')
        self.add_contour('c2', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
