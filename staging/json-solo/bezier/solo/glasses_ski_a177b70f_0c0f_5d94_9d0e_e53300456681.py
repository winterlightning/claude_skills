"""Batch-01/glasses ski (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a177b70f-0c0f-5d94-9d0e-e53300456681'
SOURCE_PATH = 'icons-json/accessories/batch-01/glasses ski_a177b70f-0c0f-5d94-9d0e-e53300456681.json'
AUTHOR = 'json_to_solo'

class Batch01GlassesSki(Solo48):
    icon_id = 'batch-01-glasses-ski'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'glasses', 'ski', 'accessories')

    def build(self):
        self.add_line('sym-e0', (24, 21), (4, 21))
        self.add_bezier('sym-e1', (4, 21), ((4, 20.952), (4, 21.048), (4, 21)))
        self.add_bezier('sym-e2', (4, 21), ((4, 20.291), (4, 19.713), (4, 19)))
        self.add_bezier('sym-e3', (4, 19), ((4, 18.619), (4.003, 17.384), (4, 17)))
        self.add_bezier('sym-e4', (4, 17), ((4, 16.408), (4, 15.56), (4, 15)))
        self.add_bezier('sym-e5', (4, 15), ((5.118, 9.304), (10.091, 8.528), (13, 8)))
        self.add_bezier('sym-e6', (13, 8), ((13.509, 8), (13.491, 8), (14, 8)))
        self.add_bezier('sym-e7', (14, 8), ((14.2, 8), (14.8, 8), (15, 8)))
        self.add_line('sym-e8', (15, 8), (24, 8))
        self.add_line('sym-e9', (24, 8), (33, 8))
        self.add_bezier('sym-e10', (33, 8), ((33.2, 8), (33.8, 8), (34, 8)))
        self.add_bezier('sym-e11', (34, 8), ((34.509, 8), (34.491, 8), (35, 8)))
        self.add_bezier('sym-e12', (35, 8), ((37.909, 8.528), (42.882, 9.304), (44, 15)))
        self.add_bezier('sym-e13', (44, 15), ((44, 15.56), (44, 16.408), (44, 17)))
        self.add_bezier('sym-e14', (44, 17), ((43.997, 17.384), (44, 18.619), (44, 19)))
        self.add_bezier('sym-e15', (44, 19), ((44, 19.713), (44, 20.291), (44, 21)))
        self.add_bezier('sym-e16', (44, 21), ((44, 21), (44, 21), (44, 21)))
        self.add_bezier('sym-e17', (44, 21), ((44, 21.048), (44, 20.952), (44, 21)))
        self.add_line('sym-e18', (44, 21), (24, 21))
        self.add_bezier('sym-e19', (5, 29), ((5.7, 35.176), (6.518, 37.384), (10, 39)))
        self.add_bezier('sym-e20', (10, 39), ((11.027, 39.464), (11.927, 40), (13, 40)))
        self.add_bezier('sym-e21', (13, 40), ((13.064, 40), (13.927, 39.984), (14, 40)))
        self.add_bezier('sym-e22', (14, 40), ((14.091, 40), (13.918, 40), (14, 40)))
        self.add_bezier('sym-e23', (14, 40), ((15.418, 40), (18.273, 39.56), (19, 37)))
        self.add_line('sym-e24', (19, 37), (20, 30))
        self.add_bezier('sym-e25', (20, 30), ((20.626, 27.796), (22.512, 27), (24, 27)))
        self.add_bezier('sym-e26', (24, 27), ((25.488, 27), (27.374, 27.796), (28, 30)))
        self.add_line('sym-e27', (28, 30), (29, 37))
        self.add_bezier('sym-e28', (29, 37), ((29.727, 39.56), (32.582, 40), (34, 40)))
        self.add_bezier('sym-e29', (34, 40), ((34.082, 40), (33.909, 40), (34, 40)))
        self.add_bezier('sym-e30', (34, 40), ((34.073, 39.984), (34.936, 40), (35, 40)))
        self.add_bezier('sym-e31', (35, 40), ((36.073, 40), (36.973, 39.464), (38, 39)))
        self.add_bezier('sym-e32', (38, 39), ((41.482, 37.384), (42.3, 35.176), (43, 29)))
        self.add_line('sym-e33', (43, 29), (44, 21))
        self.add_bezier('sym-e34', (44, 21), ((44, 21.1), (44, 21), (44, 21)))
        self.add_bezier('sym-e35', (44, 21), ((44, 21), (44, 21.069), (44, 21)))
        self.add_bezier('sym-e36', (44, 21), ((44, 20.928), (44, 21), (44, 21)))
        self.add_bezier('sym-e37', (44, 21), ((44, 21), (44, 20.894), (44, 21)))
        self.add_bezier('sym-e38', (4, 21), ((4, 21), (4, 21), (4, 21)))
        self.add_bezier('sym-e39', (4, 21), ((4, 21), (4, 20.928), (4, 21)))
        self.add_bezier('sym-e40', (4, 21), ((4, 21.1), (4, 21), (4, 21)))
        self.add_bezier('sym-e41', (4, 21), ((4, 21), (4, 21.069), (4, 21)))
        self.add_bezier('sym-e42', (4, 21), ((4, 20.894), (4, 21), (4, 21)))
        self.add_line('sym-e43', (4, 21), (5, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37')
        self.add_contour('sym-c2', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41', 'sym-e42', closed=True)
        self.add_contour('sym-c3', 'sym-e43')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
