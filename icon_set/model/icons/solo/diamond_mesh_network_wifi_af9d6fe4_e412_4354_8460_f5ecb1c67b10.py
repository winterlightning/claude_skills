"""Four circular nodes in a connected diamond. Square envelope; Lucide network shared links and circular hierarchy; one Wi-Fi arc replaces repeated arcs and the crowded signal dot."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af9d6fe4-e412-4354-8460-f5ecb1c67b10'
SOURCE_PATH = 'pictographic-primitives/technology/mesh wifi 3_af9d6fe4-e412-4354-8460-f5ecb1c67b10.svg'
AUTHOR = 'gpt-6'

class DiamondMeshNetworkWifi(Solo48):
    icon_id = 'diamond-mesh-network-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'network', 'nodes', 'wireless', 'topology', 'connection')

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
        for n,x,y in [('top',24,10),('left',10,24),('right',38,24),('bottom',24,38)]:circle(n,x,y,4)
        for n,a,b,u,v in [('tl',(20,10),(10,20),'top','left'),('tr',(28,10),(38,20),'top','right'),('bl',(10,28),(20,38),'left','bottom'),('br',(28,38),(38,28),'bottom','right')]:
            line(n,a,b);connect(n,u);connect(n,v)
        arc('wifi',(22,25),(26,25),3)
