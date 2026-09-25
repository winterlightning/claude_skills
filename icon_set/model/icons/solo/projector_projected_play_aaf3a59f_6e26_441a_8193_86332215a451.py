"""Video projector casting a play symbol. Square extremes 6/6/42/42. Preserve round lens and projected triangle; tiny feet omitted. Two outward beam lines retain the fan-shaped projection. No exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aaf3a59f-6e26-441a-8193-86332215a451'
SOURCE_PATH = 'pictographic-primitives/technology/video projector_aaf3a59f-6e26-441a-8193-86332215a451.svg'
AUTHOR = 'gpt-6'

class ProjectorProjectedPlay(Solo48):
    icon_id = 'projector-projected-play'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('projector', 'video', 'play', 'projection', 'beam', 'movie', 'media')

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
        poly('projector',(20,32),(12,32),(12,42),(36,42),(36,32),(28,32))
        circle('lens',24,32,4);connect('lens','projector')
        poly('play',(18,6),(30,13),(18,20),closed=True)

        line('left-beam',(6,6),(8,22));line('right-beam',(42,6),(40,22))
