"""A stepped keyboard with two key rows and a long spacebar.

HRECT_M extremes (2,11)-(46,37) leave room for two rows. Lucide keyboard
informs dot keys and a continuous spacebar; keep two keys per row and omit side ticks.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '669aedc6-7742-41bf-85bd-47da4843ea6b'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/keyboard_669aedc6-7742-41bf-85bd-47da4843ea6b.svg'


class ComputerKeyboard(Solo48):
    icon_id = 'computer-keyboard'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        self.add_line('shell-top-1', (5, 17), (12, 17))
        self.add_line('shell-top-2', (12, 17), (16, 11))
        self.add_line('shell-top-3', (16, 11), (32, 11))
        self.add_line('shell-top-4', (32, 11), (36, 17))
        self.add_line('shell-top-5', (36, 17), (43, 17))
        self.add_arc('shell-ne', (43, 17), (46, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('shell-right', (46, 20), (46, 28))
        self.add_arc('shell-se', (46, 28), (43, 31), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('shell-bottom-1', (43, 31), (36, 31))
        self.add_line('shell-bottom-2', (36, 31), (32, 37))
        self.add_line('shell-bottom-3', (32, 37), (16, 37))
        self.add_line('shell-bottom-4', (16, 37), (12, 31))
        self.add_line('shell-bottom-5', (12, 31), (5, 31))
        self.add_arc('shell-sw', (5, 31), (2, 28), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('shell-left', (2, 28), (2, 20))
        self.add_arc('shell-nw', (2, 20), (5, 17), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('shell', 'shell-top-1', 'shell-top-2', 'shell-top-3', 'shell-top-4', 'shell-top-5', 'shell-ne', 'shell-right', 'shell-se', 'shell-bottom-1', 'shell-bottom-2', 'shell-bottom-3', 'shell-bottom-4', 'shell-bottom-5', 'shell-sw', 'shell-left', 'shell-nw', closed=True)
        self.add_dot('key-0-0', (20, 18))
        self.add_dot('key-0-1', (28, 18))
        self.add_dot('key-1-0', (20, 24))
        self.add_dot('key-1-1', (28, 24))
        self.add_line('spacebar', (20, 30), (28, 30))
