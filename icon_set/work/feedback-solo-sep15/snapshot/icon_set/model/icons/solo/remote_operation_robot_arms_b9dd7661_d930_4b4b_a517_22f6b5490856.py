"""Pair of remotely operated robotic tools with central wireless signal. Square envelope; mirrored articulated strokes replace narrow hollow handles. No exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9dd7661-d930-4b4b-a517-22f6b5490856'
SOURCE_PATH = 'pictographic-primitives/technology/operation robot_b9dd7661-d930-4b4b-a517-22f6b5490856.svg'
AUTHOR = 'gpt-6'

class RemoteOperationRobotArms(Solo48):
    icon_id = 'remote-operation-robot-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('robot', 'surgery', 'remote', 'robotic-arms', 'operation', 'wireless', 'medical')

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
        poly('left-arm',(6,14),(6,26),(14,36),(18,42))
        poly('right-arm',(42,14),(42,26),(34,36),(30,42))
        arc('wifi-left',(16,10),(24,6),8,4);arc('wifi-right',(24,6),(32,10),8,4);contour('wifi','wifi-left','wifi-right')
        arc('inner-wifi',(20,20),(28,20),6)
        self.add_dot('signal',(24,28))
