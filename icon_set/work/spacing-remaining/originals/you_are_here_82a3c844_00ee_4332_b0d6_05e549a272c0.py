"""You are here (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a3c844-00ee-4332-b0d6-05e549a272c0'
SOURCE_PATH = 'icons-json/maps/you are here_82a3c844-00ee-4332-b0d6-05e549a272c0.json'
AUTHOR = 'json_to_solo'

class YouAreHere(Solo48):
    icon_id = 'you-are-here'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('you', 'are', 'here', 'maps')

    def build(self):
        self.add_arc('sym-e0', (18, 18), (30, 18), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 18), (18, 18), radius_x=6, radius_y=5)
        self.add_arc('sym-e2-1', (8, 41), (13, 43), radius_x=21, sweep=False)
        self.add_line('sym-e2-2', (13, 43), (23, 44))
        self.add_line('sym-e4', (23, 44), (24, 44))
        self.add_arc('sym-e5', (24, 44), (25, 44), radius_x=29)
        self.add_line('sym-e7-1', (25, 44), (35, 43))
        self.add_arc('sym-e7-2', (35, 43), (40, 41), radius_x=21, sweep=False)
        self.add_line('sym-e8', (23, 38), (14, 29))
        self.add_arc('sym-e9', (14, 29), (8, 18), radius_x=17)
        self.add_line('sym-e10', (8, 18), (8, 17))
        self.add_arc('sym-e12-1', (8, 17), (9, 13), radius_x=9)
        self.add_arc('sym-e12-2', (9, 13), (11, 9), radius_x=12)
        self.add_arc('sym-e12-3', (11, 9), (23, 4), radius_x=17)
        self.add_arc('sym-e14', (23, 4), (24, 4), radius_x=71, sweep=False)
        self.add_line('sym-e15', (24, 4), (25, 4))
        self.add_arc('sym-e17-1', (25, 4), (37, 9), radius_x=17)
        self.add_arc('sym-e17-2', (37, 9), (39, 13), radius_x=12)
        self.add_arc('sym-e17-3', (39, 13), (40, 17), radius_x=9)
        self.add_line('sym-e19', (40, 17), (40, 18))
        self.add_arc('sym-e20', (40, 18), (34, 29), radius_x=17)
        self.add_line('sym-e21', (34, 29), (25, 38))
        self.add_line('sym-e22', (25, 38), (24, 39))
        self.add_line('sym-e23', (24, 39), (23, 38))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2-1', 'sym-e2-2', 'sym-e4', 'sym-e5', 'sym-e7-1', 'sym-e7-2')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12-1', 'sym-e12-2', 'sym-e12-3', 'sym-e14', 'sym-e15', 'sym-e17-1', 'sym-e17-2', 'sym-e17-3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
