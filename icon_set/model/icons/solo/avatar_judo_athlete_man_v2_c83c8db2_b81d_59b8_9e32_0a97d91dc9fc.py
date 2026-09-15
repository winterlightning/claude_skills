"""judo-athlete-man: swept hair and open gi lapels.
Distinct-avatar plan: preserve reference identity; use swept hair and open gi lapels.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 24; shoulder top 28; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c83c8db2-b81d-59b8-9e32-0a97d91dc9fc'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar judo athlete man_c83c8db2-b81d-59b8-9e32-0a97d91dc9fc.svg'
SOURCE_HEAD_ICON_ID = 'avatar-judo-athlete-man'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class AvatarJudoAthleteManVariant2(Solo48):
    icon_id = 'avatar-judo-athlete-man-v2'
    variant_of = 'avatar-judo-athlete-man'
    variant_label = 'Refined solo portrait after visual rejection'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'judo', 'athlete', 'man', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((16, 14), (19, 12), (21, 9)), ((24, 12), (28, 16), (34, 14)))
        self.relate('connect', 'head', 'fringe')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side', (8, 44), (8, 42))
        self.add_arc('body-left-shoulder', (8, 42), (12, top), radius_x=4, radius_y=42 - top)
        self.add_contour('body-left', 'body-left-side', 'body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder', (36, top), (40, 42), radius_x=4, radius_y=42 - top)
        self.add_line('body-right-side', (40, 42), (40, 44))
        self.add_contour('body-right', 'body-right-shoulder', 'body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-tie', (12, top), (24, 44), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')
        self.relate('connect', 'head', 'body-top')
        self.relate('connect', 'head', 'body-top-right')
