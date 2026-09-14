"""53 (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74616fe2-7fa5-4153-90e2-d47735996627'
SOURCE_PATH = 'icons-json/other/53_74616fe2-7fa5-4153-90e2-d47735996627.json'
AUTHOR = 'json_to_solo'

class Icon53Other(Solo48):
    icon_id = 'icon-53-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('other',)

    def build(self):
        self.add_line('e0', (18, 8), (6, 8))
        self.add_line('e1', (6, 8), (5, 22))
        self.add_arc('e2-1', (5, 22), (15, 21), radius_x=8)
        self.add_arc('e2-2', (15, 21), (19, 30), radius_x=10)
        self.add_arc('e2-3', (19, 30), (11, 40), radius_x=9)
        self.add_line('e2-4', (11, 40), (7, 39))
        self.add_arc('e2-5', (7, 39), (4, 35), radius_x=6)
        self.add_line('e3-1', (30, 13), (33, 9))
        self.add_line('e3-2', (33, 9), (37, 8))
        self.add_arc('e3-3', (37, 8), (42, 11), radius_x=6)
        self.add_line('e3-4', (42, 11), (44, 16))
        self.add_line('e3-5', (44, 16), (42, 21))
        self.add_arc('e3-6', (42, 21), (36, 24), radius_x=9)
        self.add_line('e3-7', (36, 24), (37, 24))
        self.add_arc('e3-8', (37, 24), (42, 26), radius_x=9)
        self.add_line('e3-9', (42, 26), (44, 32))
        self.add_line('e3-10', (44, 32), (43, 36))
        self.add_arc('e3-11', (43, 36), (37, 40), radius_x=7)
        self.add_line('e3-12', (37, 40), (33, 39))
        self.add_arc('e3-13', (33, 39), (29, 34), radius_x=7)
        self.add_contour('c0', 'e0', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', 'e3-13')
