"""Burning Crashed Aircraft. Crashed aircraft, rising flame and one smoke stroke; second smoke trail removed.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81f5c526-61a1-4426-afae-2fec80a31cb2'
SOURCE_PATH = 'pictographic-primitives/war/plane crashed_81f5c526-61a1-4426-afae-2fec80a31cb2.svg'
AUTHOR = 'gpt-6'

class BurningCrashedAircraft(Solo48):
    icon_id = 'burning-crashed-aircraft'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('aircraft', 'crash', 'fire', 'smoke', 'flame', 'wreck')

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

        P('plane',(8,26),(20,30),(17,18),(27,23),(28,34),(40,40),(36,42),(25,39),(18,42),(12,42),(18,36),(8,31),closed=True)
        P('fire',(28,25),(26,17),(31,9),(30,6),(40,14),(40,23),(34,37));J('fire','plane')
        L('smoke',(12,6),(10,14))
