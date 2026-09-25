"""Top-view quadcopter with four circular rotor guards and a central body. Square envelope. Lucide drone informs four radial arms; rotor crossbars and central sensor omitted to keep openings clear."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c120838-ef37-5a04-823d-a39b12a8a7bf'
SOURCE_PATH = 'pictographic-primitives/technology/robot drone_0c120838-ef37-5a04-823d-a39b12a8a7bf.svg'
AUTHOR = 'gpt-6'

class QuadcopterDroneTopView(Solo48):
    icon_id = 'quadcopter-drone-top-view'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drone', 'quadcopter', 'rotors', 'aerial', 'uav', 'robot', 'top-view')

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
        for n,x,y in [('tl',12,12),('tr',36,12),('bl',12,36),('br',36,36)]:circle(n,x,y,6)
        poly('body',(20,20),(28,20),(28,28),(20,28),closed=True)
        for n,a,b,node in [('tl-link',(12,18),(20,20),'tl'),('tr-link',(36,18),(28,20),'tr'),('bl-link',(12,30),(20,28),'bl'),('br-link',(36,30),(28,28),'br')]:
            line(n,a,b);connect(n,node);connect(n,'body')
