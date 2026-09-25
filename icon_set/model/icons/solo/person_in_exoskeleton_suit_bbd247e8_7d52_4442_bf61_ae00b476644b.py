"""Standing figure in a rigid exoskeleton. Square envelope; mirrored outer braces and inner legs. Lucide person-standing hierarchy. Small joint circles and doubled arm outlines omitted; shoulder frame and four vertical supports retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bbd247e8-7d52-4442-bf61-ae00b476644b'
SOURCE_PATH = 'pictographic-primitives/technology/robot exo skeleton suit_bbd247e8-7d52-4442-bf61-ae00b476644b.svg'
AUTHOR = 'gpt-6'

class PersonInExoskeletonSuit(Solo48):
    icon_id = 'person-in-exoskeleton-suit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('exoskeleton', 'suit', 'person', 'robotic', 'wearable', 'power-armor', 'assist')

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
        circle('head',24,9,3)
        poly('frame',(6,30),(6,22),(14,21),(16,21),(24,21),(32,21),(34,21),(42,22),(42,30))
        poly('body',(16,21),(16,32),(16,42));connect('body','frame')
        poly('right-leg',(32,21),(32,32),(32,42));connect('right-leg','frame')
        line('waist',(16,32),(32,32));connect('waist','body');connect('waist','right-leg')
        line('left-brace',(6,30),(6,42));connect('left-brace','frame')
        line('right-brace',(42,30),(42,42));connect('right-brace','frame')
