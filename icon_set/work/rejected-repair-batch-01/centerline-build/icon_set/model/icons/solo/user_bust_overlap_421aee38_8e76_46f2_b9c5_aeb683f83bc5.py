"""A round head meeting a broad shoulder arc. VRECT_L centerline extremes (8,4)-(40,44). Lucide user-round informs coherent circular head and shoulder curves. Replace the source overlap with an explicit tangent contact at the shared center endpoint; preserve the connected head-and-shoulders reading."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '421aee38-8e76-46f2-b9c5-aeb683f83bc5'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_421aee38-8e76-46f2-b9c5-aeb683f83bc5.svg'
AUTHOR = 'gpt-6'


class UserBustOverlap(Solo48):
    icon_id = 'user-bust-overlap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('user', 'person', 'profile', 'account', 'avatar', 'member', 'contact', 'people')

    def build(self) -> None:
        self.add_arc('head-left',(24,28),(24,4),radius_x=12)
        self.add_arc('head-right',(24,4),(24,28),radius_x=12)
        self.add_contour('head','head-left','head-right',closed=True)
        self.add_arc('shoulder-left',(8,44),(24,28),radius_x=16)
        self.add_arc('shoulder-right',(24,28),(40,44),radius_x=16)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','head','shoulders')
