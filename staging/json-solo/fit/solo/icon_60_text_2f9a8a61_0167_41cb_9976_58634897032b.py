"""60 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f9a8a61-0167-41cb-9976-58634897032b'
SOURCE_PATH = 'icons-json/text/60 (text)_2f9a8a61-0167-41cb-9976-58634897032b.json'
AUTHOR = 'json_to_solo'

class Icon60TextText(Solo48):
    icon_id = 'icon-60-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_arc('e0-1', (18, 13), (12, 8), radius_x=8, sweep=False)
        self.add_arc('e0-2', (12, 8), (5, 15), radius_x=8, sweep=False)
        self.add_line('e0-3', (5, 15), (4, 26))
        self.add_line('e0-4', (4, 26), (4, 29))
        self.add_arc('e1-1', (28, 24), (36, 8), radius_x=13)
        self.add_arc('e1-2', (36, 8), (42, 13), radius_x=7)
        self.add_line('e1-3', (42, 13), (44, 24))
        self.add_line('e1-4', (44, 24), (43, 32))
        self.add_arc('e1-5', (43, 32), (41, 37), radius_x=17)
        self.add_arc('e1-6', (41, 37), (36, 40), radius_x=6)
        self.add_arc('e1-7', (36, 40), (28, 24), radius_x=13)
        self.add_arc('e2-1', (4, 29), (6, 37), radius_x=17, sweep=False)
        self.add_arc('e2-2', (6, 37), (8, 39), radius_x=6, sweep=False)
        self.add_line('e2-3', (8, 39), (12, 40))
        self.add_arc('e2-4', (12, 40), (12, 20), radius_x=11, sweep=False)
        self.add_arc('e2-5', (12, 20), (6, 23), radius_x=6, sweep=False)
        self.add_arc('e2-6', (6, 23), (4, 29), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', closed=True)
        self.relate('connect', 'c0', 'c2')
