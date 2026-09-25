"""user-beard: beard and open jacket.
Distinct-avatar plan: preserve reference identity; use beard and open jacket.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 28; shoulder top 32; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-09/references/user-beard.svg'
SOURCE_HEAD_ICON_ID = 'user-beard'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class UserBeardAvatar(Solo48):
    icon_id = 'user-beard-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'beard', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 16, 12
        self.add_arc('crown',(12,16),(36,16),radius_x=radius)
        self.add_arc('jaw',(36,16),(12,16),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('beard',(12,16),((16,24),(20,16),(24,20)),((28,16),(32,24),(36,16)))
        self.relate('connect','head','beard')
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
        self.add_polyline('body-tie', (12, top), (24,44), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
