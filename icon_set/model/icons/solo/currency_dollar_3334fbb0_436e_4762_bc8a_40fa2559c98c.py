"""Currency dollar (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3334fbb0-436e-4762-bc8a-40fa2559c98c'
SOURCE_PATH = 'pictographic-primitives/money/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CurrencyDollar(Solo48):
    icon_id = 'currency-dollar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('money', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('currency', 'dollar', 'money')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (24, 4), (24, 10))
        self.add_line('e1', (24, 44), (24, 38))
        self.add_bezier('e2', (8, 36), ((13.52, 37.673), (17.808, 37.691), (24, 37.636)), ((30.816, 37.573), (40, 36.073), (40, 31.3)), ((40, 31.225), (39.984, 31.154), (39.984, 31.091)), ((39.984, 24.418), (24.432, 24.373), (16.496, 22.809)), ((12.144, 21.955), (8.032, 20.055), (8.032, 17.209)), ((8.032, 17.027), (8, 16.845), (8, 16.664)), ((8, 16.545), (8.016, 16.436), (8.016, 16.327)), ((8.016, 15.764), (8.432, 15.145), (8.752, 14.618)), ((10.864, 11.182), (18.352, 10.364), (24, 10.364)), ((28.576, 10.364), (33.032, 10.709), (37, 12)))
        self.add_contour('c0', 'e2', closed=False)
        self.add_contour('c1', 'e0', closed=False)
        self.add_contour('c2', 'e1', closed=False)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
