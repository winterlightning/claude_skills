"""Golf Club and Teed Ball, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='337002cc-2478-5387-ba44-b90e337ec1b0'
SOURCE_PATH='pictographic-primitives/sports/sport golf club_337002cc-2478-5387-ba44-b90e337ec1b0.svg'
AUTHOR='gpt-6'

class GolfClubTeedBall(Solo48):
    icon_id='golf-club-teed-ball'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('golf', 'club', 'ball', 'tee', 'equipment', 'sport')
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
        self.add_line('shaft',(25,19),(42,6))
        arc('head-curve',(13,14),(13,24),7,5,sweep=False)
        poly('head-edge',(13,24),(25,19),(13,14))
        self.add_contour('club-head','head-curve','head-edge-1','head-edge-2',closed=True)
        self.relate('connect','shaft','club-head')
        circle('ball',34,32,3)
        self.add_line('tee',(34,35),(34,42))
        self.add_polyline('ground',(28,42),(34,42),(40,42))
        self.relate('connect','ball','tee')
        self.relate('connect','ground','tee')
