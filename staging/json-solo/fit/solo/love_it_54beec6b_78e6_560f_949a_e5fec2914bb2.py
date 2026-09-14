"""Love it (social), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54beec6b-78e6-560f-949a-e5fec2914bb2'
SOURCE_PATH = 'icons-json/social/love it_54beec6b-78e6-560f-949a-e5fec2914bb2.json'
AUTHOR = 'json_to_solo'

class LoveItSocial(Solo48):
    icon_id = 'love-it-social'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('love', 'it', 'social')

    def build(self):
        self.add_line('sym-e1', (24, 13), (25, 12))
        self.add_arc('sym-e2', (25, 12), (29, 9), radius_x=10)
        self.add_line('sym-e3', (29, 9), (33, 8))
        self.add_line('sym-e4-1', (33, 8), (38, 9))
        self.add_arc('sym-e4-2', (38, 9), (41, 11), radius_x=10)
        self.add_arc('sym-e4-3', (41, 11), (44, 17), radius_x=8)
        self.add_arc('sym-e5', (44, 17), (44, 18), radius_x=25, sweep=False)
        self.add_arc('sym-e6', (44, 18), (39, 27), radius_x=12)
        self.add_line('sym-e7', (39, 27), (24, 40))
        self.add_line('sym-e8', (24, 40), (9, 27))
        self.add_arc('sym-e9', (9, 27), (4, 18), radius_x=12)
        self.add_line('sym-e10', (4, 18), (4, 17))
        self.add_arc('sym-e11-1', (4, 17), (7, 11), radius_x=8)
        self.add_arc('sym-e11-2', (7, 11), (10, 9), radius_x=10)
        self.add_line('sym-e11-3', (10, 9), (15, 8))
        self.add_line('sym-e12', (15, 8), (19, 9))
        self.add_arc('sym-e13', (19, 9), (23, 12), radius_x=11)
        self.add_arc('sym-e14', (23, 12), (24, 13), radius_x=29)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e4-3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11-1', 'sym-e11-2', 'sym-e11-3', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
