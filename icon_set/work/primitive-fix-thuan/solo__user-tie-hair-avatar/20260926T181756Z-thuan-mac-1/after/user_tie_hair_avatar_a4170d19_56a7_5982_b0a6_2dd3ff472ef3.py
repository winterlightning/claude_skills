"""Revision from the claimed current drawing: preserve the subject and improve its distinguishing feature.
The original source is unavailable; the staged reference is the rejected drawing.
Human proportions follow icon_set/references/human_ref/user.svg.
"""
"""user-tie-hair: broad blouse collar and tie.
Distinct-avatar plan: preserve reference identity; use broad blouse collar and tie.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 22; shoulder top 26; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = "a4170d19-56a7-5982-b0a6-2dd3ff472ef3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__user-tie-hair-avatar/20260926T181756Z-thuan-mac-1/reference/user-tie-hair-avatar_a4170d19-56a7-5982-b0a6-2dd3ff472ef3.svg"
SOURCE_HEAD_ICON_ID = 'user-tie-hair'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 22
class UserTieHairAvatar(Solo48):
    icon_id = 'user-tie-hair-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'tie', 'hair', 'portrait', 'bust')
    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16, 14), pt(16, 18))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(8, 14), radius_x=8, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (32, 14), (16, 14), radius_x=8, radius_y=8)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-tie', (12, top), (24,36), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.add_line('body-tie-tail',(24,36),(24,44))
        self.relate('connect','body-tie-tail','body-tie')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
