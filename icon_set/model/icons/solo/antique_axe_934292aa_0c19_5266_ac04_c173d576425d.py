"""Antique axe (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '934292aa-0c19-5266-ac04-c173d576425d'
SOURCE_PATH = 'icons-json/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.json'
AUTHOR = 'json_to_solo'

class AntiqueAxe(Solo48):
    icon_id = 'antique-axe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('antique', 'axe', 'war')

    def build(self):
        self.add_line('e0', (29, 22), (23, 15))
        self.add_line('e1', (23, 15), (29, 8))
        self.add_line('e2', (29, 8), (34, 14))
        self.add_line('e3', (34, 8), (31, 10))
        self.add_line('e4', (44, 19), (42, 22))
        self.add_line('e5', (4, 40), (25, 17))
        self.add_arc('e6', (33, 31), (29, 22), radius_x=17, sweep=False)
        self.add_arc('e7', (34, 14), (44, 18), radius_x=15, sweep=False)
        self.add_arc('e8', (42, 22), (33, 31), radius_x=15)
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e2', 'e7')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e8')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c0')
