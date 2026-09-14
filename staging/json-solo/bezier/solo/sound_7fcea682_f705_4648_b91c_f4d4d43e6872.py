"""Sound (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fcea682-f705-4648-b91c-f4d4d43e6872'
SOURCE_PATH = 'icons-json/interface-essential/sound_7fcea682-f705-4648-b91c-f4d4d43e6872.json'
AUTHOR = 'json_to_solo'

class Sound7fcea682(Solo48):
    icon_id = 'sound-7fcea682'
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
