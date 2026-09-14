"""Onigiri japanese riceball (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02bc5d40-f3c4-5eb5-84b8-5660c7e3cdd7'
SOURCE_PATH = 'icons-json/food/onigiri japanese riceball_02bc5d40-f3c4-5eb5-84b8-5660c7e3cdd7.json'
AUTHOR = 'json_to_solo'

class OnigiriJapaneseRiceball(Solo48):
    icon_id = 'onigiri-japanese-riceball'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('onigiri', 'japanese', 'riceball', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 25), (19, 25))
        self.add_arc('sym-e1', (19, 25), (16, 29), radius_x=3, sweep=False)
        self.add_line('sym-e2', (16, 29), (16, 40))
        self.add_line('sym-e3', (16, 40), (10, 40))
        self.add_line('sym-e4', (10, 40), (9, 40))
        self.add_arc('sym-e5', (9, 40), (4, 34), radius_x=7)
        self.add_arc('sym-e7', (4, 34), (7, 27), radius_x=17)
        self.add_line('sym-e8', (7, 27), (17, 13))
        self.add_arc('sym-e9', (17, 13), (24, 8), radius_x=9)
        self.add_arc('sym-e12', (24, 8), (31, 13), radius_x=9)
        self.add_line('sym-e13', (31, 13), (41, 27))
        self.add_arc('sym-e14', (41, 27), (44, 34), radius_x=17)
        self.add_arc('sym-e16', (44, 34), (39, 40), radius_x=7)
        self.add_line('sym-e17', (39, 40), (38, 40))
        self.add_line('sym-e18', (38, 40), (32, 40))
        self.add_line('sym-e19', (32, 40), (32, 29))
        self.add_arc('sym-e20', (32, 29), (29, 25), radius_x=3, sweep=False)
        self.add_line('sym-e21', (29, 25), (24, 25))
        self.add_line('sym-e22', (16, 40), (24, 40))
        self.add_line('sym-e23', (24, 40), (32, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
