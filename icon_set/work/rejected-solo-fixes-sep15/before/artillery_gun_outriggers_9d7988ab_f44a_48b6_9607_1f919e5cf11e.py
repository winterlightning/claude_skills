"""Artillery Gun on Outriggers. Angled gun, wheel and spreading outriggers; square muzzle simplified to end cap.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d7988ab-f44a-48b6-9607-1f919e5cf11e'
SOURCE_PATH = 'pictographic-primitives/war/tank machine gun_9d7988ab-f44a-48b6-9607-1f919e5cf11e.svg'
AUTHOR = 'gpt-6'

class ArtilleryGunOutriggers(Solo48):
    icon_id = 'artillery-gun-outriggers'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('artillery', 'gun', 'barrel', 'wheel', 'outrigger', 'military')

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

        C('wheel',20,30,10)
        P('breech',(13,23),(12,17),(21,11),(29,17),(26,22));J('breech','wheel')
        L('barrel',(25,14),(38,8));J('barrel','breech')
        L('muzzle',(35,8),(41,14));J('muzzle','barrel')
        L('left-leg',(12,36),(4,40));J('left-leg','wheel')
        P('right-leg',(28,36),(36,36),(44,40));J('right-leg','wheel')
