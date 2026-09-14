"""Paragraph normal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '302ba70a-58d6-4bc5-8483-4e9e8b75df49'
SOURCE_PATH = 'icons-json/interface-essential/paragraph normal_302ba70a-58d6-4bc5-8483-4e9e8b75df49.json'
AUTHOR = 'json_to_solo'

class ParagraphNormal(Solo48):
    icon_id = 'paragraph-normal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paragraph', 'normal', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (4, 40), (28, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
