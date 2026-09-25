"""Headphones surrounded by four corner sound arcs. Square envelope, centerline extremes 6/6/42/42. Lucide headphones informs continuous headband and paired earcups; one arc at each corner replaces doubled waves."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '26f8e500-f2dc-4308-8c75-2f092c971873'
SOURCE_PATH = 'pictographic-primitives/technology/spatial audio headphone_26f8e500-f2dc-4308-8c75-2f092c971873.svg'
AUTHOR = 'gpt-6'

class SurroundSoundHeadphones(Solo48):
    icon_id = 'surround-sound-headphones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('headphones', 'spatial-audio', 'surround', 'sound', 'audio', 'music', 'waves')

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
        arc('band',(12,23),(36,23),12)
        poly('left-cup',(12,23),(20,23),(20,31),(12,31),closed=True);connect('left-cup','band')
        poly('right-cup',(36,23),(28,23),(28,31),(36,31),closed=True);connect('right-cup','band')
        arc('tl',(6,10),(10,6),4,sweep=False)
        arc('tr',(38,6),(42,10),4,sweep=False)
        arc('bl',(10,42),(6,38),4,sweep=False)
        arc('br',(42,38),(38,42),4,sweep=False)
