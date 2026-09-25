"""Running figure with bent arms, raised leg and motion marks. Square envelope; Lucide person-standing connected-limb reduction, with deliberate rightward stride."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '265af8e7-ec02-4865-b96a-7f40d0446cd3'
SOURCE_PATH = 'pictographic-primitives/technology/motion sensor person_265af8e7-ec02-4865-b96a-7f40d0446cd3.svg'
AUTHOR = 'gpt-6'

class RunningPersonMotionMarks(Solo48):
    icon_id = 'running-person-motion-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('motion', 'running', 'person', 'sensor', 'movement', 'activity', 'detection')

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
        circle('head',29,9,3)
        poly('torso',(27,21),(23,30),(33,34),(36,42))
        poly('arm-front',(27,21),(35,25),(40,21));connect('arm-front','torso')
        poly('arm-back',(27,21),(19,18),(14,24));connect('arm-back','torso');connect('arm-back','arm-front')
        poly('leg-back',(23,30),(17,38),(8,38));connect('leg-back','torso')
        line('motion-left',(6,12),(6,18));line('motion-right',(42,30),(42,32))
