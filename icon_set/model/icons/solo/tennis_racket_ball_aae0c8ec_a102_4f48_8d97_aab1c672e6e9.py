"""Tennis Racket and Ball, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='aae0c8ec-a102-4f48-8d97-aab1c672e6e9'
SOURCE_PATH='pictographic-primitives/sports/tennis racquet ball_aae0c8ec-a102-4f48-8d97-aab1c672e6e9.svg'
AUTHOR='gpt-6'

class TennisRacketBall(Solo48):
    icon_id='tennis-racket-ball'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('tennis', 'racket', 'ball', 'equipment', 'court', 'sport')
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
        def wave(n,y):
            for i,x in enumerate((6,18,30)):
                arc(f'{n}-{i}',(x,y),(x+12,y),6,2,sweep=i%2==0)
            self.add_contour(n,*[f'{n}-{i}' for i in range(3)])
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        arc('racket-a',(32,6),(42,16),10)
        arc('racket-b',(42,16),(28,32),14,16)
        arc('racket-c',(28,32),(20,28),10)
        arc('racket-d',(20,28),(18,22),10)
        arc('racket-e',(18,22),(32,6),14,16)
        self.add_contour('racket','racket-a','racket-b','racket-c','racket-d','racket-e',closed=True)
        self.add_line('handle',(6,42),(20,28))
        self.relate('connect','racket','handle')
        circle('ball',9,9,3)
