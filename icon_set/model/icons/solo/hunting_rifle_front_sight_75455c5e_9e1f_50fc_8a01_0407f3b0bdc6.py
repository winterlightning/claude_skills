"""Hunting Rifle with Front Sight. Broad stock and long sighted barrel; tiny trigger guard omitted.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75455c5e-9e1f-50fc-8a01-0407f3b0bdc6'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon rifle_75455c5e-9e1f-50fc-8a01-0407f3b0bdc6.svg'
AUTHOR = 'gpt-6'

class HuntingRifleFrontSight(Solo48):
    icon_id = 'hunting-rifle-front-sight'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('rifle', 'hunting', 'stock', 'barrel', 'sight', 'trigger')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def C(n,x,y,r):
            A(n+'a',(x-r,y),(x+r,y),r)
            A(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def J(a,b): self.relate('connect',a,b)
        def R(n,x,y,w,h,r=4):
            L(n+'t',(x+r,y),(x+w-r,y))
            A(n+'tr',(x+w-r,y),(x+w,y+r),r)
            L(n+'r',(x+w,y+r),(x+w,y+h-r))
            A(n+'br',(x+w,y+h-r),(x+w-r,y+h),r)
            L(n+'b',(x+w-r,y+h),(x+r,y+h))
            A(n+'bl',(x+r,y+h),(x,y+h-r),r)
            L(n+'l',(x,y+h-r),(x,y+r))
            A(n+'tl',(x,y+r),(x+r,y),r)
            self.add_contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)

        P('stock',(6,40),(6,29),(16,27),(21,21),(29,21))
        P('underside',(6,40),(17,34),(22,28),(29,28),(29,21));J('underside','stock')
        L('barrel',(29,21),(42,13));J('barrel','stock');J('barrel','underside')
        L('sight',(42,13),(42,8));J('sight','barrel')
