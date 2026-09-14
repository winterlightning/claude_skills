"""Design file text (tools), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c13e4b1c-0519-4681-b3ca-c44ba40934fa'
SOURCE_PATH = 'icons-json/tools/design file text_c13e4b1c-0519-4681-b3ca-c44ba40934fa.json'
AUTHOR = 'json_to_solo'

class DesignFileText(Solo48):
    icon_id = 'design-file-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('design', 'file', 'text', 'tools')

    def build(self):
        self.add_line('e0', (8, 10), (8, 4))
        self.add_line('e1', (8, 4), (40, 4))
        self.add_line('e2', (40, 4), (40, 11))
        self.add_line('e3', (24, 44), (24, 4))
        self.add_line('e4', (17, 44), (30, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
