"""judo-athlete-man: swept hair and open gi lapels.
Distinct-avatar plan: preserve reference identity; use swept hair and open gi lapels.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 24; shoulder top 28; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c83c8db2-b81d-59b8-9e32-0a97d91dc9fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-judo-athlete-man/20260926T073831Z-thuan-mac/reference/avatar judo athlete man_c83c8db2-b81d-59b8-9e32-0a97d91dc9fc.svg'
SOURCE_HEAD_ICON_ID = 'avatar-judo-athlete-man'
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 30

class AvatarJudoAthleteMan(Solo48):
    icon_id = 'avatar-judo-athlete-man'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'judo', 'athlete', 'man', 'bust', 'body', 'portrait')

    def build(self):
        # Revision per review: the body is a semicircular sweep (a half-ellipse rx 16, ry 10 from
        # (8, 44) over the shoulders to (40, 44)), and the curved hair is replaced by one straight
        # horizontal line across the upper-middle of the head. The head is an r13 circle about
        # (24, 17) so that line can use the 5-12-13 chord (12, 12)-(36, 12) with a clear crown
        # above it. Bust contact: the jaw bottom (24, 30) and the body top (24, 34) are aligned
        # cardinal extremes exactly 4 apart (ink touching), with a direct connect. A single lapel
        # runs from the neck (24, 34) to (30, 44).
        cx, radius, cy = 24, 13, 17
        self.add_arc('crown-left', (cx - 12, cy - 5), (cx, cy - radius), radius_x=radius)
        self.add_arc('crown-right', (cx, cy - radius), (cx + 12, cy - 5), radius_x=radius)
        self.add_arc('cheek-right', (cx + 12, cy - 5), (cx, cy + radius), radius_x=radius)
        self.add_arc('cheek-left', (cx, cy + radius), (cx - 12, cy - 5), radius_x=radius)
        self.add_contour('head', 'crown-left', 'crown-right', 'cheek-right', 'cheek-left', closed=True)
        self.add_line('hair-line', (cx - 12, cy - 5), (cx + 12, cy - 5))
        self.relate('connect', 'head', 'hair-line')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_arc('body-left', (8, 44), (cx, top), radius_x=16, radius_y=44 - top)
        self.add_arc('body-right', (cx, top), (40, 44), radius_x=16, radius_y=44 - top)
        self.add_contour('body', 'body-left', 'body-right')
        self.add_line('lapel', (cx, top), (30, 44))
        self.relate('connect', 'body', 'lapel')
        self.relate('connect', 'head', 'body')
