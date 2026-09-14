"""1p (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7111ee31-431e-46d9-8af7-0ae69eeb1699'
SOURCE_PATH = 'icons-json/text/1P (text)_7111ee31-431e-46d9-8af7-0ae69eeb1699.json'
AUTHOR = 'json_to_solo'

class Icon1pTextText(Solo48):
    icon_id = 'icon-1p-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('1p', 'text')

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (25, 25), (36, 25))
        self.add_line('e2', (36, 8), (25, 8))
        self.add_line('e3', (25, 8), (25, 40))
        self.add_arc('e4', (4, 14), (12, 8), radius_x=21, sweep=False)
        self.add_arc('e5-1', (36, 25), (44, 17), radius_x=9, sweep=False)
        self.add_line('e5-2', (44, 17), (42, 11))
        self.add_arc('e5-3', (42, 11), (36, 8), radius_x=9, sweep=False)
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e3')
