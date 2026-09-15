"""Downhill Skier, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c92285fd-d928-4a7c-a2c3-2e02288f502f'
SOURCE_PATH='pictographic-primitives/sports/skiing slide down_c92285fd-d928-4a7c-a2c3-2e02288f502f.svg'
AUTHOR='gpt-6'

class DownhillSkier(Solo48):
    icon_id='downhill-skier'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('ski', 'downhill', 'skier', 'snow', 'winter', 'athlete')
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
        circle('head',36,14,3)
        self.add_polyline('arms',(14,19),(10,6),(24,13),(27,28),(39,32))
        self.add_polyline('torso',(24,13),(16,27),(23,34),(17,38))
        self.relate('connect','arms','torso')
        self.add_polyline('ski',(6,33),(17,38),(34,42),(42,38))
        self.relate('connect','torso','ski')
