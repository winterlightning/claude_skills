"""Keyboard asterisk (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c039b931-f945-573e-b4dd-146dae4b3216'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard asterisk_c039b931-f945-573e-b4dd-146dae4b3216.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class KeyboardAsteriskC039b931(Solo48):
    icon_id = 'keyboard-asterisk-c039b931'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'asterisk', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (12, 12), (36, 36))
        self.add_line('e2', (6, 24), (42, 24))
        self.add_line('e3', (12, 36), (36, 12))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
