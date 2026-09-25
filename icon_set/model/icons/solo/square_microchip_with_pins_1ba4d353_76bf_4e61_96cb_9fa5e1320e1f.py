"""Square microchip with two pins on each side. Square envelope, centerline extremes 6/6/42/42. Lucide cpu informs rounded body and orthogonal pin layout; blank face preserved, no extra inner die added."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ba4d353-76bf-4e61-96cb-9fa5e1320e1f'
SOURCE_PATH = 'pictographic-primitives/technology/safety helmet mine_1ba4d353-76bf-4e61-96cb-9fa5e1320e1f.svg'
AUTHOR = 'gpt-6'

class SquareMicrochipWithPins(Solo48):
    icon_id = 'square-microchip-with-pins'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('chip', 'microchip', 'processor', 'cpu', 'circuit', 'hardware', 'semiconductor')

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
        chain('top',(18,14),(20,14),(28,14),(30,14));arc('tr',(30,14),(34,18),4)
        chain('right',(34,18),(34,20),(34,28),(34,30));arc('br',(34,30),(30,34),4)
        chain('bottom',(30,34),(28,34),(20,34),(18,34));arc('bl',(18,34),(14,30),4)
        chain('left',(14,30),(14,28),(14,20),(14,18));arc('tl',(14,18),(18,14),4)
        contour('chip','top-1','top-2','top-3','tr','right-1','right-2','right-3','br','bottom-1','bottom-2','bottom-3','bl','left-1','left-2','left-3','tl',closed=True)
        for i,p in enumerate([20,28]):
            line(f'pin-top-{i}',(p,6),(p,14));connect(f'pin-top-{i}','chip')
            line(f'pin-bottom-{i}',(p,34),(p,42));connect(f'pin-bottom-{i}','chip')
            line(f'pin-left-{i}',(6,p),(14,p));connect(f'pin-left-{i}','chip')
            line(f'pin-right-{i}',(34,p),(42,p));connect(f'pin-right-{i}','chip')
