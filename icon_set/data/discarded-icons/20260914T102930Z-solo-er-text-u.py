"""Er (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f86898a-096d-483f-89f4-6d8b09032624'
SOURCE_PATH = 'icons-json/symbol/er (text u)_4f86898a-096d-483f-89f4-6d8b09032624.json'
AUTHOR = 'json_to_solo'

class ErTextU(Solo48):
    icon_id = 'er-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('er', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (22, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 26))
        self.add_line('e2', (9, 27), (22, 27))
        self.add_line('e3', (19, 15), (8, 15))
        self.add_line('e4', (31, 13), (31, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_arc('e6', (9, 4), (8, 5), radius_x=1, sweep=False)
        self.add_line('e7', (8, 26), (9, 27))
        self.add_arc('e8', (40, 13), (31, 17), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
