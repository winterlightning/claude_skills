"""Capsule smart-lock plate with round hub and rightward lever. Square envelope, centerline extremes 6/6/42/42. Preserve the intentionally rightward projection; identical source pair retained as separate UUID-bearing outputs. Lucide lock construction informs simple rounded hardware."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '409658ba-fe28-41c4-b8c0-6a94ed4b10dd'
SOURCE_PATH = 'pictographic-primitives/technology/smart lock_409658ba-fe28-41c4-b8c0-6a94ed4b10dd.svg'
AUTHOR = 'gpt-6'

class RoundSmartLock(Solo48):
    icon_id = 'round-smart-lock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('smart-lock', 'lock', 'door', 'knob', 'lever', 'security', 'home')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x+r,y),r)
            arc(n+'b',(x+r,y),(x,y+r),r)
            arc(n+'c',(x,y+r),(x-r,y),r)
            arc(n+'d',(x-r,y),(x,y-r),r)
            contour(n,n+'a',n+'b',n+'c',n+'d',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        arc('top',(6,18),(30,18),12)
        chain('right',(30,18),(30,26),(30,30))
        arc('bottom',(30,30),(6,30),12)
        line('left',(6,30),(6,18));contour('plate','top','right-1','right-2','bottom','left',closed=True)
        circle('hub',18,26,4)
        poly('lever',(22,26),(30,26),(42,26));connect('lever','hub');connect('lever','plate')
