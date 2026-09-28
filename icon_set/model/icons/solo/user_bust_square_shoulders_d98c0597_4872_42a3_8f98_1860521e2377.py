"""A round head sits above broad flat shoulders with rounded corners. VRECT_L extremes (8,6)-(40,42). Lucide user informs the circular head and paired quarter-circle shoulders. Open a gap below the head for clarity; retain the flat shoulder top and straight sides."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd98c0597-4872-42a3-8f98-1860521e2377'
SOURCE_PATH = 'pictographic-primitives/symbol/half body person_d98c0597-4872-42a3-8f98-1860521e2377.svg'
AUTHOR = 'gpt-6'

class UserBustSquareShoulders(Solo48):
    icon_id = 'user-bust-square-shoulders'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('user', 'person', 'profile', 'account', 'avatar', 'member', 'people', 'contact')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        cx, cy, radius = (24, 14, 10)
        self.add_arc('head-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('side-left', (8, 44), (8, 38))
        self.add_arc('shoulder-left', (8, 38), (14, 32), radius_x=6)
        self.add_line('shoulder-top', (14, 32), (34, 32))
        self.add_arc('shoulder-right', (34, 32), (40, 38), radius_x=6)
        self.add_line('side-right', (40, 38), (40, 44))
        self.add_contour('shoulders', 'side-left', 'shoulder-left', 'shoulder-top', 'shoulder-right', 'side-right')
