"""Delivery robot holding a tall parcel overhead with raised arms. Square envelope; Lucide bot rounded body and sparse face. Hatch and tiny claws omitted; parcel tape becomes a short attached line."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '902b574c-e286-414e-8409-1ae25dfc15aa'
SOURCE_PATH = 'pictographic-primitives/technology/robot shipping box_902b574c-e286-414e-8409-1ae25dfc15aa.svg'
AUTHOR = 'gpt-6'

class RobotCarryingShippingBox(Solo48):
    icon_id = 'robot-carrying-shipping-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('robot', 'delivery', 'parcel', 'shipping', 'box', 'logistics', 'carrier')

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
        box('body',10,24,38,42,4)
        poly('parcel',(14,6),(24,6),(34,6),(34,24),(14,24),closed=True);connect('parcel','body')
        line('tape',(24,6),(24,13));connect('tape','parcel')
        self.add_dot('left-eye',(19,33));self.add_dot('right-eye',(29,33))
        poly('left-arm',(10,30),(6,24),(6,16));connect('left-arm','body')
        poly('right-arm',(38,30),(42,24),(42,16));connect('right-arm','body')
