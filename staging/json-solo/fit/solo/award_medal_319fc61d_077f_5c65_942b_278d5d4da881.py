"""Award medal (rewards), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '319fc61d-077f-5c65-942b-278d5d4da881'
SOURCE_PATH = 'icons-json/rewards/award medal_319fc61d-077f-5c65-942b-278d5d4da881.json'
AUTHOR = 'json_to_solo'

class AwardMedal319fc61d(Solo48):
    icon_id = 'award-medal-319fc61d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('award', 'medal', 'rewards')

    def build(self):
        self.add_line('e0', (29, 23), (40, 4))
        self.add_line('e1', (40, 4), (32, 4))
        self.add_line('e2', (32, 4), (10, 4))
        self.add_line('e3', (8, 4), (19, 23))
        self.add_arc('e4-top', (12, 33), (36, 33), radius_x=12, radius_y=11)
        self.add_arc('e4-bottom', (36, 33), (12, 33), radius_x=12, radius_y=11)
        self.add_arc('e5', (10, 4), (8, 4), radius_x=12)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e4')
