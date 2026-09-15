"""user-hoodie: rounded hood and zipper.
Distinct-avatar plan: preserve reference identity; use rounded hood and zipper.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 30; shoulder top 34; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-11/references/user-hoodie.svg'
SOURCE_HEAD_ICON_ID = 'user-hoodie'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class UserHoodieAvatar(Solo48):
    icon_id = 'user-hoodie-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('user', 'hoodie', 'portrait', 'bust')
    def build(self):
        self.add_arc('hood',(8,20),(40,20),radius_x=16)
        self.add_line('hood-left',(8,28),(8,20))
        self.add_line('hood-right',(40,20),(40,28))
        self.add_contour('veil','hood-left','hood', 'hood-right')
        self.add_arc('crown',(17,23),(31,23),radius_x=7)
        self.add_arc('face',(31,23),(17,23),radius_x=7)
        self.add_contour('head','crown','face',closed=True)
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
