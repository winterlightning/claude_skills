"""Pool Jump, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0647ba7a-9aee-4d01-9f39-460d6cba1bee'
SOURCE_PATH='pictographic-primitives/sports/swimming jump_0647ba7a-9aee-4d01-9f39-460d6cba1bee.svg'
AUTHOR='gpt-6'

class PoolJump(Solo48):
    icon_id='pool-jump'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('pool', 'jump', 'swimmer', 'water', 'diving', 'sport')
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
        circle('head',33,13,3)
        self.add_polyline('body',(18,6),(24,23),(12,22),(23,30),(18,32))
        self.add_line('arm',(24,23),(12,13))
        self.relate('connect','arm','body')
        self.add_polyline('edge',(6,42),(14,42),(14,40),(30,40))
        arc('water-a',(30,40),(36,40),3,2)
        arc('water-b',(36,40),(42,40),3,2,sweep=False)
        self.add_contour('water','water-a','water-b')
        self.relate('connect','edge','water')
