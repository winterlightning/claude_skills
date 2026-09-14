"""2-0 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7166f712-4d90-4e1d-9e81-eb0a413b8372'
SOURCE_PATH = 'icons-json/other/2-0 (text)_7166f712-4d90-4e1d-9e81-eb0a413b8372.json'
AUTHOR = 'json_to_solo'

class Icon20TextOther(Solo48):
    icon_id = 'icon-2-0-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (11, 24), (4, 40))
        self.add_line('e1', (4, 40), (13, 40))
        self.add_arc('e2-1', (4, 14), (8, 8), radius_x=10)
        self.add_arc('e2-2', (8, 8), (11, 24), radius_x=11)
        self.add_arc('e3', (23, 18), (23, 19), radius_x=19, sweep=False)
        self.add_arc('e4', (23, 35), (23, 37), radius_x=39)
        self.add_arc('e5-1', (33, 24), (34, 14), radius_x=52)
        self.add_arc('e5-2', (34, 14), (38, 8), radius_x=6)
        self.add_arc('e5-3', (38, 8), (43, 14), radius_x=6)
        self.add_line('e5-4', (43, 14), (44, 24))
        self.add_line('e5-5', (44, 24), (43, 34))
        self.add_arc('e5-6', (43, 34), (39, 40), radius_x=6)
        self.add_arc('e5-7', (39, 40), (34, 33), radius_x=7)
        self.add_arc('e5-8', (34, 33), (33, 24), radius_x=49)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0', 'e1')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', closed=True)
