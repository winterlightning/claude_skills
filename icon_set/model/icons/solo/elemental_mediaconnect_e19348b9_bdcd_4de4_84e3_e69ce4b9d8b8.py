"""Elemental mediaconnect (apps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8'
SOURCE_PATH = 'icons-json/apps/elemental mediaconnect_e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8.json'
AUTHOR = 'json_to_solo'

class ElementalMediaconnect(Solo48):
    icon_id = 'elemental-mediaconnect'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('elemental', 'mediaconnect', 'apps')

    def build(self):
        self.add_line('e0', (12, 37), (8, 34))
        self.add_line('e1', (8, 34), (8, 15))
        self.add_line('e2', (9, 14), (24, 4))
        self.add_line('e3', (24, 4), (28, 7))
        self.add_line('e4', (36, 11), (40, 14))
        self.add_line('e5', (40, 14), (40, 34))
        self.add_line('e6', (40, 35), (24, 44))
        self.add_line('e7', (24, 44), (20, 41))
        self.add_line('e8', (24, 35), (24, 24))
        self.add_line('e9', (24, 35), (15, 29))
        self.add_line('e10', (15, 29), (15, 19))
        self.add_line('e11', (24, 35), (33, 29))
        self.add_line('e12', (33, 29), (33, 19))
        self.add_line('e13', (15, 19), (24, 24))
        self.add_line('e14', (15, 19), (24, 13))
        self.add_line('e15', (24, 13), (33, 19))
        self.add_line('e16', (24, 24), (33, 19))
        self.add_arc('e17', (8, 15), (9, 14), radius_x=1)
        self.add_arc('e18', (40, 34), (40, 35), radius_x=34, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e17', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e18', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e9', 'e10')
        self.add_contour('c4', 'e11', 'e12')
        self.add_contour('c5', 'e13')
        self.add_contour('c6', 'e14', 'e15')
        self.add_contour('c7', 'e16')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
