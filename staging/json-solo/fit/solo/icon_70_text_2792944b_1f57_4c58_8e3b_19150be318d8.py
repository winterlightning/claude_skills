"""70 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2792944b-1f57-4c58-8e3b-19150be318d8'
SOURCE_PATH = 'icons-json/text/70 (text)_2792944b-1f57-4c58-8e3b-19150be318d8.json'
AUTHOR = 'json_to_solo'

class Icon70TextText(Solo48):
    icon_id = 'icon-70-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (4, 8), (19, 8))
        self.add_line('e1', (19, 8), (9, 40))
        self.add_arc('e2-1', (29, 24), (32, 10), radius_x=25)
        self.add_arc('e2-2', (32, 10), (36, 8), radius_x=5)
        self.add_arc('e2-3', (36, 8), (42, 13), radius_x=7)
        self.add_line('e2-4', (42, 13), (44, 24))
        self.add_line('e2-5', (44, 24), (43, 32))
        self.add_arc('e2-6', (43, 32), (36, 40), radius_x=8)
        self.add_arc('e2-7', (36, 40), (29, 24), radius_x=13)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', closed=True)
