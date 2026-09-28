"""man-1-5-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The current drawing was the only reference; the hair sweep was stiff at the forehead.
Revision: Recurved the side part for a smoother crown and kept the open shoulder silhouette.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'be348acf-5d1c-56be-a92e-ecad9e444774'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-1-5-avatar/20260926T175531Z-thuan-mac-1/reference/man-1-5-avatar_be348acf-5d1c-56be-a92e-ecad9e444774.svg'
SOURCE_HEAD_ICON_ID = 'man-1-5'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 24
class Man15Avatar(Solo48):
    icon_id = 'man-1-5-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('man', '1', '5', 'portrait', 'bust')
    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((19,15),(23,12),(26,9)), ((29,11),(31,14),(34,14)))
        self.relate('connect', 'head', 'fringe')

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
        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
