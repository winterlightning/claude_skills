"""Curved-Bodied Missile. Curved contour and angled fins; open exhaust and no nose seam.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a29174e5-8932-5000-98b7-fae037ea20c4'
SOURCE_PATH = 'pictographic-primitives/war/bomb rocket_a29174e5-8932-5000-98b7-fae037ea20c4.svg'
AUTHOR = 'gpt-6'

class CurvedBodiedMissile(Solo48):
    icon_id = 'curved-bodied-missile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('missile', 'rocket', 'fin', 'exhaust', 'flight', 'weapon')

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

        A('upper',(14,26),(42,6),28,20)
        A('lower',(42,6),(22,34),20,28)
        L('tail',(22,34),(14,26));self.add_contour('body','upper','lower','tail',closed=True)
        P('left-fin',(14,26),(6,28),(8,20));J('left-fin','body')
        P('right-fin',(22,34),(20,42),(28,40));J('right-fin','body')
        L('exhaust',(10,38),(6,42))
