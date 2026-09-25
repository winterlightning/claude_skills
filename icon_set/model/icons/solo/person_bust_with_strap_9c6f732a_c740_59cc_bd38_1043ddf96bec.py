"""A head above rounded shoulders and a short diagonal strap rising from the base. Lucide users informs the shoulders. The strap stays short, preserving the distinction from the full sash."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c6f732a-c740-59cc-bd38-1043ddf96bec'
SOURCE_PATH = 'pictographic-primitives/users/neutral actions_9c6f732a-c740-59cc-bd38-1043ddf96bec.svg'
AUTHOR = 'gpt-6'

class PersonBustWithStrap(Solo48):
    icon_id = 'person-bust-with-strap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('person', 'bust', 'user', 'strap', 'avatar', 'profile', 'account', 'neutral')

    def circle(self, name, cx, cy, radius):
        top, bottom = ((cx, cy - radius), (cx, cy + radius))
        self.add_arc(name + '-a', top, bottom, radius_x=radius)
        self.add_arc(name + '-b', bottom, top, radius_x=radius)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.circle('head', 24, 12, 8)
        self.add_arc('shoulder-left', (8, 36), (16, 28), radius_x=8)
        self.add_line('shoulders', (16, 28), (32, 28))
        self.add_arc('shoulder-right', (32, 28), (40, 36), radius_x=8)
        self.add_line('side-right', (40, 36), (40, 44))
        self.add_line('base-right', (40, 44), (28, 44))
        self.add_line('base-left', (28, 44), (8, 44))
        self.add_line('side-left', (8, 44), (8, 36))
        self.add_contour('body', 'shoulder-left', 'shoulders', 'shoulder-right', 'side-right', 'base-right', 'base-left', 'side-left', closed=True)
        self.add_line('strap', (28, 44), (34, 36))
        self.relate('connect', 'body', 'strap')
