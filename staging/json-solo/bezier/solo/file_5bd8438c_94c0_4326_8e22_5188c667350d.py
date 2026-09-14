"""File (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bd8438c-94c0-4326-8e22-5188c667350d'
SOURCE_PATH = 'icons-json/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.json'
AUTHOR = 'json_to_solo'

class File5bd8438c(Solo48):
    icon_id = 'file-5bd8438c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('file', 'emails')

    def build(self):
        self.add_line('e0', (17, 19), (31, 19))
        self.add_line('e1', (17, 29), (31, 29))
        self.add_line('e2', (8, 4), (23, 4))
        self.add_line('e3', (23, 4), (32, 4))
        self.add_line('e4', (32, 4), (40, 13))
        self.add_line('e5', (40, 13), (40, 44))
        self.add_line('e6', (40, 44), (32, 44))
        self.add_line('e7', (32, 44), (11, 44))
        self.add_line('e8', (11, 44), (8, 44))
        self.add_line('e9', (8, 44), (8, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', closed=True)
