"""Video cross (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38797d19-9b71-4160-9877-96a19b19a579'
SOURCE_PATH = 'pictographic-primitives/symbol/video cross_38797d19-9b71-4160-9877-96a19b19a579.svg'
AUTHOR = 'gpt-6'

class VideoCross(Solo48):
    icon_id = 'video-cross'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('video', 'cross', 'symbol')

    def build(self):
        self.add_line('sym-e0', (33, 19), (33, 29))
        self.add_line('sym-e1', (33, 29), (42, 34))
        self.add_arc('sym-e2', (42, 34), (44, 33), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e3', (44, 33), (44, 15))
        self.add_arc('sym-e5', (44, 15), (42, 14), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e6', (42, 14), (33, 19))
        self.add_line('sym-e7', (33, 19), (33, 12))
        self.add_arc('sym-e8', (33, 12), (30, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e9', (30, 8), (7, 8))
        self.add_arc('sym-e10', (7, 8), (4, 12), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e11', (4, 12), (4, 36))
        self.add_arc('sym-e13', (4, 36), (7, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e14', (7, 40), (30, 40))
        self.add_arc('sym-e15', (30, 40), (33, 36), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e16', (33, 36), (33, 29))
        self.add_line('sym-e17', (19, 17), (19, 31))
        self.add_line('sym-e18', (13, 24), (24, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=False)
        self.add_contour('sym-c1', 'sym-e17', closed=False)
        self.add_contour('sym-c2', 'sym-e18', closed=False)
