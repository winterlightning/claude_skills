"""Explorer rover with two wheels, camera mast and articulated grabber arm. Square envelope. Circular wheel construction and simple connected chassis; gripper reduced to an open angled hook, tiny hub dots omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1a889d5-dac3-48fb-ae76-990e1d90bcd0'
SOURCE_PATH = 'pictographic-primitives/technology/robot explorer_e1a889d5-dac3-48fb-ae76-990e1d90bcd0.svg'
AUTHOR = 'gpt-6'

class ExplorerRobotRover(Solo48):
    icon_id = 'explorer-robot-rover'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('rover', 'robot', 'explorer', 'space', 'vehicle', 'wheels', 'robotic-arm')

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
        circle('wheel-left',12,36,6);circle('wheel-right',36,36,6)
        poly('chassis',(12,30),(12,24),(28,24),(36,24),(36,30));connect('chassis','wheel-left');connect('chassis','wheel-right')
        line('axle',(18,36),(30,36));connect('axle','wheel-left');connect('axle','wheel-right')
        poly('camera',(6,6),(16,6),(16,14),(12,14),(6,14),closed=True)
        line('mast',(12,14),(12,24));connect('mast','camera');connect('mast','chassis')
        poly('arm',(28,24),(26,14),(34,6),(42,10),(38,16));connect('arm','chassis')
