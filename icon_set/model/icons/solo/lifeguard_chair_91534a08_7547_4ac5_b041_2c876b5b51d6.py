"""Lifeguard on Chair, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='91534a08-7547-4ac5-b041-2c876b5b51d6'
SOURCE_PATH='pictographic-primitives/sports/swimming lifeguard_91534a08-7547-4ac5-b041-2c876b5b51d6.svg'
AUTHOR='gpt-6'

class LifeguardChair(Solo48):
    icon_id='lifeguard-chair'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('lifeguard', 'chair', 'pool', 'water', 'safety', 'swimming')
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
        circle('head',17,9,3)
        self.add_polyline('rider',(15,20),(15,27),(26,27),(29,29))
        self.add_polyline('seat',(6,20),(7,27),(15,27))
        self.add_polyline('left-leg',(7,27),(6,35),(6,42))
        self.add_polyline('right-leg',(15,27),(18,35),(20,42))
        self.add_line('rung',(6,35),(18,35))
        for n in ['left-leg','right-leg']:self.relate('connect','seat',n);self.relate('connect','rung',n)
        self.relate('connect','rider','seat')
        self.relate('connect','rider','right-leg')
        arc('water-a',(30,40),(36,40),3,2)
        arc('water-b',(36,40),(42,40),3,2,sweep=False)
        self.add_contour('water','water-a','water-b')
