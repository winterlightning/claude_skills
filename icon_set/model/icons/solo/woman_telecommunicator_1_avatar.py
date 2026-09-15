"""woman-telecommunicator-1: blouse neckline and headset.
Distinct-avatar plan: preserve reference identity; use blouse neckline and headset.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 28; shoulder top 32; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2b208a3b-47e8-47f4-b99a-2f4763a0e031'
SOURCE_PATH = 'pictographic-primitives/avatars/woman telecommunicator_2b208a3b-47e8-47f4-b99a-2f4763a0e031.svg'
SOURCE_HEAD_ICON_ID = 'woman-telecommunicator-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class WomanTelecommunicator1Avatar(Solo48):
    icon_id = 'woman-telecommunicator-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'telecommunicator', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(12,16),(36,16),radius_x=12)
        self.add_arc('jaw',(36,16),(12,16),radius_x=12)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('fringe',(12,16),((20,18),(26,12),(28,10)),((30,14),(33,16),(36,16)))
        self.relate('connect','head','fringe')
        self.add_line('ear-left',(8,16),(12,16))
        self.add_line('ear-right',(36,16),(40,16))
        self.relate('connect','head','ear-left')
        self.relate('connect','head','ear-right')
        self.add_line('microphone',(40,24),(32,24))
        self.relate('connect','microphone','head')
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
