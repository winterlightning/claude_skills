"""Virtual coin crypto infinite (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3462919-e2c3-488f-97ad-cc3959be0886'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto infinite_a3462919-e2c3-488f-97ad-cc3959be0886.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoInfinite(Solo48):
    icon_id = 'virtual-coin-crypto-infinite'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'infinite', 'finance')

    def build(self):
        self.add_bezier('sym-e0', (24, 23), ((23.979, 23.042), (24.021, 22.958), (24, 23)))
        self.add_bezier('sym-e1', (24, 23), ((23.682, 22.328), (23.318, 21.672), (23, 21)))
        self.add_bezier('sym-e2', (23, 21), ((22.436, 19.832), (21.591, 18.136), (21, 17)))
        self.add_bezier('sym-e3', (21, 17), ((18.936, 13.032), (16.318, 8), (13, 8)))
        self.add_bezier('sym-e4', (13, 8), ((12.864, 8), (13.136, 8), (13, 8)))
        self.add_bezier('sym-e5', (13, 8), ((12.8, 8), (12.2, 8), (12, 8)))
        self.add_bezier('sym-e6', (12, 8), ((7.464, 8), (4, 16.496), (4, 24)))
        self.add_bezier('sym-e7', (4, 24), ((4, 24.128), (4, 23.872), (4, 24)))
        self.add_bezier('sym-e8', (4, 24), ((4, 24.384), (4, 24.616), (4, 25)))
        self.add_bezier('sym-e9', (4, 25), ((4, 31.976), (6.736, 40), (11, 40)))
        self.add_bezier('sym-e10', (11, 40), ((11.073, 40), (11.927, 40), (12, 40)))
        self.add_bezier('sym-e11', (12, 40), ((12.155, 40), (11.845, 40), (12, 40)))
        self.add_bezier('sym-e12', (12, 40), ((17.091, 40), (21.227, 28.192), (24, 22)))
        self.add_bezier('sym-e13', (24, 22), ((26.773, 28.192), (30.909, 40), (36, 40)))
        self.add_bezier('sym-e14', (36, 40), ((36.155, 40), (35.845, 40), (36, 40)))
        self.add_bezier('sym-e15', (36, 40), ((36.073, 40), (36.927, 40), (37, 40)))
        self.add_bezier('sym-e16', (37, 40), ((41.264, 40), (44, 31.976), (44, 25)))
        self.add_bezier('sym-e17', (44, 25), ((44, 24.616), (44, 24.384), (44, 24)))
        self.add_bezier('sym-e18', (44, 24), ((44, 23.872), (44, 24.128), (44, 24)))
        self.add_bezier('sym-e19', (44, 24), ((44, 16.496), (40.536, 8), (36, 8)))
        self.add_bezier('sym-e20', (36, 8), ((35.8, 8), (35.2, 8), (35, 8)))
        self.add_bezier('sym-e21', (35, 8), ((34.864, 8), (35.136, 8), (35, 8)))
        self.add_bezier('sym-e22', (35, 8), ((31.682, 8), (29.064, 13.032), (27, 17)))
        self.add_bezier('sym-e23', (27, 17), ((26.409, 18.136), (25.564, 19.832), (25, 21)))
        self.add_bezier('sym-e24', (25, 21), ((24.682, 21.672), (24.318, 22.328), (24, 23)))
        self.add_bezier('sym-e25', (24, 23), ((23.979, 22.958), (24.021, 23.042), (24, 23)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
