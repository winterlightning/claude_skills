"""Sign badge badge (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51affb95-85ee-5312-8a83-f077a030e9a9'
SOURCE_PATH = 'icons-json/maps/sign badge badge_51affb95-85ee-5312-8a83-f077a030e9a9.json'
AUTHOR = 'json_to_solo'

class SignBadgeBadge51affb95(Solo48):
    icon_id = 'sign-badge-badge-51affb95'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'maps')

    def build(self):
        self.add_line('sym-e0', (8, 23), (8, 7))
        self.add_line('sym-e1', (8, 7), (11, 9))
        self.add_arc('sym-e2', (11, 9), (15, 9), radius_x=3, sweep=False)
        self.add_line('sym-e3', (15, 9), (24, 4))
        self.add_line('sym-e4', (24, 4), (33, 9))
        self.add_arc('sym-e5', (33, 9), (37, 9), radius_x=3, sweep=False)
        self.add_line('sym-e6', (37, 9), (40, 7))
        self.add_line('sym-e7', (40, 7), (40, 23))
        self.add_line('sym-e8', (40, 23), (40, 24))
        self.add_arc('sym-e9', (40, 24), (29, 40), radius_x=25)
        self.add_arc('sym-e10', (29, 40), (24, 44), radius_x=17)
        self.add_arc('sym-e13', (24, 44), (19, 40), radius_x=18)
        self.add_arc('sym-e14', (19, 40), (8, 24), radius_x=25)
        self.add_line('sym-e15', (8, 24), (8, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
