"""Sound (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fcea682-f705-4648-b91c-f4d4d43e6872'
SOURCE_PATH = 'pictographic-primitives/interface-essential/sound_7fcea682-f705-4648-b91c-f4d4d43e6872.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SoundInterfaceEssential(Solo48):
    icon_id = 'sound-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('sound', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 10), (18, 6))
        self.add_line('e1', (18, 6), (18, 42))
        self.add_line('e2', (31, 35), (31, 13))
        self.add_line('e3', (6, 31), (6, 17))
        self.add_line('e4', (42, 26), (42, 22))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
