"""A round head sits above broad flat shoulders with rounded corners. VRECT_L extremes (8,6)-(40,42). Lucide user informs the circular head and paired quarter-circle shoulders. Open a gap below the head for clarity; retain the flat shoulder top and straight sides."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd98c0597-4872-42a3-8f98-1860521e2377'
SOURCE_PATH = 'pictographic-primitives/symbol/half body person_d98c0597-4872-42a3-8f98-1860521e2377.svg'
AUTHOR = 'gpt-6'


class UserBustSquareShoulders(Solo48):
    icon_id = 'user-bust-square-shoulders'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('user', 'person', 'profile', 'account', 'avatar', 'member', 'people', 'contact')

    def build(self) -> None:
        cx, cy, radius = 24, 14, 10
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('side-left',(8,42),(8,39))
        self.add_arc('shoulder-left',(8,39),(14,33),radius_x=6)
        self.add_line('shoulder-top',(14,33),(34,33))
        self.add_arc('shoulder-right',(34,33),(40,39),radius_x=6)
        self.add_line('side-right',(40,39),(40,42))
        self.add_contour('shoulders','side-left','shoulder-left','shoulder-top','shoulder-right','side-right')
