"""Currency pound (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbbacb30-44fc-5de5-a355-689497bccffd'
SOURCE_PATH = 'pictographic-primitives/money/currency pound_dbbacb30-44fc-5de5-a355-689497bccffd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CurrencyPound(Solo48):
    icon_id = 'currency-pound'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'pound', 'money')

    def build(self):
        self.add_line('e0', (17, 24), (17, 35))
        self.add_line('e1', (9, 24), (30, 24))
        self.add_line('e2', (40, 44), (10, 44))
        self.add_arc('e3-1', (39, 11), (34, 5), radius_x=8, sweep=False)
        self.add_line('e3-2', (34, 5), (28, 4))
        self.add_line('e3-3', (28, 4), (22, 5))
        self.add_arc('e3-4', (22, 5), (17, 11), radius_x=10, sweep=False)
        self.add_arc('e3-5', (17, 11), (17, 24), radius_x=56, sweep=False)
        self.add_arc('e4-1', (17, 35), (9, 44), radius_x=11)
        self.add_arc('e4-2', (9, 44), (8, 44), radius_x=22, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
