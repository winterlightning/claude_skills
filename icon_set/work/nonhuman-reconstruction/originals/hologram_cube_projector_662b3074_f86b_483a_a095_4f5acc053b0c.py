"""Hologram cube above a projector base. Square extremes 6/6/42/42. Lucide box face junctions; retain floating cube and two outward beams. Lens omitted to keep the cube and projector separated at native size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '662b3074-f86b-483a-a095-4f5acc053b0c'
SOURCE_PATH = 'pictographic-primitives/technology/virtual box_662b3074-f86b-483a-a095-4f5acc053b0c.svg'
AUTHOR = 'gpt-6'

class HologramCubeProjector(Solo48):
    icon_id = 'hologram-cube-projector'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hologram', 'projector', 'cube', 'virtual', '3d', 'projection', 'object')

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
        poly('cube',(14,12),(24,6),(34,12),(34,20),(24,26),(14,20),closed=True)
        poly('top-face',(14,12),(24,16),(34,12));connect('top-face','cube')
        line('edge',(24,16),(24,26));connect('edge','cube');connect('edge','top-face')
        poly('base',(14,34),(34,34),(34,42),(14,42),closed=True)
        line('left-beam',(6,24),(8,28));line('right-beam',(42,24),(40,28))
