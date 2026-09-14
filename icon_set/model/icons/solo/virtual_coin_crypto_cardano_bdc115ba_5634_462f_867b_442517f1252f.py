'Cardano coin: a balanced radial dot cluster inside the round coin, replacing the cramped central ring with a solid dot.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdc115ba-5634-462f-867b-442517f1252f'
SOURCE_PATH = 'icons-json/money/virtual coin crypto cardano_bdc115ba-5634-462f-867b-442517f1252f.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoCardano(Solo48):
    icon_id = 'virtual-coin-crypto-cardano'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'cardano', 'money')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Retain the radial dot cluster; the central ring becomes a clear solid dot.
        for i,p in enumerate(((24,24),(24,13),(32,16),(35,24),(32,32),(24,35),(16,32),(13,24),(16,16))):
            self.add_dot(f'dot-{i}',p)
