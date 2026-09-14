'Decred coin: two opposing curved marks retain their hooked ends with a wider central gap and clear coin margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55e973e5-31ee-4bd8-9749-f78c78d90cc1'
SOURCE_PATH = 'icons-json/money/virtual coin crypto decred_55e973e5-31ee-4bd8-9749-f78c78d90cc1.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoDecred(Solo48):
    icon_id = 'virtual-coin-crypto-decred'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'decred', 'money')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Two opposing curved marks retain the Decred-like counterturn and stay distinct.
        self.add_polyline('left-tip',(16,16),(18,19),(15,19))
        self.add_bezier('left-bowl',(15,19),((13,20),(13,22),(13,24)),((13,28),(16,30),(19,29)))
        self.relate('connect','left-tip','left-bowl')
        self.add_bezier('right-bowl',(29,19),((32,18),(35,20),(35,24)),((35,26),(35,28),(33,29)))
        self.add_polyline('right-tip',(33,29),(30,29),(32,32))
        self.relate('connect','right-tip','right-bowl')
