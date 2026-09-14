"""Snow Scooter Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='87213404-4655-52bf-a1d8-6be4687cfea8'
SOURCE_PATH='pictographic-primitives/sports/skiing snow scooter person_87213404-4655-52bf-a1d8-6be4687cfea8.svg'
AUTHOR='gpt-6'

class SnowScooterRider(Solo48):
    icon_id='snow-scooter-rider'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('snow', 'scooter', 'rider', 'winter', 'handlebar', 'sport')
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
        circle('head',29,9,3)
        self.add_polyline('body',(20,19),(12,28),(20,33),(17,40))
        self.add_polyline('arms',(20,19),(27,25),(38,25))
        self.relate('connect','body','arms')
        self.add_polyline('stem',(39,20),(38,25),(30,42))
        self.relate('connect','arms','stem')
        self.add_polyline('runner',(6,38),(17,40),(30,42),(36,42),(42,36))
        self.relate('connect','body','runner')
        self.relate('connect','stem','runner')
