"""man-astronaut-1: spacesuit chest panel and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 28, shoulders 32, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: spacesuit chest panel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-04/references/man-astronaut-1.svg'
SOURCE_HEAD_ICON_ID = 'man-astronaut-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class ManAstronaut1Avatar(Solo48):
    icon_id = 'man-astronaut-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'astronaut', '1', 'portrait', 'bust')
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
        self.add_line('body-band', (8,42), (40,42))
        self.relate('connect', 'body-band', 'body-left')
        self.relate('connect', 'body-band', 'body-right')
        self.add_line('body-fastening', (24,top), (24,42))
        self.relate('connect', 'body-fastening', 'body-top')
        self.relate('connect', 'body-fastening', 'body-top-right')
        self.relate('connect', 'body-fastening', 'body-band')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
