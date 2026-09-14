"""Onigiri japanese riceball (food), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02bc5d40-f3c4-5eb5-84b8-5660c7e3cdd7'
SOURCE_PATH = 'icons-json/food/onigiri japanese riceball_02bc5d40-f3c4-5eb5-84b8-5660c7e3cdd7.json'
AUTHOR = 'json_to_solo'

class OnigiriJapaneseRiceballFood(Solo48):
    icon_id = 'onigiri-japanese-riceball-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('onigiri', 'japanese', 'riceball', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 25), (19, 25))
        self.add_bezier('sym-e1', (19, 25), ((16.491, 25), (16, 26.996), (16, 29)))
        self.add_line('sym-e2', (16, 29), (16, 40))
        self.add_line('sym-e3', (16, 40), (10, 40))
        self.add_bezier('sym-e4', (10, 40), ((9.564, 40), (9.409, 40), (9, 40)))
        self.add_bezier('sym-e5', (9, 40), ((6.255, 39.301), (4, 36.745), (4, 34)))
        self.add_bezier('sym-e6', (4, 34), ((4, 33.882), (4.009, 34.118), (4, 34)))
        self.add_bezier('sym-e7', (4, 34), ((4, 32.021), (5.936, 28.726), (7, 27)))
        self.add_bezier('sym-e8', (7, 27), ((9.945, 22.225), (13.445, 17.404), (17, 13)))
        self.add_bezier('sym-e9', (17, 13), ((18.655, 10.945), (20.873, 8), (24, 8)))
        self.add_bezier('sym-e10', (24, 8), ((24.124, 8), (23.874, 8), (24, 8)))
        self.add_bezier('sym-e11', (24, 8), ((24.126, 8), (23.876, 8), (24, 8)))
        self.add_bezier('sym-e12', (24, 8), ((27.127, 8), (29.345, 10.945), (31, 13)))
        self.add_bezier('sym-e13', (31, 13), ((34.555, 17.404), (38.055, 22.225), (41, 27)))
        self.add_bezier('sym-e14', (41, 27), ((42.064, 28.726), (44, 32.021), (44, 34)))
        self.add_bezier('sym-e15', (44, 34), ((43.991, 34.118), (44, 33.882), (44, 34)))
        self.add_bezier('sym-e16', (44, 34), ((44, 36.745), (41.745, 39.301), (39, 40)))
        self.add_bezier('sym-e17', (39, 40), ((38.591, 40), (38.436, 40), (38, 40)))
        self.add_line('sym-e18', (38, 40), (32, 40))
        self.add_line('sym-e19', (32, 40), (32, 29))
        self.add_bezier('sym-e20', (32, 29), ((32, 26.996), (31.509, 25), (29, 25)))
        self.add_line('sym-e21', (29, 25), (24, 25))
        self.add_line('sym-e22', (16, 40), (24, 40))
        self.add_line('sym-e23', (24, 40), (32, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
