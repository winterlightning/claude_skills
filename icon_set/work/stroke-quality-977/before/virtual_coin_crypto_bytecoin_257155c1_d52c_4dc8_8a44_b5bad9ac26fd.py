"""virtual-coin-crypto-bytecoin: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '257155c1-d52c-4dc8-8a44-b5bad9ac26fd'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto bytecoin_257155c1-d52c-4dc8-8a44-b5bad9ac26fd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class VirtualCoinCryptoBytecoin(Solo48):
    icon_id = 'virtual-coin-crypto-bytecoin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'bytecoin', 'money')

    def build(self):
        # SQUARE (6,6)-(42,42); retain Bytecoin crossbar, match the two bowls.
        # Construction reference: Lucide bold: coherent arc bowls
        self.add_line('top',(14,6),(32,6))
        self.add_arc('upper-bowl',(32,6),(32,24),radius_x=10,radius_y=9)
        self.add_arc('lower-bowl',(32,24),(32,42),radius_x=10,radius_y=9)
        self.add_line('bottom',(32,42),(14,42))
        self.add_line('stem',(14,42),(14,6))
        self.add_contour('letter','top','upper-bowl','lower-bowl','bottom','stem',closed=True)
        self.add_line('crossbar',(6,24),(32,24))
        self.relate('connect','crossbar','letter')
