"""Virtual coin crypto ontology (finance), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80653a19-bd19-42ef-b06a-af93442364b4'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto ontology_80653a19-bd19-42ef-b06a-af93442364b4.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoOntology(Solo48):
    icon_id = 'virtual-coin-crypto-ontology'
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
        self.add_line('e5-1', (17, 8), (26, 6))
        self.add_arc('e5-2', (26, 6), (42, 22), radius_x=16)
        self.add_arc('e6', (6, 24), (31, 39), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2', 'e3', 'e6', 'e4')
