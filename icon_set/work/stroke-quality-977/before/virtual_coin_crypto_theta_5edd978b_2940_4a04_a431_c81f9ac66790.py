"""Virtual coin crypto theta (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5edd978b-2940-4a04-a431-c81f9ac66790'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto theta_5edd978b-2940-4a04-a431-c81f9ac66790.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoTheta(Solo48):
    icon_id = 'virtual-coin-crypto-theta'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'theta', 'money')

    def build(self):
        self.add_line('e0', (24, 13), (24, 18))
        self.add_line('e1', (18, 18), (24, 18))
        self.add_line('e2', (30, 18), (24, 18))
        self.add_line('e3', (18, 29), (24, 29))
        self.add_line('e4', (24, 34), (24, 29))
        self.add_line('e5', (29, 29), (24, 29))
        self.add_line('e6', (38, 4), (10, 4))
        self.add_line('e7', (8, 7), (8, 41))
        self.add_line('e8', (10, 44), (37, 44))
        self.add_line('e9', (40, 41), (40, 7))
        self.add_line('e10', (10, 4), (8, 7))
        self.add_line('e11', (8, 41), (10, 44))
        self.add_arc('e12', (37, 44), (40, 41), radius_x=3, sweep=False)
        self.add_line('e13', (40, 7), (38, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e10', 'e7', 'e11', 'e8', 'e12', 'e9', 'e13', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
