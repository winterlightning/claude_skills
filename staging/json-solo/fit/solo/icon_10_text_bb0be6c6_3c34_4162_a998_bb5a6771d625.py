"""10 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb0be6c6-3c34-4162-a998-bb5a6771d625'
SOURCE_PATH = 'icons-json/other/10 (text)_bb0be6c6-3c34-4162-a998-bb5a6771d625.json'
AUTHOR = 'json_to_solo'

class Icon10TextOther(Solo48):
    icon_id = 'icon-10-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (11, 8), (11, 40))
        self.add_arc('e1', (4, 14), (11, 8), radius_x=16, sweep=False)
        self.add_arc('e2-1', (24, 24), (34, 8), radius_x=13)
        self.add_arc('e2-2', (34, 8), (40, 11), radius_x=8)
        self.add_arc('e2-3', (40, 11), (43, 17), radius_x=17)
        self.add_line('e2-4', (43, 17), (44, 24))
        self.add_line('e3-1', (44, 24), (43, 31))
        self.add_arc('e3-2', (43, 31), (41, 36), radius_x=18)
        self.add_arc('e3-3', (41, 36), (38, 39), radius_x=10)
        self.add_line('e3-4', (38, 39), (34, 40))
        self.add_arc('e3-5', (34, 40), (24, 24), radius_x=13)
        self.add_contour('c0', 'e1', 'e0')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
