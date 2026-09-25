"""Cone in front of a sphere. Square envelope reaches left/right 6/42 and top/bottom 6/42. Keep overlap and curved cone base; sphere hidden behind cone. No exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '53810b6e-ae05-418f-a2d4-32bb79dc5fbd'
SOURCE_PATH = 'pictographic-primitives/technology/reality_53810b6e-ae05-418f-a2d4-32bb79dc5fbd.svg'
AUTHOR = 'gpt-6'

class ConeAndSphere(Solo48):
    icon_id = 'cone-and-sphere'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('shapes', 'cone', 'sphere', '3d', 'geometry', 'reality', 'objects')

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
        poly('cone-sides',(6,38),(18,18),(25,30),(30,38))
        arc('base',(30,38),(6,38),12,4,sweep=True);connect('base','cone-sides')
        arc('sphere-top',(18,18),(42,18),12)
        arc('sphere-bottom',(42,18),(30,30),12)
        line('sphere-end',(30,30),(25,30))
        contour('sphere','sphere-top','sphere-bottom','sphere-end');connect('sphere','cone-sides')
