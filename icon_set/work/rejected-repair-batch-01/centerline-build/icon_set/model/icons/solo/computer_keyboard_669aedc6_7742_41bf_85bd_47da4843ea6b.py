"""Keyboard with one row of three dot keys and a spacebar inside a rounded shell. HRECT_M visible bounds (2,6)-(46,42). Lucide keyboard informed the simplified keys; the crowded second row and stepped shell are removed."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '669aedc6-7742-41bf-85bd-47da4843ea6b'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/keyboard_669aedc6-7742-41bf-85bd-47da4843ea6b.svg'
AUTHOR = 'gpt-6'

class ComputerKeyboard(Solo48):
    icon_id = 'computer-keyboard'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        self.add_line('top',(8,8),(40,8))
        self.add_arc('ne',(40,8),(44,12),radius_x=4)
        self.add_line('right',(44,12),(44,36))
        self.add_arc('se',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('sw',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,12))
        self.add_arc('nw',(4,12),(8,8),radius_x=4)
        self.add_contour('shell','top','ne','right','se','bottom','sw','left','nw',closed=True)
        for i,x in enumerate((14,24,34)):
            self.add_dot('key-'+str(i),(x,19))
        self.add_line('spacebar',(14,29),(34,29))
