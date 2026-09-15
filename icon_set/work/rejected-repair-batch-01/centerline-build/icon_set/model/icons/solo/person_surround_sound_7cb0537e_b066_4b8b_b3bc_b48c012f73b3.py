"""Head-and-shoulders listener surrounded by four corner sound arcs. Square envelope, centerline extremes 6/6/42/42. Lucide person-standing head hierarchy; four single arcs replace paired corner waves, mirrored about the listener."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7cb0537e-b066-4b8b-b3bc-b48c012f73b3'
SOURCE_PATH = 'pictographic-primitives/technology/spatial audio user surround_7cb0537e-b066-4b8b-b3bc-b48c012f73b3.svg'
AUTHOR = 'gpt-6'

class PersonSurroundSound(Solo48):
    icon_id = 'person-surround-sound'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('spatial-audio', 'surround', 'person', 'sound', 'listener', 'audio', 'waves')

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
        circle('head',24,13,3)
        arc('shoulders',(16,31),(32,31),8,6)
        arc('tl',(6,10),(10,6),4,sweep=False)
        arc('tr',(38,6),(42,10),4,sweep=False)
        arc('bl',(10,42),(6,38),4,sweep=False)
        arc('br',(42,38),(38,42),4,sweep=False)
