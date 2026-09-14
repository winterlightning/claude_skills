"""Social profile avatar (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '250b8419-48bd-502c-b2f3-1e27915a95fd'
SOURCE_PATH = 'icons-json/social/social profile avatar_250b8419-48bd-502c-b2f3-1e27915a95fd.json'
AUTHOR = 'json_to_solo'

class SocialProfileAvatarSocial(Solo48):
    icon_id = 'social-profile-avatar-social'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('social', 'profile', 'avatar')

    def build(self):
        self.add_line('e0', (14, 44), (14, 36))
        self.add_line('e1', (35, 14), (40, 28))
        self.add_line('e2', (40, 28), (35, 28))
        self.add_line('e3', (35, 28), (35, 32))
        self.add_line('e4', (27, 38), (27, 44))
        self.add_arc('e5-1', (14, 36), (9, 25), radius_x=20, sweep=False)
        self.add_line('e5-2', (9, 25), (8, 20))
        self.add_arc('e5-3', (8, 20), (9, 14), radius_x=19)
        self.add_arc('e5-4', (9, 14), (11, 10), radius_x=16)
        self.add_arc('e5-5', (11, 10), (15, 6), radius_x=15)
        self.add_line('e5-6', (15, 6), (22, 4))
        self.add_arc('e5-7', (22, 4), (35, 14), radius_x=14)
        self.add_arc('e6-1', (35, 32), (32, 37), radius_x=6)
        self.add_line('e6-2', (32, 37), (27, 38))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e1', 'e2', 'e3', 'e6-1', 'e6-2', 'e4')
