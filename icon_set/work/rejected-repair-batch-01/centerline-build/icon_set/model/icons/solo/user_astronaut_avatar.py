"""user-astronaut: spacesuit front harness.
Distinct-avatar plan: preserve reference identity; use spacesuit front harness.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 28; shoulder top 32; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-09/references/user-astronaut.svg'
SOURCE_HEAD_ICON_ID = 'user-astronaut'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class UserAstronautAvatar(Solo48):
    icon_id = 'user-astronaut-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('user', 'astronaut', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 16, 12
        self.add_arc('crown',(12,16),(36,16),radius_x=radius)
        self.add_arc('jaw',(36,16),(12,16),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_line('ear-left',(8,16),(12,16))
        self.add_line('ear-right',(36,16),(40,16))
        self.relate('connect','head','ear-left')
        self.relate('connect','head','ear-right')
        self.add_line('visor',(22,16),(26,16))
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-apron-left', (18,top), (18,44))
        self.add_line('body-apron-right', (30,top), (30,44))
        self.relate('connect', 'body-apron-left', 'body-top')
        self.relate('connect', 'body-apron-right', 'body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
