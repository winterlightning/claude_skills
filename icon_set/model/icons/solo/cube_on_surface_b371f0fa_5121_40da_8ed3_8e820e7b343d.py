"""Isometric cube above a V-shaped surface. Square extremes 6/6/42/42. Lucide box informs shared face junctions; separate side dashes omitted so the placement surface remains clear."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b371f0fa-5121-40da-8ed3-8e820e7b343d'
SOURCE_PATH = 'pictographic-primitives/technology/tools reality composer pro_b371f0fa-5121-40da-8ed3-8e820e7b343d.svg'
AUTHOR = 'gpt-6'

class CubeOnSurface(Solo48):
    icon_id = 'cube-on-surface'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('cube', '3d', 'object', 'surface', 'placement', 'reality-composer', 'model')

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
        poly('cube',(12,14),(24,6),(36,14),(36,26),(24,32),(12,26),closed=True)
        poly('top-face',(12,14),(24,21),(36,14));connect('top-face','cube')
        line('edge',(24,21),(24,32));connect('edge','top-face');connect('edge','cube')
        poly('surface',(6,32),(24,42),(42,32))
