"""drugs dealer.
Plan: Added a capsule dividing seam and two recognizable opposing hands with a visible passing gesture.
Construction: hand-helping: open palm and distinct thumb.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '37a4523d-3384-4c79-9494-a5cfb681f4f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-passing-capsule/20260928T180129Z-thuan-mac/reference/drugs dealer_37a4523d-3384-4c79-9494-a5cfb681f4f0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-passing-capsule'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('drugs', 'dealer')

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

        self.rect('pill',8,18,23,10,5)
        self.add_line('seam',(19,18),(19,28));self.relate('connect','seam','pill')
        self.add_polyline('upper-back',(42,6),(34,10),(25,10),(18,17))
        self.add_bezier('upper-thumb',(42,17),((39,19),(38,21),(35,21)),((33,24),(30,25),(29,23)),((28,21),(31,18),(33,16)))
        self.add_bezier('palm',(6,34),((12,34),(17,33),(20,37)),((25,37),(31,36),(33,38)),((35,39),(36,42),(36,42)))
        self.add_line('palm-base',(6,42),(36,42));self.relate('connect','palm','palm-base')

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve the divided capsule held between an upper hand and a receiving lower palm. Small pill interior and genuine pinch contacts are necessary for the action.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '1b49c6019981c5e0602ed0407fc112144a1a0cdc6777de9d424bf98d35afd17f'}
