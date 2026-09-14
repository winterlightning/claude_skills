"""17 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '674016cf-6aeb-4dd5-ac72-415a7e797cae'
SOURCE_PATH = 'icons-json/other/17 (text)_674016cf-6aeb-4dd5-ac72-415a7e797cae.json'
AUTHOR = 'json_to_solo'

class Icon17TextOther(Solo48):
    icon_id = 'icon-17-text-other'
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
        self.add_bezier('e3', (4, 14), ((4.009, 14), (4.009, 13.99), (4.018, 13.99)), ((4.018, 13.94), (4.7, 13.67), (4.745, 13.65)), ((5.618, 13.24), (6.482, 12.78), (7.318, 12.28)), ((9.182, 11.17), (10.5, 9.6), (12, 8)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e2')
