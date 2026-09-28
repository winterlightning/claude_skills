"""mahayana-monk: diagonal robe and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 24, shoulders 28, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: diagonal robe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-04/references/mahayana-monk.svg'
SOURCE_HEAD_ICON_ID = 'mahayana-monk'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class MahayanaMonkAvatar(Solo48):
    icon_id = 'mahayana-monk-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('mahayana', 'monk', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 14, 10
        self.add_arc('crown',(14,14),(34,14),radius_x=radius)
        self.add_arc('jaw',(34,14),(14,14),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
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
        self.add_polyline('body-wrap', (18,top), (30,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
