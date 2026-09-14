"""17 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '674016cf-6aeb-4dd5-ac72-415a7e797cae'
SOURCE_PATH = 'icons-json/other/17 (text)_674016cf-6aeb-4dd5-ac72-415a7e797cae.json'
AUTHOR = 'json_to_solo'

class Icon17Text(Solo48):
    icon_id = 'icon-17-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (24, 8), (44, 8))
        self.add_line('e2', (44, 8), (30, 40))
        self.add_arc('e3', (4, 14), (12, 8), radius_x=20, sweep=False)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e2')
