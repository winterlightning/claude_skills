"""24 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3ef1255-7230-466e-a0e3-b1897407d9eb'
SOURCE_PATH = 'icons-json/other/24 (text)_e3ef1255-7230-466e-a0e3-b1897407d9eb.json'
AUTHOR = 'json_to_solo'

class Icon24Text(Solo48):
    icon_id = 'icon-24-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (16, 24), (4, 40))
        self.add_line('e1', (4, 40), (19, 40))
        self.add_line('e2', (44, 32), (29, 32))
        self.add_line('e3', (29, 32), (41, 8))
        self.add_line('e4', (41, 8), (41, 40))
        self.add_arc('e5-1', (5, 14), (12, 8), radius_x=8)
        self.add_arc('e5-2', (12, 8), (16, 24), radius_x=10)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
