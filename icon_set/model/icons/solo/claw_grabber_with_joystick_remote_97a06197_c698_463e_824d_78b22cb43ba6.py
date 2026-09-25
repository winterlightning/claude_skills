"""Mechanical grabber with joystick remote. Square physical-control scene; circular pivots and split contact nodes. Single radio arc and simplified trapezoid base."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97a06197-c698-463e-824d-78b22cb43ba6'
SOURCE_PATH = 'pictographic-primitives/technology/gripping vice controller_97a06197-c698-463e-824d-78b22cb43ba6.svg'
AUTHOR = 'gpt-6'

class ClawGrabberWithJoystickRemote(Solo48):
    icon_id = 'claw-grabber-with-joystick-remote'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('claw', 'gripper', 'joystick', 'remote', 'robotics', 'control', 'vice', 'wireless')

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
        poly('suspension-left',(10,6),(12,18));poly('suspension-right',(24,6),(22,18))
        circle('hub',17,18,5);connect('suspension-left','hub');connect('suspension-right','hub')
        poly('jaw-left',(12,18),(6,24),(10,30));connect('jaw-left','hub');connect('jaw-left','suspension-left')
        poly('jaw-right',(22,18),(26,24),(22,30));connect('jaw-right','hub');connect('jaw-right','suspension-right')
        circle('stick-ball',37,27,3)
        line('stick',(37,30),(37,42));connect('stick','stick-ball')
        poly('base',(28,42),(37,42),(42,42));connect('stick','base')
        arc('signal',(32,10),(42,14),12)
