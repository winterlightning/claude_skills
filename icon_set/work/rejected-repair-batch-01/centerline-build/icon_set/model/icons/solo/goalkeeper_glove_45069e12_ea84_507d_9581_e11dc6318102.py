"""Goalkeeper Glove, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='45069e12-ea84-507d-9581-e11dc6318102'
SOURCE_PATH='pictographic-primitives/sports/soccer goalkeeper glove_45069e12-ea84-507d-9581-e11dc6318102.svg'
AUTHOR='gpt-6'

class GoalkeeperGlove(Solo48):
    icon_id='goalkeeper-glove'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('goalkeeper', 'glove', 'soccer', 'football', 'hand', 'protection')
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
        poly('edge',(10,24),(10,12))
        arc('index',(10,12),(18,12),4)
        self.add_line('step-a',(18,12),(18,10))
        arc('middle',(18,10),(26,10),4)
        self.add_line('step-b',(26,10),(26,12))
        arc('ring',(26,12),(34,12),4)
        self.add_line('step-c',(34,12),(34,18))
        arc('little',(34,18),(42,18),4)
        poly('palm',(42,18),(42,26),(36,34),(36,42),(16,42),(16,34),(6,26),(8,20),(10,24))
        self.add_contour('outline','edge-1','index','step-a','middle','step-b','ring','step-c','little',*[f'palm-{i}' for i in range(1,9)],closed=True)
        for x,y,z in [(18,12,23),(26,12,23),(34,18,25)]:
            self.add_line(f'finger-{x}',(x,y),(x,z))
            self.relate('connect',f'finger-{x}','outline')
        self.add_line('cuff',(16,34),(36,34))
        self.relate('connect','cuff','outline')
