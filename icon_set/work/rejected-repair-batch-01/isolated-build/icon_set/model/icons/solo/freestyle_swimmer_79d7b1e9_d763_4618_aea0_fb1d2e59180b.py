"""Swimmer, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='79d7b1e9-d763-4618-aea0-fb1d2e59180b'
SOURCE_PATH='pictographic-primitives/sports/swimming_79d7b1e9-d763-4618-aea0-fb1d2e59180b.svg'
AUTHOR='gpt-6'

class FreestyleSwimmer(Solo48):
    icon_id='freestyle-swimmer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('swimmer', 'swimming', 'water', 'stroke', 'pool', 'sport')
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
        circle('head',35,13,3)
        self.add_polyline('arm',(10,23),(21,14),(20,6),(14,6))
        self.add_polyline('body',(21,14),(28,23),(30,28))
        self.relate('connect','arm','body')
        wave('water-top',28)
        self.relate('connect','body','water-top')
        wave('water-bottom',40)
