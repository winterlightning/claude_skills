"""korean-woman-1-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The rejected top bun and shirt seam contradicted the side bun head reference.
Revision: Redrew the center parted head with the bun on the right.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__korean-woman-1-avatar/20260926T175531Z-thuan-mac-1/reference/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.svg'
SOURCE_HEAD_ICON_ID = 'korean-woman-1'
AUTHOR = "gpt-6"
class KoreanWoman1Avatar(Solo48):
    icon_id = 'korean-woman-1-avatar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('korean', 'woman', '1', 'portrait', 'bust')
    def build(self):
        # Broad round hair cap, center part, and the source's right side bun.
        cx, cy, radius = 20, 24, 16
        self.add_arc('head-top',(4,24),(36,24),radius_x=radius)
        self.add_arc('head-bottom',(36,24),(4,24),radius_x=radius)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('part-left',(4,24),((12,24),(17,19),(20,8)))
        self.add_bezier('part-right',(20,8),((23,19),(28,24),(36,24)))
        self.add_contour('center-part','part-left','part-right')
        self.relate('connect','head','center-part')
        self.add_arc('bun-top',(36,24),(44,24),radius_x=4)
        self.add_arc('bun-bottom',(44,24),(36,24),radius_x=4)
        self.add_contour('side-bun','bun-top','bun-bottom',closed=True)
        self.relate('connect','head','side-bun')
