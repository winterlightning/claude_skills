"""Laser projector with a centered round lens and rising beams. Square envelope, centerline extremes 6/6/42/42. Two widening arcs replace three; lens sits in a split body edge. Shared axis and matched device sides; no exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1db65932-f61e-42a1-a8d7-c48bf56a25a4'
SOURCE_PATH = 'pictographic-primitives/technology/smart laser projector_1db65932-f61e-42a1-a8d7-c48bf56a25a4.svg'
AUTHOR = 'gpt-6'

class LaserProjectorWithBeams(Solo48):
    icon_id = 'laser-projector-with-beams'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('projector', 'laser', 'beam', 'lens', 'smart', 'device', 'projection')

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
        poly('body',(18,30),(6,30),(6,42),(42,42),(42,30),(30,30))
        circle('lens',24,30,6);connect('body','lens')
        arc('wide-beam',(10,10),(38,10),14,4)
        arc('inner-beam',(18,17),(30,17),6,2)
