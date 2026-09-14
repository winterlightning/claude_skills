"""Paragraph (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a023cd36-2b3e-4170-a467-848947816409'
SOURCE_PATH = 'icons-json/interface-essential/paragraph_a023cd36-2b3e-4170-a467-848947816409.json'
AUTHOR = 'json_to_solo'

class ParagraphInterfaceEssential(Solo48):
    icon_id = 'paragraph-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paragraph', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
