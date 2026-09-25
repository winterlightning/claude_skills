"""File (emails), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5bd8438c-94c0-4326-8e22-5188c667350d'
SOURCE_PATH = 'pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'
AUTHOR = 'gpt-6'

class FileEmails(Solo48):
    icon_id = 'file-emails'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    categories = ('emails', 'primitives')
    aliases = ()
    keywords = ('file', 'emails')

    def build(self):
        self.add_line('e0', (17, 19), (31, 19))
        self.add_line('e1', (17, 29), (31, 29))
        self.add_line('e2', (8, 4), (32, 4))
        self.add_line('e4', (32, 4), (40, 13))
        self.add_line('e5', (40, 13), (40, 44))
        self.add_line('e6', (40, 44), (8, 44))
        self.add_line('e9', (8, 44), (8, 4))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e4', 'e5', 'e6', 'e9', closed=True)
