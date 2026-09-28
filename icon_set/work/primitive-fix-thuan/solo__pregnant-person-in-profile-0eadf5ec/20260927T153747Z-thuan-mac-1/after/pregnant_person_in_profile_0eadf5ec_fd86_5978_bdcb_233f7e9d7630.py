"""Pregnant Person in Profile.
Plan: (8,4)-(40,44). Round head above curved back and prominent right-facing belly; bent arm rests across belly. Head bottom16 to shoulder24 gives exact8 gap.
References: supplied original source; human_ref/user.svg: circular head and broad curved body; source belly silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0eadf5ec-fd86-5978-bdcb-233f7e9d7630'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pregnant-person-in-profile-0eadf5ec/20260927T153747Z-thuan-mac-1/reference/specialty pregnancy_0eadf5ec-fd86-5978-bdcb-233f7e9d7630.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pregnant-person-in-profile-0eadf5ec'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('pregnant-person-in-profile',)
    keywords = ('pregnant', 'person', 'in', 'profile')

    def build(self):
        # Profile with a rounded belly and one arm cupping it diagonally.
        self.add_arc('head-top', (14, 10), (26, 10), radius_x=6)
        self.add_arc('head-bottom', (26, 10), (14, 10), radius_x=6)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('back-curve', (20, 24), (8, 36), radius_x=12, sweep=False)
        self.add_line('back-leg', (8, 36), (8, 44))
        self.add_contour('back', 'back-curve', 'back-leg')
        self.add_arc('belly-upper', (20, 24), (40, 34), radius_x=20, radius_y=10, sweep=True)
        self.add_arc('belly-lower', (40, 34), (24, 44), radius_x=16, radius_y=10, sweep=True)
        self.add_contour('belly', 'belly-upper', 'belly-lower')
        self.relate('connect', 'back', 'belly')
        self.add_polyline('arm', (20, 24), (24, 32), (40, 34))
        self.relate('connect', 'arm', 'back')
        self.relate('connect', 'arm', 'belly')
