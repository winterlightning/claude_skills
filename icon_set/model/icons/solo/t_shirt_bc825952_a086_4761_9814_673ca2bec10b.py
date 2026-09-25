"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc825952-a086-4761-9814-673ca2bec10b'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_bc825952-a086-4761-9814-673ca2bec10b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TShirtBc825952(Solo48):
    icon_id = 't-shirt-bc825952'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        self.add_line('e0', (11, 11), (4, 18))
        self.add_line('e1', (4, 18), (10, 24))
        self.add_line('e2', (10, 24), (14, 21))
        self.add_line('e3', (14, 21), (14, 40))
        self.add_line('e4', (14, 40), (35, 40))
        self.add_line('e5', (35, 40), (35, 21))
        self.add_line('e6', (35, 21), (38, 24))
        self.add_line('e7', (38, 24), (44, 18))
        self.add_line('e8', (44, 18), (37, 10))
        self.add_line('e9-1', (37, 10), (32, 8))
        self.add_line('e9-2', (32, 8), (31, 8))
        self.add_arc('e9-3', (31, 8), (27, 13), radius_x=8)
        self.add_arc('e9-4', (27, 13), (24, 14), radius_x=6)
        self.add_arc('e9-5', (24, 14), (17, 8), radius_x=7)
        self.add_arc('e9-6', (17, 8), (11, 11), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', closed=True)
