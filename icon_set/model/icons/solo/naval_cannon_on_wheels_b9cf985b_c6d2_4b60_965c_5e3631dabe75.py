"""Naval Cannon on Wheels. Two carriage wheels and fuse distinguish naval cannon; pivot ring omitted.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9cf985b-c6d2-4b60-965c-5e3631dabe75'
SOURCE_PATH = 'pictographic-primitives/war/pirate cannon_b9cf985b-c6d2-4b60-965c-5e3631dabe75.svg'
AUTHOR = 'gpt-6'

class NavalCannonOnWheels(Solo48):
    icon_id = 'naval-cannon-on-wheels'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('cannon', 'naval', 'pirate', 'carriage', 'wheel', 'barrel')

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

        P('barrel',(10,25),(7,18),(40,8),(44,17),(28,23))
        P('carriage',(10,25),(10,31),(40,31),(40,23),(28,23));J('carriage','barrel')
        C('left-wheel',14,37,3);C('right-wheel',38,37,3)
        L('axle-left',(14,31),(14,34));J('axle-left','left-wheel');J('axle-left','carriage')
        L('axle-right',(38,31),(38,34));J('axle-right','right-wheel');J('axle-right','carriage')
        L('fuse',(7,18),(4,12));J('fuse','barrel')
