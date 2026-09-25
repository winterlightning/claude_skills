"""Uptrend arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d828078-5c96-443f-b25a-b44dbc02b54f'
SOURCE_PATH = 'pictographic-primitives/symbol/uptrend arrow_4d828078-5c96-443f-b25a-b44dbc02b54f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class UptrendArrow(Solo48):
    icon_id = 'uptrend-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('uptrend', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (36, 9), (44, 8))
        self.add_line('e1', (44, 8), (27, 33))
        self.add_line('e2', (27, 33), (19, 22))
        self.add_line('e3', (19, 22), (4, 40))
        self.add_line('e4', (43, 19), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
