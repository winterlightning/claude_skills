"""Electric toothbrush paired with a phone. Square envelope, centerline extremes 6/6/42/42. Lucide smartphone rounded rectangle construction inspected earlier; one signal arc replaces two and phone footer omitted to preserve clear device shapes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'daebb644-0ba7-42d0-83a7-0593009cd417'
SOURCE_PATH = 'pictographic-primitives/technology/smart ultra sonic tooth brush_daebb644-0ba7-42d0-83a7-0593009cd417.svg'
AUTHOR = 'gpt-6'

class SmartToothbrushAndPhone(Solo48):
    icon_id = 'smart-toothbrush-and-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('toothbrush', 'electric', 'ultrasonic', 'phone', 'smart', 'wireless', 'dental')

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
        poly('brush-head',(6,6),(14,6),(14,16),(10,16),(6,16),closed=True)
        line('neck',(10,16),(10,26));connect('neck','brush-head')
        poly('handle',(6,26),(10,26),(14,26),(14,42),(6,42),closed=True);connect('handle','neck')
        box('phone',26,22,42,42,4)
        arc('wireless',(24,12),(36,12),6,4)
