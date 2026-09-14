"""Circular Radar Sweep. Two circular rings and upper-right sweep retain the radar reading.
Keyshape CIRCLE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b97bdca9-06a5-5d5a-95b9-90e3ce59cd2b'
SOURCE_PATH = 'pictographic-primitives/war/surveillance target_b97bdca9-06a5-5d5a-95b9-90e3ce59cd2b.svg'
AUTHOR = 'gpt-6'

class CircularRadarSweep(Solo48):
    icon_id = 'circular-radar-sweep'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('radar', 'sweep', 'circle', 'dial', 'surveillance', 'scan')

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

        C('outer',24,24,20);C('inner',24,24,10)
        L('sweep',(24,24),(36,8));J('sweep','inner');J('sweep','outer')
