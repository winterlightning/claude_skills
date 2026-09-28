"""Quadcopter Drone. Four rotor rings and shared central arm junction; central body reduced to joint.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5512d99-74c8-5dbb-9bfe-e3970ff37efe'
SOURCE_PATH = 'pictographic-primitives/war/ground drone_d5512d99-74c8-5dbb-9bfe-e3970ff37efe.svg'
AUTHOR = 'gpt-6'

class QuadcopterDrone(Solo48):
    icon_id = 'quadcopter-drone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('drone', 'quadcopter', 'rotor', 'aircraft', 'remote', 'propeller')

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

        for n,x,y in [('nw',12,12),('ne',36,12),('sw',12,36),('se',36,36)]:
            C(n,x,y,6)
            L(n+'-arm',(x,y),(24,24));J(n,n+'-arm')
        for a,b in [('nw','ne'),('nw','sw'),('nw','se'),('ne','sw'),('ne','se'),('sw','se')]: J(a+'-arm',b+'-arm')
