"""Horse Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='932e176d-8abb-4412-94f0-22f2542b288a'
SOURCE_PATH='pictographic-primitives/sports/sport horse riding_932e176d-8abb-4412-94f0-22f2542b288a.svg'
AUTHOR='gpt-6'

class HorseRider(Solo48):
    icon_id='horse-rider'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('horse', 'rider', 'equestrian', 'helmet', 'animal', 'sport')
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
        circle('head',24,9,3)
        self.add_polyline('rider',(19,20),(14,26),(22,29),(20,37))
        self.add_polyline('arms',(19,20),(27,24),(34,18))
        self.add_polyline('horse',(14,26),(28,28),(34,18),(38,18),(42,26),(34,26),(31,34),(38,38),(37,42))
        self.add_polyline('rear-leg',(14,26),(12,34),(8,42))
        self.add_polyline('tail',(6,32),(8,27),(14,26))
        for x,y in [('rider','arms'),('rider','horse'),('arms','horse'),('horse','rear-leg'),('horse','tail'),('rider','rear-leg'),('rider','tail'),('tail','rear-leg')]:self.relate('connect',x,y)
