"""30 (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '938d3539-4c60-42ce-a3e5-41e92e309fc2'
SOURCE_PATH = 'icons-json/other/30_938d3539-4c60-42ce-a3e5-41e92e309fc2.json'
AUTHOR = 'json_to_solo'

class Icon30Other(Solo48):
    icon_id = 'icon-30-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('other',)

    def build(self):
        self.add_arc('e0-1', (5, 13), (11, 8), radius_x=7)
        self.add_arc('e0-2', (11, 8), (17, 18), radius_x=8)
        self.add_arc('e0-3', (17, 18), (10, 24), radius_x=7)
        self.add_arc('e0-4', (10, 24), (17, 35), radius_x=8)
        self.add_arc('e0-5', (17, 35), (11, 40), radius_x=7)
        self.add_arc('e0-6', (11, 40), (4, 34), radius_x=8)
        self.add_arc('e1-1', (28, 24), (29, 14), radius_x=34)
        self.add_arc('e1-2', (29, 14), (35, 8), radius_x=7)
        self.add_arc('e1-3', (35, 8), (43, 16), radius_x=9)
        self.add_line('e1-4', (43, 16), (44, 24))
        self.add_line('e1-5', (44, 24), (42, 35))
        self.add_arc('e1-6', (42, 35), (36, 40), radius_x=7)
        self.add_arc('e1-7', (36, 40), (28, 24), radius_x=13)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
