"""A wide keyboard has two rows of keys and a long spacebar.

Keyshape HRECT_L: visible extremes (0, 6, 48, 42).
Lucide keyboard: rounded rectangle, regular dot keys, centered spacebar. Dashes become dots to retain eight separate keys."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6da646a1-34eb-51f2-af2d-b08aed786a57'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg'
AUTHOR = 'astra-chatgpt'


class SimpleComputerKeyboard(Solo48):
    icon_id = 'simple-computer-keyboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        self.add_line('case-top0', (6, 8), (42, 8))
        self.add_arc('case-ne', (42, 8), (46, 12), radius_x=4, sweep=True)
        self.add_line('case-right', (46, 12), (46, 36))
        self.add_arc('case-se', (46, 36), (42, 40), radius_x=4, sweep=True)
        self.add_line('case-bottom0', (42, 40), (6, 40))
        self.add_arc('case-sw', (6, 40), (2, 36), radius_x=4, sweep=True)
        self.add_line('case-left', (2, 36), (2, 12))
        self.add_arc('case-nw', (2, 12), (6, 8), radius_x=4, sweep=True)
        self.add_contour('case', 'case-top0', 'case-ne', 'case-right', 'case-se', 'case-bottom0', 'case-sw', 'case-left', 'case-nw', closed=True)
        self.add_dot('key-12-16', (12, 16))
        self.add_dot('key-20-16', (20, 16))
        self.add_dot('key-28-16', (28, 16))
        self.add_dot('key-36-16', (36, 16))
        self.add_dot('key-12-24', (12, 24))
        self.add_dot('key-20-24', (20, 24))
        self.add_dot('key-28-24', (28, 24))
        self.add_dot('key-36-24', (36, 24))
        self.add_line('spacebar', (16, 32), (32, 32))
