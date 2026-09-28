"""Radar Dial with Outer Ticks. Dial, cardinal ticks and upper-left sweep; center ring retained.
Keyshape CIRCLE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '98f5c8e1-3bcb-4332-a117-c53c88b9300f'
SOURCE_PATH = 'pictographic-primitives/war/surveillance location 1_98f5c8e1-3bcb-4332-a117-c53c88b9300f.svg'
AUTHOR = 'gpt-6'

class RadarDialOuterTicks(Solo48):
    icon_id = 'radar-dial-outer-ticks'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('radar', 'dial', 'sweep', 'circle', 'surveillance', 'target')

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

        C('dial',24,24,17);self.add_dot('hub',(24,24))
        for n,a,b in [('top',(24,7),(24,4)),('bottom',(24,41),(24,44)),('left',(7,24),(4,24)),('right',(41,24),(44,24))]:
            L(n,a,b);J(n,'dial')
        L('sweep',(24,24),(9,16));J('sweep','dial');J('sweep','hub')
