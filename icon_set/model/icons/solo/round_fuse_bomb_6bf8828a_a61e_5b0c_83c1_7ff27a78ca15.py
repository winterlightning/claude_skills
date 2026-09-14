"""Round Fuse Bomb. Lucide bomb informed circular body; curved fuse replaces small neck collar.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6bf8828a-a61e-5b0c-83c1-7ff27a78ca15'
SOURCE_PATH = 'pictographic-primitives/war/bomb_6bf8828a-a61e-5b0c-83c1-7ff27a78ca15.svg'
AUTHOR = 'gpt-6'

class RoundFuseBomb(Solo48):
    icon_id = 'round-fuse-bomb'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('bomb', 'fuse', 'round', 'explosive', 'weapon', 'sphere')

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

        C('body',24,28,16)
        L('neck',(24,12),(24,10));J('neck','body')
        A('fuse-rise',(24,10),(30,6),6)
        A('fuse-fall',(30,6),(36,10),6)
        self.add_contour('fuse','fuse-rise','fuse-fall');J('fuse','neck')
