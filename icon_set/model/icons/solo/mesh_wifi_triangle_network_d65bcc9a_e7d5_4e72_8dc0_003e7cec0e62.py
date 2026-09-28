"""Three square nodes connected in a triangle. Square envelope; Lucide network node/link construction. One central wireless arc retains room around the links."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd65bcc9a-e7d5-4e72-8dc0-003e7cec0e62'
SOURCE_PATH = 'pictographic-primitives/technology/mesh wifi 1_d65bcc9a-e7d5-4e72-8dc0-003e7cec0e62.svg'
AUTHOR = 'gpt-6'

class MeshWifiTriangleNetwork(Solo48):
    icon_id = 'mesh-wifi-triangle-network'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'network', 'nodes', 'wireless', 'router', 'connection')

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
        poly('left-node',(6,6),(16,6),(16,11),(16,16),(6,16),closed=True)
        poly('right-node',(32,6),(42,6),(42,16),(32,16),(32,11),closed=True)
        poly('bottom-node',(19,32),(29,32),(29,42),(19,42),closed=True)
        line('top-link',(16,11),(32,11));connect('top-link','left-node');connect('top-link','right-node')
        line('left-link',(6,16),(19,42));connect('left-link','left-node');connect('left-link','bottom-node')
        line('right-link',(42,16),(29,42));connect('right-link','right-node');connect('right-link','bottom-node')
        arc('wifi',(20,23),(28,23),12)
