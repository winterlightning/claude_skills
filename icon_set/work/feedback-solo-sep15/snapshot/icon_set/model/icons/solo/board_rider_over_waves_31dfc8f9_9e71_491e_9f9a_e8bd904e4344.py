"""Board Rider over Waves, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='31dfc8f9-9e71-491e-9f9a-e8bd904e4344'
SOURCE_PATH='pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'
AUTHOR='gpt-6'

class BoardRiderOverWaves(Solo48):
    icon_id='board-rider-over-waves'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('board', 'rider', 'wave', 'water', 'balance', 'sport')
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
        circle('head',17,9,3)
        self.add_polyline('arms',(6,22),(24,21),(36,6))
        self.add_line('torso',(24,21),(20,24))
        self.relate('connect','arms','torso')
        self.add_polyline('leg',(20,24),(32,24),(35,32))
        self.relate('connect','torso','leg')
        self.add_polyline('board',(12,33),(17,32),(35,32),(42,24))
        self.add_line('standing-leg',(20,24),(17,32))
        self.relate('connect','standing-leg','torso')
        self.relate('connect','standing-leg','leg')
        self.relate('connect','standing-leg','board')
        self.relate('connect','board','leg')
        for n,x in [('left',6),('right',24)]:
            arc('wave-'+n,(x,42),(x+18,42),9,1)
        self.add_contour('water','wave-left','wave-right')
