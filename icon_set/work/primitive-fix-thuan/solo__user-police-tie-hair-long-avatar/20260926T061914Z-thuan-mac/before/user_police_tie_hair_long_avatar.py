"""user-police-tie-hair-long: long hair and uniform tie.
Distinct-avatar plan: preserve reference identity; use long hair and uniform tie.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 28; shoulder top 32; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-12/references/user-police-tie-hair-long.svg'
SOURCE_HEAD_ICON_ID = 'user-police-tie-hair-long'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class UserPoliceTieHairLongAvatar(Solo48):
    icon_id = 'user-police-tie-hair-long-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'police', 'tie', 'hair', 'long', 'portrait', 'bust')
    def build(self):
        cx = 24
        self.add_polyline('cap', (8, 12), (cx, 4), (40, 12), (34, 20), (32, 20), (16, 20), (14, 20), (8, 12))
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'cap', 'band')
        self.add_arc('face', (32,20),(16,20),radius_x=8,radius_y=8)
        self.relate('connect', 'cap', 'face')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 8, 20), ((cx + sign * 8, 24), (cx + sign * 13, 26), (cx + sign * 16, 28)))
            self.relate('connect', 'hair-' + side, 'cap')
            self.relate('connect', 'hair-' + side, 'face')

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
        self.add_polyline('body-tie', (12, top), (24,40), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.add_line('body-tie-tail',(24,40),(24,44))
        self.relate('connect','body-tie-tail','body-tie')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
