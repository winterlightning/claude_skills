"""Underwater Drone with Claw. Waterline, torpedo hull and jointed claw; internal hull seam removed.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd23e8415-7129-4003-9c39-95ff203bcfe9'
SOURCE_PATH = 'pictographic-primitives/war/underwater drone 1_d23e8415-7129-4003-9c39-95ff203bcfe9.svg'
AUTHOR = 'gpt-6'

class UnderwaterDroneWithClaw(Solo48):
    icon_id = 'underwater-drone-with-claw'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('underwater', 'drone', 'submersible', 'claw', 'robot', 'marine')

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

        P('water',(6,10),(10,8),(17,10),(24,8),(31,10),(38,8),(42,10))
        R('hull',10,20,34,12,6)
        P('tail',(6,20),(10,26),(6,32));J('tail','hull')
        P('arm',(25,32),(25,40),(34,40));J('arm','hull')
        P('claw',(40,35),(34,40),(40,40));J('claw','arm')
