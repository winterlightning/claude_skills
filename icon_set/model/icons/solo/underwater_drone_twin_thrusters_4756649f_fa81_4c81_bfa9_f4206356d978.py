"""Underwater Drone with Twin Thrusters. Symmetric vehicle, twin thrusters and lower arms; central housing simplified.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4756649f-fa81-4c81-bfa9-f4206356d978'
SOURCE_PATH = 'pictographic-primitives/war/underwater drone_4756649f-fa81-4c81-bfa9-f4206356d978.svg'
AUTHOR = 'gpt-6'

class UnderwaterDroneTwinThrusters(Solo48):
    icon_id = 'underwater-drone-twin-thrusters'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('underwater', 'drone', 'thruster', 'robot', 'submersible', 'marine')

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

        P('water',(6,8),(12,11),(24,8),(36,11),(42,8))
        R('body',4,23,40,10,5)
        L('left-thruster',(12,23),(12,20));L('right-thruster',(36,23),(36,20))
        J('left-thruster','body');J('right-thruster','body')
        P('left-leg',(16,33),(16,40),(10,40));P('right-leg',(32,33),(32,40),(38,40))
        J('left-leg','body');J('right-leg','body')
