'simple-computer-keyboard: Reduced the keys to one evenly spaced row above the spacebar. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6da646a1-34eb-51f2-af2d-b08aed786a57'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg'
AUTHOR = 'gpt-6'

class SimpleComputerKeyboard(Solo48):
    icon_id = 'simple-computer-keyboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        self.add_line('case-top0', (8, 8), (40, 8))
        self.add_arc('case-ne', (40, 8), (44, 12), radius_x=4, sweep=True)
        self.add_line('case-right', (44, 12), (44, 36))
        self.add_arc('case-se', (44, 36), (40, 40), radius_x=4, sweep=True)
        self.add_line('case-bottom0', (40, 40), (8, 40))
        self.add_arc('case-sw', (8, 40), (4, 36), radius_x=4, sweep=True)
        self.add_line('case-left', (4, 36), (4, 12))
        self.add_arc('case-nw', (4, 12), (8, 8), radius_x=4, sweep=True)
        self.add_contour('case', 'case-top0', 'case-ne', 'case-right', 'case-se', 'case-bottom0', 'case-sw', 'case-left', 'case-nw', closed=True)
        for x in (14, 24, 34):
            self.add_dot(f'key-{x}', (x, 18))
        self.add_line('spacebar', (14, 30), (34, 30))
