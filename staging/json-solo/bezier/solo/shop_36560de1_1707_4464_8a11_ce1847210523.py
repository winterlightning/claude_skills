"""Shop (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'icons-json/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.json'
AUTHOR = 'json_to_solo'

class Shop36560de1(Solo48):
    icon_id = 'shop-36560de1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')

    def build(self):
        self.add_line('sym-e0', (24, 40), (41, 40))
        self.add_line('sym-e1', (41, 40), (41, 22))
        self.add_bezier('sym-e2', (41, 22), ((39.109, 22.859), (37.6, 23.272), (36, 22)))
        self.add_bezier('sym-e3', (36, 22), ((35.473, 21.579), (34.064, 19.992), (34, 20)))
        self.add_bezier('sym-e4', (34, 20), ((33.955, 20), (32.5, 21.722), (32, 22)))
        self.add_bezier('sym-e5', (32, 22), ((30.127, 23.019), (27.709, 23.314), (26, 22)))
        self.add_bezier('sym-e6', (26, 22), ((25.373, 21.52), (24.518, 20.581), (24, 20)))
        self.add_bezier('sym-e7', (24, 20), ((23.482, 20.581), (22.627, 21.52), (22, 22)))
        self.add_bezier('sym-e8', (22, 22), ((20.291, 23.314), (17.873, 23.019), (16, 22)))
        self.add_bezier('sym-e9', (16, 22), ((15.5, 21.722), (14.045, 20), (14, 20)))
        self.add_bezier('sym-e10', (14, 20), ((13.936, 19.992), (12.527, 21.579), (12, 22)))
        self.add_bezier('sym-e11', (12, 22), ((10.4, 23.272), (8.891, 22.859), (7, 22)))
        self.add_line('sym-e12', (7, 22), (7, 40))
        self.add_line('sym-e13', (7, 40), (24, 40))
        self.add_bezier('sym-e14', (41, 22), ((42.464, 21.335), (44, 19.516), (44, 18)))
        self.add_bezier('sym-e15', (44, 18), ((44, 17.933), (44, 18.067), (44, 18)))
        self.add_bezier('sym-e16', (44, 18), ((44, 17.874), (44, 18.135), (44, 18)))
        self.add_bezier('sym-e17', (44, 18), ((44, 17.082), (43.245, 15.901), (43, 15)))
        self.add_line('sym-e18', (43, 15), (41, 8))
        self.add_line('sym-e19', (41, 8), (24, 8))
        self.add_line('sym-e20', (24, 8), (7, 8))
        self.add_line('sym-e21', (7, 8), (5, 15))
        self.add_bezier('sym-e22', (5, 15), ((4.755, 15.901), (4, 17.082), (4, 18)))
        self.add_bezier('sym-e23', (4, 18), ((4, 18.135), (4, 17.874), (4, 18)))
        self.add_bezier('sym-e24', (4, 18), ((4, 18.067), (4, 17.933), (4, 18)))
        self.add_bezier('sym-e25', (4, 18), ((4, 19.516), (5.536, 21.335), (7, 22)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
