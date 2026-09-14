"""Social profile avatar (social), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (14, 36), ((14, 32.709), (12.034, 30.591), (10.451, 28.045)), ((9.086, 25.836), (8, 23.055), (8, 20.345)), ((8, 20.344), (8, 20.343), (8, 20.342)), ((8, 20.261), (8, 20.181), (8, 20.1)), ((8, 19.727), (8.017, 19.355), (8.017, 18.973)), ((8.017, 11.373), (14.257, 4.018), (21.465, 4.018)), ((21.541, 4.009), (21.625, 4.009), (21.701, 4)), ((21.704, 4), (21.708, 4), (21.711, 4)), ((21.918, 4), (22.126, 4.018), (22.341, 4.018)), ((28.286, 4.018), (32.861, 8.236), (35, 14)))
        self.add_bezier('e6', (35, 32), ((35, 32.991), (34.611, 34.218), (34.131, 35.045)), ((32.623, 37.627), (29.526, 37.955), (27, 38)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e6', 'e4')
