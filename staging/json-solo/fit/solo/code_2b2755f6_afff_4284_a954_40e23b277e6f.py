"""Code (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b2755f6-afff-4284-a954-40e23b277e6f'
SOURCE_PATH = 'icons-json/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.json'
AUTHOR = 'json_to_solo'

class Code2b2755f6(Solo48):
    icon_id = 'code-2b2755f6'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('code', 'programing')

    def build(self):
        self.add_line('e0', (19, 40), (29, 8))
        self.add_line('e1', (12, 13), (4, 24))
        self.add_line('e2', (4, 24), (12, 35))
        self.add_line('e3', (36, 13), (44, 24))
        self.add_line('e4', (44, 24), (36, 35))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
