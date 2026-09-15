"""Pool ball triangle, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1d2c2052-4b90-5fa9-9052-b630e3b3f01b'
SOURCE_PATH='pictographic-primitives/sports/pool triangle_1d2c2052-4b90-5fa9-9052-b630e3b3f01b.svg'
AUTHOR='gpt-6'

class PoolBallTriangle(Solo48):
    icon_id='pool-ball-triangle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('pool', 'ball', 'triangle')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        self.add_polyline('rack',(24,6),(42,42),(6,42),closed=True)
        for n,x,y in [('top',24,24),('left',20,33),('right',28,33)]:
            self.add_dot(n,(x,y))
