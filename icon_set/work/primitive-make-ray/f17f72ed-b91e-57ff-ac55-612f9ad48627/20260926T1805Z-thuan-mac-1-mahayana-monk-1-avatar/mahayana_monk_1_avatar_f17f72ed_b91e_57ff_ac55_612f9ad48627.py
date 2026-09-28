"""mahayana-monk-1: folded robe neckline and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 24, shoulders 28, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: folded robe neckline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f17f72ed-b91e-57ff-ac55-612f9ad48627'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mahayana-monk-1-avatar/20260926T175531Z-thuan-mac-1/reference/mahayana-monk-1-avatar_f17f72ed-b91e-57ff-ac55-612f9ad48627.svg'
SOURCE_HEAD_ICON_ID = 'mahayana-monk-1'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 24
class MahayanaMonk1Avatar(Solo48):
    icon_id = 'mahayana-monk-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('mahayana', 'monk', '1', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 14, 10
        self.add_arc('crown',(14,14),(34,14),radius_x=radius)
        self.add_arc('jaw',(34,14),(14,14),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('robe-neck',(16,top),(24,42),(32,top))
        self.relate('connect','robe-neck','body-top')
        self.relate('connect','robe-neck','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
