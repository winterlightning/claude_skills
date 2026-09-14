"""Standing Rifle Shooter, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ad6a0427-9dcf-56bc-a271-c70f6694c4d6'
SOURCE_PATH='pictographic-primitives/sports/shooting rifle person aim_ad6a0427-9dcf-56bc-a271-c70f6694c4d6.svg'
AUTHOR='gpt-6'

class AimingRifleShooter(Solo48):
    icon_id='aiming-rifle-shooter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('shooting', 'rifle', 'shooter', 'aim', 'target', 'sport')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42) from current SOLO48 contract.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        circle('head',12,9,3)
        self.add_line('torso',(12,21),(12,30))
        self.add_polyline('legs',(6,42),(12,30),(22,42))
        self.relate('connect','torso','legs')
        self.add_polyline('rifle',(12,21),(33,21),(42,21))
        self.relate('connect','rifle','torso')
        self.add_polyline('arms',(12,21),(24,31),(33,21))
        self.relate('connect','arms','rifle')
        self.relate('connect','arms','torso')
