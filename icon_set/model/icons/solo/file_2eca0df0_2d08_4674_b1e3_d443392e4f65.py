"""File (emails), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2eca0df0-2d08-4674-b1e3-d443392e4f65'
SOURCE_PATH = 'icons-json/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.json'
AUTHOR = 'json_to_solo'

class File(Solo48):
    icon_id = 'file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('file', 'emails')

    def build(self):
        self.add_line('e0', (10, 4), (32, 4))
        self.add_line('e1', (32, 4), (39, 12))
        self.add_line('e2', (40, 13), (40, 42))
        self.add_line('e3', (38, 44), (10, 44))
        self.add_line('e4', (8, 42), (8, 5))
        self.add_line('e5', (39, 12), (40, 13))
        self.add_arc('e6', (40, 42), (38, 44), radius_x=2)
        self.add_arc('e7', (10, 44), (8, 42), radius_x=2)
        self.add_line('e8', (8, 5), (10, 4))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', closed=True)
