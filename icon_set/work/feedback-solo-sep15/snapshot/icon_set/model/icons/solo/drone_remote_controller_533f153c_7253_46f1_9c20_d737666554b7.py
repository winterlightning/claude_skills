"""Drone remote with twin dials and central transmitting antenna; one pair of radio arcs retained. Lucide radio-receiver rounded housing; square envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '533f153c-7253-46f1-9c20-d737666554b7'
SOURCE_PATH = 'pictographic-primitives/technology/drone controller_533f153c-7253-46f1-9c20-d737666554b7.svg'
AUTHOR = 'gpt-6'

class DroneRemoteController(Solo48):
    icon_id = 'drone-remote-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('remote', 'controller', 'drone', 'joystick', 'antenna', 'signal', 'transmitter')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
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
        box('body',6,20,42,42,5)
        circle('dial-left',17,31,2);circle('dial-right',31,31,2)
        line('antenna',(24,20),(24,10));connect('antenna','body')
        arc('signal-left',(12,6),(12,10),10,sweep=False)
        arc('signal-right',(36,6),(36,10),10,sweep=True)
