"""House projected above a flat projector. Square extremes 6/6/42/42. Physical projection scene retained; hosted play triangle and lens omitted because neither fits with safe clearance inside the small house/projector. Two feet distinguish this version. No exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01d3426e-07f3-494a-a30e-0560137a535e'
SOURCE_PATH = 'pictographic-primitives/technology/virtual home_01d3426e-07f3-494a-a30e-0560137a535e.svg'
AUTHOR = 'gpt-6'

class ProjectorVideoHouse(Solo48):
    icon_id = 'projector-video-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('virtual-home', 'projector', 'house', 'video', 'play', 'hologram', 'smart-home')

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
        poly('house',(14,14),(24,6),(34,14),(34,24),(14,24),closed=True)

        poly('base',(6,32),(42,32),(42,40),(34,40),(14,40),(6,40),closed=True)
        line('left-foot',(14,40),(14,42));line('right-foot',(34,40),(34,42));connect('left-foot','base');connect('right-foot','base')
