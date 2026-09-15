"""Show theater (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79dcd02e-0d11-480b-83e8-28d614866f51'
SOURCE_PATH = 'pictographic-primitives/entertainment/show theater_79dcd02e-0d11-480b-83e8-28d614866f51.svg'
AUTHOR = 'gpt-6'

class ShowTheater(Solo48):
    icon_id = 'show-theater'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('show', 'theater', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (4, 16), (44, 16))
        self.add_line('sym-e4', (44, 16), (44, 39))
        self.add_line('sym-e7', (44, 39), (41, 40))
        self.add_arc('sym-e8', (41, 40), (40, 40), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_line('sym-e9', (40, 40), (39, 40))
        self.add_arc('sym-e10', (39, 40), (38, 40), radius_x=39, radius_y=39, large_arc=False, sweep=False)
        self.add_arc('sym-e12', (38, 40), (36, 40), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_line('sym-e14', (36, 40), (32, 39))
        self.add_line('sym-e15', (32, 39), (32, 25))
        self.add_arc('sym-e17', (32, 25), (25, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e18', (16, 25), (16, 38))
        self.add_arc('sym-e19', (16, 38), (16, 39), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e20', (16, 39), (12, 40))
        self.add_line('sym-e22', (12, 40), (8, 40))
        self.add_arc('sym-e26', (8, 40), (7, 40), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e27', (7, 40), (4, 39))
        self.add_line('sym-e28', (4, 39), (4, 8))
        self.add_arc('sym-e33', (4, 8), (5, 8), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e34', (5, 8), (43, 8))
        self.add_arc('sym-e36', (43, 8), (44, 8), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e37', (44, 8), (44, 9), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e38', (44, 9), (44, 16))
        self.add_arc('sym-e39', (23, 16), (16, 25), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('sym-e40', (16, 25), (8, 26), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_line('sym-e41', (8, 26), (4, 26))
        self.add_line('sym-e44', (32, 25), (40, 26))
        self.add_line('sym-e45', (40, 26), (44, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', closed=False)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e33', 'sym-e34', 'sym-e36', 'sym-e37', 'sym-e38', closed=False)
        self.add_contour('sym-c2', 'sym-e39', 'sym-e40', 'sym-e41', closed=False)
        self.add_contour('sym-c3', 'sym-e44', 'sym-e45', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
