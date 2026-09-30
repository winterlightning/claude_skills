"""Two diagonally arranged linked wireless routers. Square envelope; Lucide router silhouette. Antennas retained; repeated radio arcs omitted to preserve the device pair and link."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a93e8de-6f91-4fe6-b134-63af89e10c77'
SOURCE_PATH = 'pictographic-primitives/technology/mesh wifi_5a93e8de-6f91-4fe6-b134-63af89e10c77.svg'
AUTHOR = 'gpt-6'

class TwoLinkedWifiRouters(Solo48):
    icon_id = 'two-linked-wifi-routers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'router', 'network', 'wireless', 'antenna', 'connection')

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
        poly('router-one',(6,16),(15,16),(24,16),(24,26),(20,26),(6,26),closed=True)
        poly('router-two',(24,32),(28,32),(33,32),(42,32),(42,42),(24,42),closed=True)
        line('antenna-one',(15,6),(15,16));connect('antenna-one','router-one')
        line('antenna-two',(33,22),(33,32));connect('antenna-two','router-two')
        line('link',(20,26),(28,32));connect('link','router-one');connect('link','router-two')
