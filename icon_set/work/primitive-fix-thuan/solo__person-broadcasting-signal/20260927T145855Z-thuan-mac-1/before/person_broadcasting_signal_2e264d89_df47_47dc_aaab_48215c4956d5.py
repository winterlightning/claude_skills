"""Person broadcasting with two chest-level signal arcs. Square envelope, centerline extremes 6/6/42/42. Mirrored shoulder curves and shared signal axis; circle head retained. Lucide person-standing head hierarchy and radio-tower nested signal rhythm."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2e264d89-df47-47dc-aaab-48215c4956d5'
SOURCE_PATH = 'pictographic-primitives/technology/signal tower node 5g_2e264d89-df47-47dc-aaab-48215c4956d5.svg'
AUTHOR = 'gpt-6'

class PersonBroadcastingSignal(Solo48):
    icon_id = 'person-broadcasting-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('signal', 'person', 'node', '5g', 'broadcast', 'wireless', 'user')

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
        circle('head',24,11,5)
        arc('left-shoulder',(6,42),(14,24),8,18)
        arc('right-shoulder',(34,24),(42,42),8,18)
        arc('outer-wave',(18,33),(30,33),6,3)
        arc('inner-wave',(20,42),(28,42),4,1)
