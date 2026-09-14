"""Horse Skijoring, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8a0e37cf-e3ff-4de5-bc93-53ba132c5629'
SOURCE_PATH='pictographic-primitives/sports/skijoring_8a0e37cf-e3ff-4de5-bc93-53ba132c5629.svg'
AUTHOR='gpt-6'

class HorseSkijoring(Solo48):
    icon_id='horse-skijoring'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('skijoring', 'horse', 'ski', 'rider', 'snow', 'winter')
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
        circle('skier-head',9,9,3)
        self.add_polyline('skier',(8,21),(8,29),(14,33),(12,42))
        self.add_polyline('tether',(8,21),(14,23),(22,28))
        self.relate('connect','skier','tether')
        self.add_polyline('ski',(6,42),(12,42),(14,42))
        self.relate('connect','ski','skier')
        self.add_polyline('horse',(22,42),(22,36),(22,28),(30,28),(34,16),(38,12),(42,18),(36,22),(36,36),(36,42))
        self.relate('connect','horse','tether')
        self.add_line('belly',(22,36),(36,36))
        self.relate('connect','belly','horse')
