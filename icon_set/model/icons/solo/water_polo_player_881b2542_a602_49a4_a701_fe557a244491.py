"""Water Polo Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='881b2542-a602-49a4-a701-fe557a244491'
SOURCE_PATH='pictographic-primitives/sports/swimming waterpolo_881b2542-a602-49a4-a701-fe557a244491.svg'
AUTHOR='gpt-6'

class WaterPoloPlayer(Solo48):
    icon_id='water-polo-player'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('water', 'polo', 'player', 'ball', 'swimming', 'sport')
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
        def wave(n,y):
            for i,x in enumerate((6,18,30)):
                arc(f'{n}-{i}',(x,y),(x+12,y),6,2,sweep=i%2==0)
            self.add_contour(n,*[f'{n}-{i}' for i in range(3)])
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        circle('ball',35,10,4)
        circle('head',20,19,3)
        self.add_polyline('arm-body',(35,14),(29,29),(18,31),(12,34),(6,40))
        self.add_line('torso',(29,29),(30,40))
        wave('water',40)
        for x,y in [('arm-body','ball'),('arm-body','torso'),('torso','water'),('arm-body','water')]:self.relate('connect',x,y)
