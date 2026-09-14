"""Award medal (rewards), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a05303d-ae76-55f0-9b37-fe4f3470f89b'
SOURCE_PATH = 'icons-json/rewards/award medal_2a05303d-ae76-55f0-9b37-fe4f3470f89b.json'
AUTHOR = 'json_to_solo'

class AwardMedal2a05303d(Solo48):
    icon_id = 'award-medal-2a05303d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('award', 'medal', 'rewards')

    def build(self):
        self.add_line('e0', (19, 22), (8, 4))
        self.add_line('e1', (8, 4), (40, 4))
        self.add_line('e2', (40, 4), (29, 22))
        self.add_line('e3', (34, 13), (14, 13))
        self.add_arc('e4-1', (29, 22), (37, 33), radius_x=12)
        self.add_arc('e4-2', (37, 33), (34, 40), radius_x=11)
        self.add_arc('e4-3', (34, 40), (29, 43), radius_x=12)
        self.add_arc('e4-4', (29, 43), (24, 44), radius_x=14)
        self.add_arc('e4-5', (24, 44), (12, 36), radius_x=13)
        self.add_arc('e4-6', (12, 36), (19, 22), radius_x=12)
        self.add_arc('e5', (29, 22), (19, 22), radius_x=22, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
