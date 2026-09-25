"""man-beanie-1: winter jacket and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 34, shoulders 38, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: winter jacket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a04a510f-3d69-41b5-8500-f37570241148'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/man beanie 1_a04a510f-3d69-41b5-8500-f37570241148.svg'
SOURCE_HEAD_ICON_ID = 'man-beanie-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 34
class ManBeanie1Avatar(Solo48):
    icon_id = 'man-beanie-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars', 'primitive', 'primitives')
    aliases = ()
    keywords = ('man', 'beanie', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('cap',(12,16),(36,16),radius_x=12)
        self.add_polyline('cuff',(12,16),(12,24),(36,24),(36,16),(12,16))
        self.relate('connect','cap','cuff')
        self.add_arc('face',(34,24),(14,24),radius_x=10)
        self.relate('connect','face','cuff')
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

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
