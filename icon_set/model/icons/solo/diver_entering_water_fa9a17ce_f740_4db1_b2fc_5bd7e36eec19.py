"""Diver Entering Water, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fa9a17ce-f740-4db1-b2fc-5bd7e36eec19'
SOURCE_PATH='pictographic-primitives/sports/swimming diving_fa9a17ce-f740-4db1-b2fc-5bd7e36eec19.svg'
AUTHOR='gpt-6'

class DiverEnteringWater(Solo48):
    icon_id='diver-entering-water'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('diving', 'diver', 'water', 'swimming', 'athlete', 'sport')
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
        self.add_polyline('diver',(6,6),(12,20),(27,28),(30,40))
        circle('head',39,22,3)
        wave('water',40)
        self.relate('connect','diver','water')
