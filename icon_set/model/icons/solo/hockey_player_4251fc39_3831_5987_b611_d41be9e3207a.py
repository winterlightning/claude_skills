"""Hockey Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4251fc39-3831-5987-b611-d41be9e3207a'
SOURCE_PATH='pictographic-primitives/sports/sport hockey_4251fc39-3831-5987-b611-d41be9e3207a.svg'
AUTHOR='gpt-6'

class HockeyPlayer(Solo48):
    icon_id='hockey-player'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('hockey', 'player', 'stick', 'puck', 'athlete', 'sport')
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
        circle('head',20,9,3)
        self.add_polyline('body',(15,20),(12,30),(6,42))
        self.add_polyline('front-leg',(12,30),(20,35),(20,42))
        self.add_line('arms',(15,20),(26,24))
        self.add_polyline('stick',(26,24),(28,35),(30,38))
        circle('puck',40,40,2)
        for x,y in [('body','front-leg'),('body','arms'),('arms','stick')]:self.relate('connect',x,y)
