"""Car 2 (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa4ae914-3af0-476a-9426-f0036782e934'
SOURCE_PATH = 'icons-json/transportation/car 2_aa4ae914-3af0-476a-9426-f0036782e934.json'
AUTHOR = 'json_to_solo'

class Car2Transportation(Solo48):
    icon_id = 'car-2-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (9, 34), (6, 34))
        self.add_line('e2', (4, 31), (4, 23))
        self.add_line('e3', (6, 19), (20, 19))
        self.add_line('e4', (6, 19), (12, 9))
        self.add_line('e5', (30, 34), (18, 34))
        self.add_line('e6', (20, 19), (36, 19))
        self.add_line('e7', (36, 19), (29, 9))
        self.add_line('e8', (26, 8), (20, 8))
        self.add_line('e9', (20, 19), (20, 8))
        self.add_arc('e10-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_bezier('e12', (42, 34), ((44, 32.597), (43.955, 30.4), (43.982, 27.52)), ((43.982, 27.323), (44, 27.138), (44, 26.942)), ((44, 26.938), (44, 26.933), (44, 26.929)), ((44, 26.675), (43.982, 26.421), (43.982, 26.166)), ((43.982, 24.96), (43.609, 23.668), (43.127, 22.683)), ((41.436, 19.249), (38.736, 19.037), (36, 19)))
        self.add_bezier('e13', (6, 34), ((4.773, 33.237), (4.527, 32.674), (4, 31)))
        self.add_bezier('e14', (4, 23), ((4.209, 22.052), (4.382, 20.677), (4.991, 19.975)), ((5.264, 19.68), (5.727, 19.295), (6, 19)))
        self.add_bezier('e15', (12, 9), ((13.527, 8), (15.191, 8.025), (16.918, 8.025)), ((17.036, 8.025), (17.155, 8.025), (17.273, 8.025)), ((17.391, 8.025), (17.509, 8.025), (17.627, 8.025)), ((17.809, 8.025), (17.982, 8.012), (18.155, 8.012)), ((18.273, 8.025), (18.382, 8.025), (18.491, 8.025)), ((18.818, 8.025), (19.136, 8), (19.464, 8)), ((19.764, 8), (19.7, 8), (20, 8)))
        self.add_bezier('e16', (29, 9), ((28.155, 8.36), (27, 8), (26, 8)))
        self.add_contour('c0', 'e0', 'e12')
        self.add_contour('c1', 'e1', 'e13', 'e2', 'e14')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e15')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e7', 'e16', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c1', 'e11')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c4', 'e11')
