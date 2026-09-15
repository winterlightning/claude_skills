"""Rocket with Porthole. Broad curved rocket hull fits a circular porthole; short open fins, exhaust omitted for spacing.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3077a15f-909e-5ae1-9555-d52644d8badb'
SOURCE_PATH = 'pictographic-primitives/war/rocket attack_3077a15f-909e-5ae1-9555-d52644d8badb.svg'
AUTHOR = 'gpt-6'

class RocketWithPorthole(Solo48):
    icon_id = 'rocket-with-porthole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('rocket', 'porthole', 'space', 'fin', 'exhaust', 'flight')

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

        A('upper',(6,30),(42,6),36,24)
        A('lower',(42,6),(18,42),24,36)
        L('tail',(18,42),(6,30));self.add_contour('body','upper','lower','tail',closed=True)
        C('porthole',24,24,3)
        P('fin',(6,30),(6,20));J('fin','body')
        P('other-fin',(18,42),(28,42));J('other-fin','body')
