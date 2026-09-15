"""Pitched-roof house on a network post. Square envelope, centerline extremes 6/6/42/42. Mirror roof, walls and door; preserve post and wide horizontal network base. No exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f1eba82-917c-4c8f-926d-350b09b272d4'
SOURCE_PATH = 'pictographic-primitives/technology/smart house_7f1eba82-917c-4c8f-926d-350b09b272d4.svg'
AUTHOR = 'gpt-6'

class HouseOnNetworkPost(Solo48):
    icon_id = 'house-on-network-post'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('house', 'home', 'smart-home', 'network', 'post', 'building', 'connected')

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
        poly('house',(10,18),(10,32),(20,32),(24,32),(28,32),(38,32),(38,18),(24,6),closed=True)
        poly('door',(20,32),(20,23),(28,23),(28,32));connect('door','house')
        line('post',(24,32),(24,42));connect('post','house')
        poly('network',(6,42),(24,42),(42,42));connect('network','post')
