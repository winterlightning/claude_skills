"""Hierarchy (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03c563a0-7c54-57e4-a8ff-454322ef2c14'
SOURCE_PATH = 'icons-json/programing/hierarchy_03c563a0-7c54-57e4-a8ff-454322ef2c14.json'
AUTHOR = 'json_to_solo'

class Hierarchy03c563a0(Solo48):
    icon_id = 'hierarchy-03c563a0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self):
        self.add_line('e0', (10, 30), (7, 30))
        self.add_line('e1', (6, 40), (14, 40))
        self.add_line('e2', (17, 37), (17, 32))
        self.add_line('e3', (10, 30), (11, 24))
        self.add_line('e4', (11, 24), (38, 24))
        self.add_line('e5', (38, 24), (38, 30))
        self.add_line('e6', (24, 24), (24, 17))
        self.add_line('e7', (24, 17), (29, 17))
        self.add_line('e8', (29, 8), (19, 8))
        self.add_line('e9', (17, 11), (17, 15))
        self.add_line('e10', (19, 17), (24, 17))
        self.add_line('e11', (31, 33), (31, 37))
        self.add_line('e12', (34, 40), (41, 40))
        self.add_line('e13', (44, 37), (44, 32))
        self.add_line('e14', (41, 30), (37, 30))
        self.add_bezier('e15', (7, 30), ((4.736, 30), (4.018, 31.773), (4.018, 33.457)), ((4.018, 33.929), (4, 34.402), (4, 34.874)), ((4, 34.882), (4, 34.889), (4, 34.897)), ((4, 35.427), (4.018, 35.966), (4.018, 36.497)), ((4.018, 37.794), (4.027, 38.939), (5.255, 39.781)), ((5.427, 39.907), (5.818, 39.899), (6, 40)))
        self.add_bezier('e16', (14, 40), ((14.191, 40), (14.391, 39.992), (14.582, 39.992)), ((14.764, 39.992), (14.936, 39.992), (15.118, 39.992)), ((15.173, 39.992), (15.227, 39.983), (15.282, 39.983)), ((16.509, 39.983), (17, 37.775), (17, 37)))
        self.add_bezier('e17', (17, 32), ((16.882, 31.722), (16.582, 31.023), (16.382, 30.771)), ((15.264, 29.423), (11.545, 30.017), (10, 30)))
        self.add_bezier('e18', (29, 17), ((31.918, 17), (32.1, 14.863), (32.091, 12.909)), ((32.073, 10.535), (32.618, 8.008), (29.136, 8.008)), ((28.936, 8.008), (29.2, 8), (29, 8)))
        self.add_bezier('e19', (19, 8), ((18.855, 8.008), (19.164, 8.008), (19.018, 8.017)), ((17.591, 8.017), (17, 9.846), (17, 11)))
        self.add_bezier('e20', (17, 15), ((17, 16.726), (17.1, 17), (19, 17)))
        self.add_bezier('e21', (37, 30), ((34.118, 30), (31, 29.573), (31, 33)))
        self.add_bezier('e22', (31, 37), ((31, 38.617), (32.227, 40), (34, 40)))
        self.add_bezier('e23', (41, 40), ((41.082, 40), (41.427, 39.992), (41.509, 39.992)), ((43.318, 39.992), (43.991, 38.72), (43.991, 37.255)), ((43.991, 37.162), (44, 37.061), (44, 36.96)), ((44, 36.851), (44, 37.109), (44, 37)))
        self.add_bezier('e24', (44, 32), ((44, 31.865), (43.991, 32.152), (43.991, 32.008)), ((43.991, 30.602), (42.3, 30), (41, 30)))
        self.add_contour('c0', 'e0', 'e15', 'e1', 'e16', 'e2', 'e17', 'e3', 'e4', 'e5')
        self.add_contour('c1', 'e6', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10')
        self.add_contour('c2', 'e21', 'e11', 'e22', 'e12', 'e23', 'e13', 'e24', 'e14', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
