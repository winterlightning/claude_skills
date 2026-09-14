"""4g (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac8587c1-0df5-4aea-b48e-de1aeb5f9c83'
SOURCE_PATH = 'icons-json/other/4g (text)_ac8587c1-0df5-4aea-b48e-de1aeb5f9c83.json'
AUTHOR = 'json_to_solo'

class Icon4gText(Solo48):
    icon_id = 'icon-4g-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('4g', 'text', 'other')

    def build(self):
        self.add_line('e0', (19, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_line('e3', (44, 33), (44, 25))
        self.add_line('e4', (44, 25), (38, 25))
        self.add_line('e5-1', (43, 13), (41, 9))
        self.add_line('e5-2', (41, 9), (37, 8))
        self.add_arc('e5-3', (37, 8), (28, 20), radius_x=10, sweep=False)
        self.add_arc('e5-4', (28, 20), (29, 34), radius_x=38, sweep=False)
        self.add_arc('e5-5', (29, 34), (36, 40), radius_x=8, sweep=False)
        self.add_line('e5-6', (36, 40), (40, 39))
        self.add_arc('e5-7', (40, 39), (43, 36), radius_x=7, sweep=False)
        self.add_line('e5-8', (43, 36), (44, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e3', 'e4')
