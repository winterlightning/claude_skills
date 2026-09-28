"""Revision from the claimed current drawing: preserve the subject and improve its distinguishing feature.
The original source is unavailable; the staged reference is the rejected drawing.
Human proportions follow icon_set/references/human_ref/user.svg.
"""
"""user-vneck-hair: deep blouse V neckline.
Distinct-avatar plan: preserve reference identity; use deep blouse V neckline.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 22; shoulder top 26; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = "4d1572d4-fe02-5f11-b6c9-46f0bd80f617"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__user-vneck-hair-avatar/20260926T181756Z-thuan-mac-1/reference/user-vneck-hair-avatar_4d1572d4-fe02-5f11-b6c9-46f0bd80f617.svg"
SOURCE_HEAD_ICON_ID = 'user-vneck-hair'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 22
class UserVneckHairAvatar(Solo48):
    icon_id = 'user-vneck-hair-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'vneck', 'hair', 'portrait', 'bust')
    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16, 14), pt(16, 20))
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
        self.add_polyline('body-tie', (12, top), (24,38), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
