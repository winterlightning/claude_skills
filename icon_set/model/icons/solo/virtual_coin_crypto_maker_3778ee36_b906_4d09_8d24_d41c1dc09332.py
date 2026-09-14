"""Virtual coin crypto maker (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3778ee36-b906-4d09-8d24-d41c1dc09332'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto maker_3778ee36-b906-4d09-8d24-d41c1dc09332.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoMaker(Solo48):
    icon_id = 'virtual-coin-crypto-maker'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'maker', 'finance')

    def build(self):
        self.add_line('sym-e0', (28, 40), (28, 23))
        self.add_bezier('sym-e1', (28, 23), ((28.182, 22.188), (28.391, 20.48), (29, 20)))
        self.add_line('sym-e2', (29, 20), (44, 8))
        self.add_line('sym-e3', (44, 8), (44, 40))
        self.add_line('sym-e4', (20, 40), (20, 23))
        self.add_bezier('sym-e5', (20, 23), ((19.818, 22.188), (19.609, 20.48), (19, 20)))
        self.add_line('sym-e6', (19, 20), (4, 8))
        self.add_line('sym-e7', (4, 8), (4, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
