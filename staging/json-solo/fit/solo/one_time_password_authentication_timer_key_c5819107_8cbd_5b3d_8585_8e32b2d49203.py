"""One time password authentication timer key (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5819107-8cbd-5b3d-8585-8e32b2d49203'
SOURCE_PATH = 'icons-json/apps/one time password authentication timer key_c5819107-8cbd-5b3d-8585-8e32b2d49203.json'
AUTHOR = 'json_to_solo'

class OneTimePasswordAuthenticationTimerKeyApps(Solo48):
    icon_id = 'one-time-password-authentication-timer-key-apps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('one', 'time', 'password', 'authentication', 'timer', 'key', 'apps')

    def build(self):
        self.add_line('e0', (25, 21), (39, 8))
        self.add_line('e1', (39, 8), (44, 12))
        self.add_line('e2', (39, 16), (35, 12))
        self.add_line('e3', (16, 24), (16, 29))
        self.add_line('e4', (16, 29), (19, 32))
        self.add_arc('e5-top', (4, 29), (28, 29), radius_x=12, radius_y=11)
        self.add_arc('e5-bottom', (28, 29), (4, 29), radius_x=12, radius_y=11)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'c0')
