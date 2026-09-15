"""muslim-dad-son-1: rounded tunic neck.
Distinct-avatar plan: preserve reference identity; use rounded tunic neck.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 26; shoulder top 30; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-07/references/muslim-dad-son-1.svg'
SOURCE_HEAD_ICON_ID = 'muslim-dad-son-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class MuslimDadSon1Avatar(Solo48):
    icon_id = 'muslim-dad-son-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('muslim', 'dad', 'son', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('cap-top',(12,12),(36,12),radius_x=12,radius_y=8)
        self.add_polyline('cap-base',(36,12),(36,16),(12,16),(12,12))
        self.relate('connect','cap-top','cap-base')
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','cap-base')
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
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect','body-neckline','body-top')
        self.relate('connect','body-neckline','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
