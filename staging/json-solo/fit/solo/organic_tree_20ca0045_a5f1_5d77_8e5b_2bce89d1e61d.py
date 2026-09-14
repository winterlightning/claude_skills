"""Organic tree (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20ca0045-a5f1-5d77-8e5b-2bce89d1e61d'
SOURCE_PATH = 'icons-json/ecology/organic tree_20ca0045-a5f1-5d77-8e5b-2bce89d1e61d.json'
AUTHOR = 'json_to_solo'

class OrganicTree20ca0045(Solo48):
    icon_id = 'organic-tree-20ca0045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('organic', 'tree', 'ecology')

    def build(self):
        self.add_line('e0', (24, 19), (24, 44))
        self.add_line('e1', (19, 44), (29, 44))
        self.add_line('e2', (24, 33), (19, 33))
        self.add_arc('e3-1', (19, 33), (8, 23), radius_x=11)
        self.add_arc('e3-2', (8, 23), (13, 14), radius_x=11)
        self.add_arc('e3-3', (13, 14), (15, 8), radius_x=8)
        self.add_arc('e3-4', (15, 8), (19, 5), radius_x=11)
        self.add_line('e3-5', (19, 5), (24, 4))
        self.add_line('e3-6', (24, 4), (29, 5))
        self.add_arc('e3-7', (29, 5), (32, 7), radius_x=11)
        self.add_arc('e3-8', (32, 7), (35, 15), radius_x=9)
        self.add_arc('e3-9', (35, 15), (39, 19), radius_x=12)
        self.add_arc('e3-10', (39, 19), (40, 23), radius_x=9)
        self.add_arc('e3-11', (40, 23), (35, 31), radius_x=9)
        self.add_arc('e3-12', (35, 31), (24, 33), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
