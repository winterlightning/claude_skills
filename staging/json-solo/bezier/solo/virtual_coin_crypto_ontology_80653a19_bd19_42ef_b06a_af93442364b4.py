"""Virtual coin crypto ontology (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80653a19-bd19-42ef-b06a-af93442364b4'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto ontology_80653a19-bd19-42ef-b06a-af93442364b4.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoOntologyFinance(Solo48):
    icon_id = 'virtual-coin-crypto-ontology-finance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'ontology', 'finance')

    def build(self):
        self.add_line('e0', (12, 12), (17, 8))
        self.add_line('e1', (42, 22), (42, 42))
        self.add_line('e2', (42, 42), (6, 6))
        self.add_line('e3', (6, 6), (6, 24))
        self.add_line('e4', (31, 39), (36, 36))
        self.add_bezier('e5', (17, 8), ((19.193, 6.748), (22.405, 6.016), (24.965, 6.016)), ((25.26, 6.016), (25.555, 6), (25.849, 6)), ((25.996, 6), (26.144, 6.008), (26.291, 6.008)), ((27.42, 6.008), (28.582, 6.303), (29.67, 6.565)), ((35.52, 7.98), (40.069, 12.815), (41.493, 18.592)), ((41.722, 19.516), (42, 21.051), (42, 22)))
        self.add_bezier('e6', (6, 24), ((6, 25.612), (6.843, 28.099), (7.505, 29.58)), ((11.515, 38.449), (22.041, 42), (31, 39)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e6', 'e4')
