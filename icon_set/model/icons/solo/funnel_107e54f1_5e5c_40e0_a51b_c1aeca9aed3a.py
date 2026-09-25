"""Funnel (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '107e54f1-5e5c-40e0-a51b-c1aeca9aed3a'
SOURCE_PATH = 'pictographic-primitives/symbol/funnel_107e54f1-5e5c-40e0-a51b-c1aeca9aed3a.svg'
AUTHOR = 'gpt-6'

class Funnel(Solo48):
    icon_id = 'funnel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('funnel', 'symbol')

    def build(self):
        self.add_line('e0', (19, 42), (19, 26))
        self.add_line('e1', (19, 26), (6, 6))
        self.add_line('e2', (6, 6), (42, 6))
        self.add_line('e3', (42, 6), (29, 26))
        self.add_line('e4', (29, 33), (19, 42))
        self.add_line('e6', (29, 26), (29, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e6', 'e4', closed=True)
