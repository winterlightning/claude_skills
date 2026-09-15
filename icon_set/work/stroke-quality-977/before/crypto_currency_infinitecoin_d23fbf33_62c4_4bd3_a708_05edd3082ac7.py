"""Crypto currency infinitecoin (money), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd23fbf33-62c4-4bd3-a708-05edd3082ac7'
SOURCE_PATH = 'pictographic-primitives/money/crypto currency infinitecoin_d23fbf33-62c4-4bd3-a708-05edd3082ac7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CryptoCurrencyInfinitecoin(Solo48):
    icon_id = 'crypto-currency-infinitecoin'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('crypto', 'currency', 'infinitecoin', 'money')

    def build(self):
        self.add_bezier('sym-e0', (24, 24), ((26.2, 29.104), (32.227, 40), (36, 40)))
        self.add_bezier('sym-e1', (36, 40), ((36.064, 40), (35.936, 40), (36, 40)))
        self.add_bezier('sym-e2', (36, 40), ((36.155, 40), (36.845, 40), (37, 40)))
        self.add_bezier('sym-e3', (37, 40), ((41.236, 40), (44, 31.992), (44, 25)))
        self.add_bezier('sym-e4', (44, 25), ((44, 24.888), (44, 25.112), (44, 25)))
        self.add_bezier('sym-e5', (44, 25), ((44, 24.584), (44, 24.416), (44, 24)))
        self.add_bezier('sym-e6', (44, 24), ((44, 16.624), (40.473, 8), (36, 8)))
        self.add_bezier('sym-e7', (36, 8), ((35.864, 8), (36.136, 8), (36, 8)))
        self.add_bezier('sym-e8', (36, 8), ((35.809, 8), (35.191, 8), (35, 8)))
        self.add_bezier('sym-e9', (35, 8), ((30.964, 8), (26.373, 16.864), (24, 22)))
        self.add_bezier('sym-e10', (24, 22), ((21.627, 16.864), (17.036, 8), (13, 8)))
        self.add_bezier('sym-e11', (13, 8), ((12.809, 8), (12.191, 8), (12, 8)))
        self.add_bezier('sym-e12', (12, 8), ((11.864, 8), (12.136, 8), (12, 8)))
        self.add_bezier('sym-e13', (12, 8), ((7.527, 8), (4, 16.624), (4, 24)))
        self.add_bezier('sym-e14', (4, 24), ((4, 24.416), (4, 24.584), (4, 25)))
        self.add_bezier('sym-e15', (4, 25), ((4, 25.112), (4, 24.888), (4, 25)))
        self.add_bezier('sym-e16', (4, 25), ((4, 31.992), (6.764, 40), (11, 40)))
        self.add_bezier('sym-e17', (11, 40), ((11.155, 40), (11.845, 40), (12, 40)))
        self.add_bezier('sym-e18', (12, 40), ((12.064, 40), (11.936, 40), (12, 40)))
        self.add_bezier('sym-e19', (12, 40), ((15.773, 40), (21.8, 29.104), (24, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
