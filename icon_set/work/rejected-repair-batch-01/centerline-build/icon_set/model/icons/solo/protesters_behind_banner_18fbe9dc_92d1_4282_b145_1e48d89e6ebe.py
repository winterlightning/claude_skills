"""Protesters Behind a Banner. Three heads above wide banner; each pair of legs reduced to one short stroke.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18fbe9dc-92d1-4282-b145-1e48d89e6ebe'
SOURCE_PATH = 'pictographic-primitives/war/protester_18fbe9dc-92d1-4282-b145-1e48d89e6ebe.svg'
AUTHOR = 'gpt-6'

class ProtestersBehindBanner(Solo48):
    icon_id = 'protesters-behind-banner'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('protester', 'banner', 'group', 'crowd', 'demonstration', 'people')

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

        for n,x in [('left',9),('middle',24),('right',39)]:
            C(n+'-head',x,11,3)
            L(n+'-neck',(x,14),(x,22));J(n+'-neck',n+'-head')
        P('banner',(4,22),(44,22),(44,34),(4,34),closed=True)
        for n,x in [('left',9),('middle',24),('right',39)]:
            J(n+'-neck','banner')
            L(n+'-legs',(x,34),(x,40));J(n+'-legs','banner')
