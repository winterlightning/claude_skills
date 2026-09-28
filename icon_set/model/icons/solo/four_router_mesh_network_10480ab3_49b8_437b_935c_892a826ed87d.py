"""Four twin-antenna routers in a two-by-two mesh. Square envelope; Lucide router body/antenna construction. Horizontal and diagonal links retain a connected four-router graph; vertical links omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10480ab3-49b8-437b-935c-892a826ed87d'
SOURCE_PATH = 'pictographic-primitives/technology/mesh wifi 2_10480ab3-49b8-437b-935c-892a826ed87d.svg'
AUTHOR = 'gpt-6'

class FourRouterMeshNetwork(Solo48):
    icon_id = 'four-router-mesh-network'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'routers', 'network', 'wireless', 'nodes', 'connection')

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
        for n,x,y in [('tl',6,10),('tr',32,10),('bl',6,34),('br',32,34)]:
            poly(n,(x,y),(x+10,y),(x+10,y+4),(x+10,y+8),(x,y+8),(x,y+4),closed=True)
            for side,xx in [('l',x),('r',x+10)]:
                line(n+'-ant-'+side,(xx,y-4),(xx,y));connect(n+'-ant-'+side,n)
        line('top-link',(16,14),(32,14));connect('top-link','tl');connect('top-link','tr')
        line('bottom-link',(16,38),(32,38));connect('bottom-link','bl');connect('bottom-link','br')
        line('diagonal',(16,18),(32,34));connect('diagonal','tl');connect('diagonal','br');connect('diagonal','br-ant-l')
