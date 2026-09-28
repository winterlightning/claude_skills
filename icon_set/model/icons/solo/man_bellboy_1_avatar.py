"""man-bellboy-1: uniform front bands and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 24, shoulders 28, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: uniform front bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c204bbb4-18f5-5b91-af1a-c247e0a589d2'
SOURCE_PATH = 'pictographic-primitives/avatars/man bellboy_c204bbb4-18f5-5b91-af1a-c247e0a589d2.svg'
SOURCE_HEAD_ICON_ID = 'man-bellboy-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class ManBellboy1Avatar(Solo48):
    icon_id = 'man-bellboy-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'bellboy', '1', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(14,14),(14,4),(34,4),(34,14))
        self.add_line('cap-bottom',(14,14),(34,14))
        self.relate('connect','cap','cap-bottom')
        self.add_arc('face',(34,14),(14,14),radius_x=10)
        self.relate('connect','face','cap-bottom')
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

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
