"""Eight ball, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='da44a824-a8a5-4c75-8b61-855bba1f9a37'
SOURCE_PATH='pictographic-primitives/sports/pool black ball_da44a824-a8a5-4c75-8b61-855bba1f9a37.svg'
AUTHOR='gpt-6'

class EightBall(Solo48):
    icon_id='eight-ball'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('eight', 'ball')
    def build(self) -> None:
        # CIRCLE centerline extremes (4, 4, 44, 44).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        circle('ball',24,24,20)
        circle('eight-top',24,21,3)
        circle('eight-bottom',24,27,3)
        self.relate('connect','eight-top','eight-bottom')
