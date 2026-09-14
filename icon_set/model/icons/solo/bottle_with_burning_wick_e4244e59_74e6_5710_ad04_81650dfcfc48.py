"""Bottle with Burning Wick. Upright bottle and swept burning wick; mouth collar omitted.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4244e59-74e6-5710-ad04-81650dfcfc48'
SOURCE_PATH = 'pictographic-primitives/war/bomb fire bottle_e4244e59-74e6-5710-ad04-81650dfcfc48.svg'
AUTHOR = 'gpt-6'

class BottleWithBurningWick(Solo48):
    icon_id = 'bottle-with-burning-wick'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('bottle', 'wick', 'fire', 'incendiary', 'glass', 'flame')

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

        P('bottle',(8,42),(8,30),(16,22),(16,14),(26,14),(26,22),(32,30),(32,42),(8,42))
        A('wick-rise',(21,14),(29,6),8,10)
        P('flame',(29,6),(34,10),(40,10));J('wick-rise','bottle');J('wick-rise','flame')
