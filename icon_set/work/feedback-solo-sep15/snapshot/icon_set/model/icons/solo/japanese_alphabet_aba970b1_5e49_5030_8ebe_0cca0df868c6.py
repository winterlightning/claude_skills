"""Japanese alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba970b1-5e49-5030-8ebe-0cca0df868c6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/japanese alphabet_aba970b1-5e49-5030-8ebe-0cca0df868c6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class JapaneseAlphabet(Solo48):
    icon_id = 'japanese-alphabet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('japanese', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 21), (19, 6))
        self.add_line('e1', (35, 41), (31, 42))
        self.add_line('e2', (7, 11), (40, 11))
        self.add_line('e3', (22, 41), (20, 37))
        self.add_arc('e4-1', (33, 17), (17, 39), radius_x=37)
        self.add_arc('e4-2', (17, 39), (8, 40), radius_x=9)
        self.add_line('e4-3', (8, 40), (6, 35))
        self.add_arc('e4-4', (6, 35), (19, 21), radius_x=16)
        self.add_arc('e5-1', (20, 37), (19, 21), radius_x=56)
        self.add_arc('e5-2', (19, 21), (38, 23), radius_x=25)
        self.add_arc('e5-3', (38, 23), (42, 31), radius_x=10)
        self.add_arc('e5-4', (42, 31), (35, 41), radius_x=11)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c1', 'c0')
