"""Monument (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f142849-8b23-40f0-aba8-d7cdaa500f99'
SOURCE_PATH = 'pictographic-primitives/symbol/monument_7f142849-8b23-40f0-aba8-d7cdaa500f99.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Monument(Solo48):
    icon_id = 'monument'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('monument', 'symbol')

    def build(self):
        self.add_line('e0', (6, 42), (42, 42))
        self.add_line('e1', (35, 29), (12, 29))
        self.add_line('e2', (7, 37), (6, 42))
        self.add_line('e3', (35, 29), (35, 24))
        self.add_line('e4', (13, 22), (13, 29))
        self.add_line('e5', (24, 6), (24, 13))
        self.add_arc('e6-1', (42, 42), (40, 34), radius_x=25, sweep=False)
        self.add_arc('e6-2', (40, 34), (35, 29), radius_x=7, sweep=False)
        self.add_arc('e7', (12, 29), (7, 37), radius_x=15, sweep=False)
        self.add_arc('e8-1', (35, 24), (21, 13), radius_x=11, sweep=False)
        self.add_arc('e8-2', (21, 13), (13, 22), radius_x=11, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e8-1', 'e8-2', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
