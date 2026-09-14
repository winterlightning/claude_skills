"""Hang Glider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='46124d39-e8cc-47e1-a905-ab2eb126c524'
SOURCE_PATH='pictographic-primitives/sports/sport paragliding_46124d39-e8cc-47e1-a905-ab2eb126c524.svg'
AUTHOR='gpt-6'

class TriangularHangGlider(Solo48):
    icon_id='triangular-hang-glider'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('hang', 'glider', 'pilot', 'flight', 'wing', 'sport')
    def build(self) -> None:
        # HRECT_L centerline extremes (4, 8, 44, 40) from current SOLO48 contract.
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
        self.add_polyline('wing',(4,8),(44,14),(27,18),(10,22),closed=True)
        self.add_line('support',(27,18),(26,34))
        circle('head',37,28,2)
        self.add_polyline('pilot',(8,40),(17,33),(26,34),(35,40),(42,38))
        self.relate('connect','wing','support')
        self.relate('connect','support','pilot')
