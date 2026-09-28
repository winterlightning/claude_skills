"""Diving Platform, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2820d03d-9e60-4900-ab78-2226f17a6d6e'
SOURCE_PATH='pictographic-primitives/sports/swimming diving board_2820d03d-9e60-4900-ab78-2226f17a6d6e.svg'
AUTHOR='gpt-6'

class DivingPlatform(Solo48):
    icon_id='diving-platform'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('diving', 'platform', 'tower', 'pool', 'swimming', 'equipment')
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
        self.add_polyline('tower',(6,6),(14,6),(14,18),(14,24),(14,42),(6,42),closed=True)
        self.add_polyline('upper-board',(14,6),(26,6),(34,6))
        self.add_line('lower-board',(14,24),(30,24))
        for n in ['upper-board','lower-board']:self.relate('connect',n,'tower')
        arc('water-a',(24,40),(33,40),5,2)
        arc('water-b',(33,40),(42,40),5,2,sweep=False)
        self.add_contour('water','water-a','water-b')
