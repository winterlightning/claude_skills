"""Korean Woman: asymmetric wrap jacket, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Face center is (24,14), radius 10; shoulder ink touches the face.
The side bun is reduced to radius 3 to preserve the centered face and keyshape.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__korean-woman/20260926T175531Z-thuan-mac-1/reference/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.svg'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class KoreanWoman(Solo48):
    icon_id = 'korean-woman'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('korean', 'woman', 'avatars')

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
