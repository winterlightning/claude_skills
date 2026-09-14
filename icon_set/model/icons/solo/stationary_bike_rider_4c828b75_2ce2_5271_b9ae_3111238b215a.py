"""Stationary Bike Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4c828b75-2ce2-5271-b9ae-3111238b215a'
SOURCE_PATH='pictographic-primitives/sports/sport gym cycling_4c828b75-2ce2-5271-b9ae-3111238b215a.svg'
AUTHOR='gpt-6'

class StationaryBikeRider(Solo48):
    icon_id='stationary-bike-rider'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('cycling', 'bike', 'stationary', 'fitness', 'exercise', 'rider')
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
        circle('head',25,9,3)
        self.add_polyline('rider',(19,19),(12,27),(24,30),(20,34))
        self.add_polyline('arms',(19,19),(27,25),(38,22))
        self.add_line('fork',(38,22),(34,34))
        poly('top',(10,34),(20,34),(34,34),(38,34))
        arc('right',(38,34),(38,42),4)
        self.add_line('bottom',(38,42),(10,42))
        arc('left',(10,42),(10,34),4)
        self.add_contour('base','top-1','top-2','top-3','right','bottom','left',closed=True)
        for x,y in [('rider','arms'),('arms','fork'),('fork','base'),('rider','base')]:self.relate('connect',x,y)
