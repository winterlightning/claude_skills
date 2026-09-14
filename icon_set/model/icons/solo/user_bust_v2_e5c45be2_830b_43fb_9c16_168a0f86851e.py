"""A round head floats above shoulders. VRECT_L extremes (8,6)-(40,42). Lucide user-round: shared axis, circle and coherent shoulder arc; retain the source gap."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5c45be2-830b-43fb-9c16-168a0f86851e'
SOURCE_PATH = 'pictographic-primitives/symbol/exchange_e5c45be2-830b-43fb-9c16-168a0f86851e.svg'
AUTHOR = 'gpt-6'

class UserBustVariant2(Solo48):
    icon_id = 'user-bust-v2'
    variant_of = 'user-bust'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('user', 'person', 'profile', 'account', 'avatar', 'member', 'contact', 'people')

    def build(self) -> None:
        cx, cy, radius = (24, 12, 8)
        self.add_arc('head-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (8, 44), (40, 44), radius_x=16, radius_y=16)
