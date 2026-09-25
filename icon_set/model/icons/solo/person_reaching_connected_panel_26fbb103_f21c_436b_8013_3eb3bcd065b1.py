"""Person reaching toward a connected panel. Square envelope; integral node wiring and reaching arm retained; Lucide person-standing simple figure construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '26fbb103-f21c-436b-8013-3eb3bcd065b1'
SOURCE_PATH = 'pictographic-primitives/technology/immersive reality_26fbb103-f21c-436b-8013-3eb3bcd065b1.svg'
AUTHOR = 'gpt-6'

class PersonReachingConnectedPanel(Solo48):
    icon_id = 'person-reaching-connected-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('immersive', 'person', 'panel', 'interaction', 'spatial', 'connection', 'virtual-reality')

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
        poly('panel',(6,10),(20,6),(20,12),(20,24),(10,22),(6,20),closed=True)
        poly('connector',(20,12),(29,12),(29,9),(36,9));connect('connector','panel')
        circle('node',39,9,3);connect('node','connector')
        line('stem',(10,22),(10,29));connect('stem','panel')
        circle('lower-node',10,32,3);connect('lower-node','stem')
        circle('head',36,26,3)
        chain('arm',(20,24),(25,33),(34,38))
        arc('shoulder',(34,38),(42,42),10)
        contour('person','arm-1','arm-2','shoulder');connect('person','panel')
