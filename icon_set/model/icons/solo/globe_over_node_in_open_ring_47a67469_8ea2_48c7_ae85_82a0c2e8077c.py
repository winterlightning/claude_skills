"""Globe over node within open circular network ring. Radial envelope admits a legible continent division and detached node; continent simplified to one smooth S-shaped division."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47a67469-8ea2-48c7-ae85-82a0c2e8077c'
SOURCE_PATH = 'pictographic-primitives/technology/amazon web service cross region data delivery 1_47a67469-8ea2-48c7-ae85-82a0c2e8077c.svg'
AUTHOR = 'gpt-6'

class GlobeOverNodeInOpenRing(Solo48):
    icon_id = 'globe-over-node-in-open-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('globe', 'world', 'region', 'network', 'cloud', 'delivery', 'node', 'data')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
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
        arc('ring-a',(12,40),(6,24),20)
        arc('ring-b',(6,24),(24,6),20)
        arc('ring-c',(24,6),(42,24),20)
        arc('ring-d',(42,24),(36,40),20)
        contour('ring','ring-a','ring-b','ring-c','ring-d')
        circle('globe',24,22,9)
        arc('land-a',(24,13),(24,22),6,sweep=False)
        arc('land-b',(24,22),(24,31),6,sweep=True)
        contour('land','land-a','land-b');connect('land','globe')
        circle('node',24,42,2)
