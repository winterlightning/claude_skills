"""Underwear bra (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c22cd393-1a0c-5c5b-8aba-474ac250aa1f'
SOURCE_PATH = 'icons-json/clothes/underwear bra_c22cd393-1a0c-5c5b-8aba-474ac250aa1f.json'
AUTHOR = 'json_to_solo'

class UnderwearBraC22cd393(Solo48):
    icon_id = 'underwear-bra-c22cd393'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bra', 'clothes')

    def build(self):
        self.add_line('e0', (7, 21), (7, 8))
        self.add_line('e1', (41, 20), (41, 8))
        self.add_line('e2', (26, 35), (22, 35))
        self.add_line('e3', (26, 35), (27, 30))
        self.add_line('e4', (36, 23), (42, 21))
        self.add_arc('e5-1', (22, 35), (14, 40), radius_x=11)
        self.add_arc('e5-2', (14, 40), (4, 30), radius_x=10)
        self.add_arc('e5-3', (4, 30), (7, 21), radius_x=22)
        self.add_arc('e6-1', (26, 35), (34, 40), radius_x=9, sweep=False)
        self.add_arc('e6-2', (34, 40), (42, 36), radius_x=10, sweep=False)
        self.add_line('e6-3', (42, 36), (44, 29))
        self.add_arc('e6-4', (44, 29), (41, 20), radius_x=15, sweep=False)
        self.add_arc('e7', (27, 30), (36, 23), radius_x=13)
        self.add_arc('e8', (7, 21), (22, 35), radius_x=16)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e0')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c0')
