"""man-riot: protective vest fastening with reference hair/headwear.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 32, shoulders 36, zero painted gap. Curved shoulders follow
human_ref/user.svg; Lucide user-round original and atomic-debug guide arcs.
Fine trim omitted at 48; clothing cue: protective vest fastening. Source asymmetry is retained
in headwear while the face stays centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-06/references/man-riot.svg'
SOURCE_HEAD_ICON_ID = 'man-riot'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class ManRiotAvatar(Solo48):
    icon_id = 'man-riot-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'riot', 'portrait', 'bust')
    def build(self):
        self.add_polyline('crest',(20,4),(28,4),(28,12),(24,12),(20,12),(20,4))
        self.add_arc('crown-left',(14,22),(24,12),radius_x=10)
        self.add_arc('crown-right',(24,12),(34,22),radius_x=10)
        self.add_arc('jaw',(34,22),(14,22),radius_x=10)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.relate('connect','head','crest')
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
