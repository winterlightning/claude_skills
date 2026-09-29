"""bike cargo back.
Plan: Restored full-size wheels and a triangular bicycle frame beneath a compact rear cargo box.
Construction: bike: equal circular wheels; car: open connected silhouette.
Keyshape: HRECT_L; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '697554f1-3afd-5c1d-87a3-50b358ece127'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cargo-bicycle-rear-box/20260928T180129Z-thuan-mac/reference/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cargo-bicycle-rear-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bike', 'cargo', 'back')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.circle('rear',12,32,8);self.circle('front',36,32,8)
        self.rect('cargo',4,8,16,12,2)
        self.add_polyline('frame',(12,32),(23,32),(32,20),(20,20))
        self.add_polyline('fork',(36,32),(29,8),(25,8))
        
        self.relate('connect','frame','rear');self.relate('connect','fork','front');self.relate('connect','frame','cargo');

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve a rear cargo box and two full bicycle wheels with connected frame and fork. These genuine compact mechanical parts require closer spacing.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'f4a69e72188efc5096396206f37a8dbbb497bc1a977aa254e5f9dc1947d4b188'}
