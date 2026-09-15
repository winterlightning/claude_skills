"""A round head above a closed domed torso. VRECT_L extremes (8,4)-(40,44). Lucide user-round informs the circular head and symmetrical shoulder arch. Retain the source flat torso base; enlarge the head-to-shoulder gap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '093e80cf-d93b-43db-a775-fc33b3c13e12'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_093e80cf-d93b-43db-a775-fc33b3c13e12.svg'
AUTHOR = 'gpt-6'


class UserBustRoundedTorso(Solo48):
    icon_id = 'user-bust-rounded-torso'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('user', 'person', 'profile', 'account', 'avatar', 'member', 'people', 'contact')

    def build(self) -> None:
        cx, cy, radius = 24, 11, 7
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders',(8,40),(40,40),radius_x=16,radius_y=12)
        self.add_polyline('base',(40,40),(40,44),(8,44),(8,40))
        self.relate('connect','shoulders','base')
