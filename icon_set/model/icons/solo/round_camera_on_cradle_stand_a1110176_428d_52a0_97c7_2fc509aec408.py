"""Round camera suspended above a cradle stand. Square extremes 6/6/42/42. Concentric lens and camera retained; cradle and short base meet at a shared point. No exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1110176-428d-52a0-97c7-2fc509aec408'
SOURCE_PATH = 'pictographic-primitives/technology/toys racquet_a1110176-428d-52a0-97c7-2fc509aec408.svg'
AUTHOR = 'gpt-6'

class RoundCameraOnCradleStand(Solo48):
    icon_id = 'round-camera-on-cradle-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('camera', 'webcam', 'lens', 'stand', 'monitor', 'device', 'round')

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
        circle('camera',24,21,11);circle('lens',24,21,2)
        line('cord',(24,6),(24,10));connect('cord','camera')
        arc('cradle-left',(6,30),(24,42),18,12,sweep=False)
        arc('cradle-right',(24,42),(42,30),18,12,sweep=False);contour('cradle','cradle-left','cradle-right')
        poly('base',(18,42),(24,42),(30,42));connect('base','cradle')
