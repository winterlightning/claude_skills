"""Virtual coin crypto holo (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f78271eb-4357-4efb-8b9c-a23fe0c4d8ae'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto holo_f78271eb-4357-4efb-8b9c-a23fe0c4d8ae.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoHoloFinance(Solo48):
    icon_id = 'virtual-coin-crypto-holo-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'holo', 'finance')

    def build(self):
        self.add_line('sym-e0', (9, 24), (19, 24))
        self.add_line('sym-e1', (19, 24), (29, 24))
        self.add_line('sym-e2', (29, 24), (39, 24))
        self.add_bezier('sym-e3', (4, 8), ((4.218, 8), (4.782, 8), (5, 8)))
        self.add_bezier('sym-e4', (5, 8), ((6.6, 8), (7.609, 8.335), (9, 9)))
        self.add_bezier('sym-e5', (9, 9), ((13.355, 11.088), (16.791, 15.663), (18, 20)))
        self.add_bezier('sym-e6', (18, 20), ((18.382, 21.406), (18.864, 22.568), (19, 24)))
        self.add_bezier('sym-e7', (19, 24), ((18.864, 25.432), (18.382, 26.594), (18, 28)))
        self.add_bezier('sym-e8', (18, 28), ((16.791, 32.337), (13.355, 36.912), (9, 39)))
        self.add_bezier('sym-e9', (9, 39), ((7.609, 39.665), (6.6, 40), (5, 40)))
        self.add_bezier('sym-e10', (5, 40), ((4.782, 40), (4.218, 40), (4, 40)))
        self.add_bezier('sym-e11', (44, 8), ((43.909, 8), (44, 8), (44, 8)))
        self.add_bezier('sym-e12', (44, 8), ((42.445, 8), (40.364, 8.368), (39, 9)))
        self.add_bezier('sym-e13', (39, 9), ((32.827, 11.863), (29.545, 17.886), (29, 24)))
        self.add_bezier('sym-e14', (29, 24), ((29.545, 30.114), (32.827, 36.137), (39, 39)))
        self.add_bezier('sym-e15', (39, 39), ((40.364, 39.632), (42.445, 40), (44, 40)))
        self.add_bezier('sym-e16', (44, 40), ((44, 40), (43.909, 40), (44, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
