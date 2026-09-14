"""Cross-Country Skier, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4ed29164-79b1-5c31-a787-c6eaf3105619'
SOURCE_PATH='pictographic-primitives/sports/skiing cross country_4ed29164-79b1-5c31-a787-c6eaf3105619.svg'
AUTHOR='gpt-6'

class CrossCountrySkier(Solo48):
    icon_id='cross-country-skier'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('ski', 'cross-country', 'skier', 'pole', 'winter', 'stride')
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
        self.add_polyline('arms',(6,22),(18,18),(28,24),(40,19))
        self.add_polyline('torso',(18,18),(20,28),(29,34),(27,42))
        self.relate('connect','arms','torso')
        self.add_polyline('rear-leg',(20,28),(13,34),(6,34))
        self.relate('connect','torso','rear-leg')
        self.add_polyline('pole',(40,12),(40,19),(38,35))
        self.relate('connect','pole','arms')
        self.add_polyline('ski',(9,42),(27,42),(39,42),(42,38))
        self.relate('connect','ski','torso')
