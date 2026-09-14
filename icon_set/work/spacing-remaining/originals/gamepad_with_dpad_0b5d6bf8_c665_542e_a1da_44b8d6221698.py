"""Gamepad with mirrored grips and a D-pad. Lucide gamepad-2 controls and coherent grip contour; single reference button retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b5d6bf8-c665-542e-a1da-44b8d6221698'
SOURCE_PATH = 'pictographic-primitives/technology/controller_0b5d6bf8-c665-542e-a1da-44b8d6221698.svg'
AUTHOR = 'gpt-6'

class GamepadWithDpad(Solo48):
    icon_id = 'gamepad-with-dpad'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('controller', 'gamepad', 'game', 'gaming', 'joypad', 'console', 'play')

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
        line('top',(14,8),(34,8))
        arc('tr',(34,8),(42,18),10)
        line('right',(42,18),(42,32))
        arc('grip-r',(42,32),(28,32),8)
        arc('notch',(28,32),(20,32),4,sweep=False)
        arc('grip-l',(20,32),(6,32),8)
        line('left',(6,32),(6,18))
        arc('tl',(6,18),(14,8),10)
        contour('shell','top','tr','right','grip-r','notch','grip-l','left','tl',closed=True)
        poly('dpad-h',(13,20),(17,20),(21,20))
        poly('dpad-v',(17,17),(17,20),(17,22))
        connect('dpad-h','dpad-v')
        circle('button',33,20,2)
