'Iota symbol: four equal curved arms preserve the rotational motif with clear separation and a shared construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85afe198-8caf-4a8a-b751-b82fbc6bda8c'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto iota_85afe198-8caf-4a8a-b751-b82fbc6bda8c.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoIota(Solo48):
    icon_id = 'virtual-coin-crypto-iota'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'iota', 'finance')

    def build(self) -> None:
        # Four repeated curved arms retain the rotational movement and clear separation.
        for i in range(4):
            def p(x,y):
                for _ in range(i):x,y=48-y,x
                return x,y
            self.add_arc(f'outer-{i}',p(6,19),p(19,6),radius_x=13)
            self.add_bezier(f'hook-{i}',p(19,6),(p(22,6),p(22,15),p(17,18)))
            self.add_contour(f'arm-{i}',f'outer-{i}',f'hook-{i}')
