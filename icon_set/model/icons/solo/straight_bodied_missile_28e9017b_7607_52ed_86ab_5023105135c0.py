"""Straight-Bodied Missile. Angular body and tail fins; small nose division and exhaust outline omitted.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '28e9017b-7607-52ed-86ab-5023105135c0'
SOURCE_PATH = 'pictographic-primitives/war/bomb rocket_28e9017b-7607-52ed-86ab-5023105135c0.svg'
AUTHOR = 'gpt-6'

class StraightBodiedMissile(Solo48):
    icon_id = 'straight-bodied-missile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('missile', 'rocket', 'fin', 'nose', 'exhaust', 'flight')

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

        P('body',(16,26),(32,10),(42,6),(38,16),(22,32),(16,26))
        P('left-fin',(24,18),(10,18),(6,30),(16,26));J('left-fin','body')
        P('right-fin',(30,24),(30,38),(18,42),(22,32));J('right-fin','body')
        L('exhaust',(11,37),(6,42))
