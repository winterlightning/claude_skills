"""Virtual coin cryptocurrency (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd4e64b6-abb6-48f9-9ff6-6bd02c94c7b7'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin cryptocurrency_fd4e64b6-abb6-48f9-9ff6-6bd02c94c7b7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptocurrency(Solo48):
    icon_id = 'virtual-coin-cryptocurrency'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'cryptocurrency', 'money')

    def build(self):
        self.add_line('e0', (17, 33), (17, 16))
        self.add_line('e1', (19, 15), (24, 22))
        self.add_line('e2', (24, 22), (29, 15))
        self.add_line('e3', (31, 16), (31, 33))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5', (17, 16), (19, 15), radius_x=2)
        self.add_arc('e6', (29, 15), (31, 16), radius_x=2)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e6', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
