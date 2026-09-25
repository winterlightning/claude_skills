"""Bench Press Station, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d455951e-056e-4788-9743-6d682c228f64'
SOURCE_PATH='pictographic-primitives/sports/sport bench press_d455951e-056e-4788-9743-6d682c228f64.svg'
AUTHOR='gpt-6'

class BenchPressStation(Solo48):
    icon_id='bench-press-station'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('bench', 'press', 'barbell', 'weight', 'fitness', 'equipment')
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
        for n,flip in [('left',False),('right',True)]:
            pts=[(6,6),(14,6),(14,14),(14,22),(10,22),(6,22)]
            self.add_polyline(n,*[mirror(p) if flip else p for p in pts],closed=True)
            x=38 if flip else 10
            self.add_line(n+'-post',(x,22),(x,38))
            self.relate('connect',n,n+'-post')
        self.add_line('bar',(14,14),(34,14))
        for n in ['left','right']:self.relate('connect','bar',n)
        self.add_polyline('bench',(20,28),(28,28),(30,36),(28,36),(20,36),(18,36),closed=True)
        self.add_line('leg-left',(20,36),(18,42))
        self.add_line('leg-right',(28,36),(30,42))
        for n in ['leg-left','leg-right']:self.relate('connect',n,'bench')
