"""Crossed Cutlasses. Two bowed blades cross with the rear partly occluded; straight grips and guards replace tiny loops.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ef35f0a-e6c2-5cd6-861a-50bf28d6a460'
SOURCE_PATH = 'pictographic-primitives/war/pirate sword_0ef35f0a-e6c2-5cd6-861a-50bf28d6a460.svg'
AUTHOR = 'gpt-6'

class CrossedCutlass(Solo48):
    icon_id = 'crossed-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('cutlass', 'sword', 'pirate', 'crossed', 'blade', 'weapon')

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

        A('outer',(6,6),(32,32),26,s=False)
        L('inner',(32,32),(6,6));self.add_contour('front-blade','outer','inner',closed=True)
        A('back-outer',(27,27),(42,6),15,21,s=False)
        L('back-edge',(42,6),(33,15));self.add_contour('back-blade','back-outer','back-edge');J('back-blade','front-blade')
        L('left-grip',(16,37),(10,42))
        L('right-grip',(32,32),(42,42));J('right-grip','front-blade')
        L('left-guard',(6,30),(18,42));J('left-guard','left-grip')
        L('right-guard',(26,38),(38,26));J('right-guard','right-grip');J('right-guard','front-blade')
