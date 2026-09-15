"""Love lollipop (romance), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '911ef131-2509-56e7-8de2-02eb51318d04'
SOURCE_PATH = 'icons-json/romance/love lollipop_911ef131-2509-56e7-8de2-02eb51318d04.json'
AUTHOR = 'gpt-6'

class LoveLollipop(Solo48):
    icon_id = 'love-lollipop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('love', 'lollipop', 'romance')

    def build(self):
        self.add_line('sym-e0', (24, 27), (24, 44))
        self.add_line('sym-e2', (24, 8), (25, 7))
        self.add_arc('sym-e3', (25, 7), (26, 6), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('sym-e4', (26, 6), (31, 4), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e6', (31, 4), (32, 4))
        self.add_arc('sym-e7', (32, 4), (40, 10), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (40, 10), (40, 11), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e9', (40, 11), (40, 12), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (40, 12), (36, 18), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('sym-e11', (36, 18), (24, 27))
        self.add_line('sym-e12', (24, 27), (12, 18))
        self.add_arc('sym-e13', (12, 18), (8, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e14', (8, 12), (8, 10))
        self.add_arc('sym-e16', (8, 10), (16, 4), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e17', (16, 4), (17, 4), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_arc('sym-e19', (17, 4), (22, 6), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e20', (22, 6), (23, 7), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('sym-e21', (23, 7), (24, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
