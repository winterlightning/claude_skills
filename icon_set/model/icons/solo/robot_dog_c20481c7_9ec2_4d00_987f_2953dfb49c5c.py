"""Left-facing robotic dog with wedge head, raised tail and angular legs. Square envelope. Lucide dog was inspected but its frontal organic head is not useful here; preserve mechanical side-view geometry. Far legs omitted as occluded; two bent legs and flat feet remain."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c20481c7-9ec2-4d00-987f-2953dfb49c5c'
SOURCE_PATH = 'pictographic-primitives/technology/robot pet dog_c20481c7-9ec2-4d00-987f-2953dfb49c5c.svg'
AUTHOR = 'gpt-6'

class RobotDog(Solo48):
    icon_id = 'robot-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('robot', 'dog', 'pet', 'quadruped', 'companion', 'robotic', 'animal')

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
        poly('head',(6,6),(18,6),(18,18),(10,14),closed=True)
        poly('back',(18,18),(36,18),(42,12));connect('back','head')
        poly('front-leg',(18,18),(14,28),(20,34),(16,42),(8,42));connect('front-leg','head');connect('front-leg','back')
        poly('rear-leg',(36,18),(34,28),(40,34),(36,42),(28,42));connect('rear-leg','back')
        line('belly',(14,28),(34,28));connect('belly','front-leg');connect('belly','rear-leg')
