"""Fr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c234d5a-675f-46f8-98db-4cf6d3b23336'
SOURCE_PATH = 'icons-json/symbol/fr (text u)_1c234d5a-675f-46f8-98db-4cf6d3b23336.json'
AUTHOR = 'json_to_solo'

class FrTextU(Solo48):
    icon_id = 'fr-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fr', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 13), (19, 13))
        self.add_line('e1', (8, 27), (8, 5))
        self.add_line('e2', (9, 4), (21, 4))
        self.add_line('e3', (31, 13), (31, 27))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5', (8, 5), (9, 4), radius_x=1)
        self.add_arc('e6', (40, 13), (31, 17), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c2')
