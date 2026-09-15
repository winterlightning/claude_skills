'Timer key: round clock with compact hands and a diagonal key shaft, joined at the clock edge.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5819107-8cbd-5b3d-8585-8e32b2d49203'
SOURCE_PATH = 'pictographic-primitives/apps/one time password authentication timer key_c5819107-8cbd-5b3d-8585-8e32b2d49203.svg'
AUTHOR = 'gpt-6'

class OneTimePasswordAuthenticationTimerKey(Solo48):
    icon_id = 'one-time-password-authentication-timer-key'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('one', 'time', 'password', 'authentication', 'timer', 'key', 'apps')

    def build(self) -> None:
        self.add_arc('clock-top', (4,28), (28,28), radius_x=12, radius_y=12)
        self.add_arc('clock-bottom', (28,28), (4,28), radius_x=12, radius_y=12)
        self.add_contour('clock', 'clock-top', 'clock-bottom', closed=True)

        self.add_polyline('hands',(16,25),(16,28),(18,30))
        self.add_polyline('key',(28,28),(28,19),(39,8),(44,13))
        self.add_line('tooth',(32,15),(37,20))
        self.relate('connect','clock','key');self.relate('connect','key','tooth')
