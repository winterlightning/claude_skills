"""Playstation five joy (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98c659a9-5582-453f-ab4e-3cfe3c3fd603'
SOURCE_PATH = 'icons-json/video-games/playstation five joy_98c659a9-5582-453f-ab4e-3cfe3c3fd603.json'
AUTHOR = 'json_to_solo'

class PlaystationFiveJoyVideoGames(Solo48):
    icon_id = 'playstation-five-joy-video-games'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('playstation', 'five', 'joy', 'video-games')

    def build(self):
        self.add_arc('sym-e0', (30, 20), (34, 20), radius_x=2)
        self.add_arc('sym-e1', (34, 20), (30, 20), radius_x=2)
        self.add_arc('sym-e2', (18, 20), (14, 20), radius_x=2, sweep=False)
        self.add_arc('sym-e3', (14, 20), (18, 20), radius_x=2, sweep=False)
        self.add_line('sym-e4', (24, 8), (36, 8))
        self.add_bezier('sym-e5', (36, 8), ((37.936, 8), (39.573, 11.711), (40, 14)))
        self.add_line('sym-e6', (40, 14), (44, 34))
        self.add_bezier('sym-e7', (44, 34), ((44, 34.246), (44, 34.754), (44, 35)))
        self.add_bezier('sym-e8', (44, 35), ((44, 37.338), (41.764, 40), (40, 40)))
        self.add_bezier('sym-e9', (40, 40), ((39.973, 40), (40.036, 40), (40, 40)))
        self.add_bezier('sym-e10', (40, 40), ((39.891, 40), (40.109, 40), (40, 40)))
        self.add_bezier('sym-e11', (40, 40), ((39.364, 40), (38.482, 39.542), (38, 39)))
        self.add_line('sym-e12', (38, 39), (32, 33))
        self.add_bezier('sym-e13', (32, 33), ((31.691, 32.655), (31.309, 31.369), (31, 31)))
        self.add_line('sym-e14', (31, 31), (24, 31))
        self.add_line('sym-e15', (24, 31), (17, 31))
        self.add_bezier('sym-e16', (17, 31), ((16.691, 31.369), (16.309, 32.655), (16, 33)))
        self.add_line('sym-e17', (16, 33), (10, 39))
        self.add_bezier('sym-e18', (10, 39), ((9.518, 39.542), (8.636, 40), (8, 40)))
        self.add_bezier('sym-e19', (8, 40), ((7.891, 40), (8.109, 40), (8, 40)))
        self.add_bezier('sym-e20', (8, 40), ((7.964, 40), (8.027, 40), (8, 40)))
        self.add_bezier('sym-e21', (8, 40), ((6.236, 40), (4, 37.338), (4, 35)))
        self.add_bezier('sym-e22', (4, 35), ((4, 34.754), (4, 34.246), (4, 34)))
        self.add_line('sym-e23', (4, 34), (8, 14))
        self.add_bezier('sym-e24', (8, 14), ((8.427, 11.711), (10.064, 8), (12, 8)))
        self.add_line('sym-e25', (12, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
