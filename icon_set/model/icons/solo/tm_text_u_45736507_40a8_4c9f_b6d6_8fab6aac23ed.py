"""Tm (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45736507-40a8-4c9f-b6d6-8fab6aac23ed'
SOURCE_PATH = 'icons-json/symbol/tm (text u)_45736507-40a8-4c9f-b6d6-8fab6aac23ed.json'
AUTHOR = 'json_to_solo'

class TmTextU(Solo48):
    icon_id = 'tm-text-u'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('tm', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (19, 8))
        self.add_line('e1', (11, 26), (11, 8))
        self.add_line('e2', (26, 15), (26, 26))
        self.add_line('e3', (35, 18), (35, 26))
        self.add_line('e4', (44, 18), (44, 26))
        self.add_line('e5', (4, 40), (44, 40))
        self.add_arc('e6', (26, 17), (35, 18), radius_x=5)
        self.add_arc('e7', (35, 17), (44, 18), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e6', 'e3')
        self.add_contour('c4', 'e7', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c3')
