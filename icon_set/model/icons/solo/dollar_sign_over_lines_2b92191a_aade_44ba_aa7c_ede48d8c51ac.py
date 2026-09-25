"""Dollar Sign over Lines. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide dollar-sign: rounded S bowls and vertical currency marks; source specifies two detached horizontal lines below.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b92191a-aade-44ba-aa7c-ede48d8c51ac'
SOURCE_PATH = 'pictographic-primitives/symbol/dollar with texts_2b92191a-aade-44ba-aa7c-ede48d8c51ac.svg'
AUTHOR = 'gpt-6'


class DollarSignOverLines(Solo48):
    icon_id = 'dollar-sign-over-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('dollar', 'money', 'price', 'amount', 'finance', 'payment', 'currency', 'total')

    def build(self) -> None:
        self.add_line('s-top', (30, 8), (24, 8))
        self.add_arc('s-upper', (24, 8), (24, 16), radius_x=6, radius_y=4, sweep=False)
        self.add_arc('s-lower', (24, 16), (24, 24), radius_x=6, radius_y=4, sweep=True)
        self.add_line('s-foot', (24, 24), (18, 24))
        self.add_contour('s', 's-top', 's-upper', 's-lower', 's-foot')
        self.add_line('stem-top', (24, 6), (24, 8))
        self.add_line('stem-bottom', (24, 24), (24, 26))
        self.relate("connect", 's', 'stem-top')
        self.relate("connect", 's', 'stem-bottom')
        self.add_line('line-one', (6, 34), (42, 34))
        self.add_line('line-two', (6, 42), (42, 42))
