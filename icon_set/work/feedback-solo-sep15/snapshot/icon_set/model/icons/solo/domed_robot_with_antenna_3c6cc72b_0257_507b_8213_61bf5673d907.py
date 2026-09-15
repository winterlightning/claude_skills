"""Half-dome robot with antenna ball. Square envelope, centerline extremes 6/6/42/42. Shared axis and matching circular dome quarters; no identifying feature dropped. Lucide radio-tower beacon construction informs the ball and stem."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c6cc72b-0257-507b-8213-61bf5673d907'
SOURCE_PATH = 'pictographic-primitives/technology/robot spider_3c6cc72b-0257-507b-8213-61bf5673d907.svg'
AUTHOR = 'gpt-6'

class DomedRobotWithAntenna(Solo48):
    icon_id = 'domed-robot-with-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('robot', 'dome', 'antenna', 'spider-robot', 'device', 'rover', 'machine')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        circle('ball',24,10,4)
        line('antenna',(24,14),(24,24));connect('antenna','ball')
        arc('left-dome',(6,42),(24,24),18);arc('right-dome',(24,24),(42,42),18)
        line('base',(42,42),(6,42));contour('dome','left-dome','right-dome','base',closed=True);connect('antenna','dome')
