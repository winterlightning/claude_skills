"""Magic wand (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab312eb6-0227-4cb6-98e2-21e3c1f7afe5'
SOURCE_PATH = 'pictographic-primitives/design/magic wand_ab312eb6-0227-4cb6-98e2-21e3c1f7afe5.svg'
AUTHOR = 'gpt-6'

class MagicWand(Solo48):
    icon_id = 'magic-wand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('magic', 'wand', 'design')

    def build(self):
        self.add_line('e0', (28, 19), (31, 26))
        self.add_line('e1', (31, 26), (34, 20))
        self.add_line('e2', (34, 20), (42, 20))
        self.add_line('e4', (42, 20), (36, 14))
        self.add_line('e5', (36, 14), (40, 7))
        self.add_line('e6', (40, 7), (32, 10))
        self.add_line('e7', (31, 10), (26, 6))
        self.add_line('e8', (26, 6), (27, 13))
        self.add_line('e9', (27, 13), (21, 17))
        self.add_line('e10', (21, 17), (28, 19))
        self.add_line('e11', (6, 42), (28, 19))
        self.add_line('e12', (32, 10), (31, 10))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e4', 'e5', 'e6', 'e12', 'e7', 'e8', 'e9', 'e10', closed=True)
        self.add_contour('c1', 'e11', closed=False)
